#!/usr/bin/env python3
import csv
from collections import Counter,defaultdict
from pathlib import Path
H=Path(__file__).parent; RAW=H/'matrix-raw.csv'; MATRIX=H/'matrix.csv'; FUND=H/'fundamentals.csv'; DEC=H/'decision-log.csv'
SITES={'alibaba','global-sources','made-in-china','indiamart','tradekey','ec21','exporthub'}
CAPS={'positioning','discovery','rfq','verification','storefront','messaging','sample','online-order','payment','protection','logistics','inspection','dispute','localization','monetization'}
def main():
 rows=list(csv.DictReader(RAW.open(encoding='utf-8'))); errors=[]; by=defaultdict(set); out=[]
 for r in rows:
  by[r['site']].add(r['capability'])
  for k in ['site','capability','dimension_id','evidence_state','observed_fact','source_report_url','source_data_url','source_evidence_url','accessed_at','confidence','limitations']:
   if not r.get(k):errors.append(f"{r.get('site')}/{r.get('capability')}: missing {k}")
  if r.get('evidence_state') not in {'observed','observed-not-found'}:errors.append('state')
  out.append({**r,'evidence_coverage_flag':'1' if r.get('evidence_state')=='observed' else '0','score_interpretation':'evidence coverage only; not quality, market rank, or capability performance'})
 if set(by)!=SITES:errors.append('site set')
 for s in SITES:
  if by[s]!=CAPS:errors.append(s+': capability set')
 with MATRIX.open('w',encoding='utf-8',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(out[0]),lineterminator='\n');w.writeheader();w.writerows(out)
 funds=list(csv.DictReader(FUND.open(encoding='utf-8')))
 if {r['site'] for r in funds}!=SITES or len(funds)!=7:errors.append('fundamentals')
 decisions=list(csv.DictReader(DEC.open(encoding='utf-8')))
 if not decisions:errors.append('decision log empty')
 print('matrix_rows=',len(rows),'sites=',len(by),'capabilities=',len(CAPS),'errors=',len(errors))
 print('coverage=',dict(Counter((x['site'],x['evidence_state']) for x in rows)))
 print('fundamentals=',len(funds),'decisions=',len(decisions))
 if errors:raise SystemExit('\n'.join(errors))
if __name__=='__main__':main()
