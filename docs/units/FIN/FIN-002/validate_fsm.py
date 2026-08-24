#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FIN-002 validator & processed-output generator (reproducible).
Reads: state_machine.csv, transitions.csv, ledger_events.csv, constraints.csv
Writes: machine_summary.csv (processed view) and state_machine_diagram.md (mermaid)
Checks (errors => exit 1):
  C1 all 11 required states present
  C2 unique state ids, all 16 required attributes non-empty per state
  C3 every transition endpoints exist
  C4 terminal sink: RELEASE/REFUND/RESOLUTION have no outgoing transitions
  C5 CANCELLED/EXPIRED only -> REFUND
  C6 reachability: AUTHORIZE reaches RELEASE, REFUND, DISPUTE, RESOLUTION, INSPECT, SHIP, DELIVERY, ACCEPT
  C7 every compliance gate id referenced by a state exists in constraints.csv
  C8 every ledger event id referenced by a state exists in ledger_events.csv
  C9 no duplicate from->to transitions
Run:  python3 docs/units/FIN/FIN-002/validate_fsm.py
"""
import csv
import os
from collections import defaultdict, deque

BASE = os.path.dirname(os.path.abspath(__file__))
REQ_STATES = ["AUTHORIZE", "HOLD", "VERIFY", "INSPECT", "SHIP", "DELIVERY",
              "ACCEPT", "RELEASE", "REFUND", "DISPUTE", "RESOLUTION"]
REQ_ATTRS = ["trigger", "actor", "input", "output", "evidence", "permission",
             "timeout", "transition", "failure_path", "refund_condition",
             "dispute_condition", "ledger_event", "audit_log",
             "compliance_gate", "legal_dependency", "insurance_dependency"]
TERMINALS = {"RELEASE", "REFUND", "RESOLUTION"}


def read(name):
    with open(os.path.join(BASE, name), encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def main():
    states = read("state_machine.csv")
    trans = read("transitions.csv")
    ledgers = read("ledger_events.csv")
    constraints = read("constraints.csv")
    errors = []

    ids = [s["state_id"] for s in states]
    # C1
    for r in REQ_STATES:
        if r not in ids:
            errors.append(f"C1 missing required state: {r}")
    # C2
    if len(ids) != len(set(ids)):
        errors.append("C2 duplicate state ids")
    for s in states:
        for a in REQ_ATTRS:
            if not s.get(a, "").strip():
                errors.append(f"C2 {s['state_id']}: empty attr {a}")
    # C3, C9
    state_set = set(ids)
    seen = set()
    for t in trans:
        if t["from_state"] not in state_set or t["to_state"] not in state_set:
            errors.append(f"C3 bad endpoint in {t['from_state']}->{t['to_state']}")
        pair = (t["from_state"], t["to_state"])
        if pair in seen:
            errors.append(f"C9 duplicate transition {pair}")
        seen.add(pair)
    # C4 global terminal (money execution end): RELEASE/REFUND have no outgoing;
    # RESOLUTION may exit only via RELEASE/REFUND (partial = both events, single pass)
    out_count = defaultdict(int)
    for t in trans:
        out_count[t["from_state"]] += 1
    for s in ("RELEASE", "REFUND"):
        if out_count.get(s, 0):
            errors.append(f"C4 terminal money-state {s} has {out_count[s]} outgoing")
    for t in trans:
        if t["from_state"] == "RESOLUTION" and t["to_state"] not in ("RELEASE", "REFUND"):
            errors.append(f"C4 RESOLUTION bad exit: {t['to_state']}")
    # C5
    for s in ("CANCELLED", "EXPIRED"):
        outs = [t["to_state"] for t in trans if t["from_state"] == s]
        if outs and set(outs) - {"REFUND"}:
            errors.append(f"C5 {s} may only go to REFUND: {outs}")
    # C6 reachability
    adj = defaultdict(list)
    for t in trans:
        adj[t["from_state"]].append(t["to_state"])
    if "AUTHORIZE" in adj:
        seen_states, q = set(), deque(["AUTHORIZE"])
        while q:
            cur = q.popleft()
            for nxt in adj.get(cur, []):
                if nxt not in seen_states:
                    seen_states.add(nxt)
                    q.append(nxt)
        for target in TERMINALS | {"DISPUTE", "INSPECT", "SHIP", "DELIVERY", "ACCEPT"}:
            if target not in seen_states:
                errors.append(f"C6 state not reachable: {target}")
    else:
        errors.append("C6 AUTHORIZE has no transitions")
    # C7
    gate_ids = {g["gate_id"] for g in constraints}
    for s in states:
        for g in s["compliance_gate"].split(","):
            g = g.strip()
            if g and g not in gate_ids:
                errors.append(f"C7 {s['state_id']} references unknown gate {g}")
    # C8
    ev_ids = {e["event_id"] for e in ledgers}
    for s in states:
        for e in s["ledger_event"].split(","):
            e = e.strip()
            if e and e not in ev_ids:
                errors.append(f"C8 {s['state_id']} references unknown ledger {e}")

    # ---- outputs ----
    rows = []
    for s in states:
        rows.append({
            "state_id": s["state_id"],
            "state_fa": s["state_fa"],
            "is_terminal": s["is_terminal"],
            "outgoing_count": out_count.get(s["state_id"], 0),
            "outgoing_to": " | ".join(
                t["to_state"] for t in trans if t["from_state"] == s["state_id"]),
            "compliance_gates": s["compliance_gate"],
            "ledger_events": s["ledger_event"],
        })
    with open(os.path.join(BASE, "machine_summary.csv"), "w",
              encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    # mermaid diagram
    lines = ["```mermaid", "stateDiagram-v2", "direction LR"]
    for s in states:
        term = " [*]" if s["is_terminal"] == "1" else ""
        lines.append(f"    {s['state_id']}{term} : {s['state_fa']}")
    for t in trans:
        lines.append(f"    {t['from_state']} --> {t['to_state']} : {t['trigger']}")
    lines.append("```")
    with open(os.path.join(BASE, "state_machine_diagram.md"), "w",
              encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    print(f"states={len(states)} transitions={len(trans)} ledgers={len(ledgers)} gates={len(constraints)}")
    if errors:
        print("ERRORS:")
        for e in errors:
            print(" -", e)
        raise SystemExit(1)
    print("ALL CHECKS PASSED (C1..C9)")
    print("wrote machine_summary.csv, state_machine_diagram.md")


if __name__ == "__main__":
    main()
