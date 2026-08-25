#!/usr/bin/env python3
"""Validate RND-005 Made-in-China.com dossier data against SITE-DOSSIER v1.1."""
from __future__ import annotations
import csv
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

HERE=Path(__file__).resolve().parent
RAW=HERE/'dimensions-raw.csv'; OUT=HERE/'dimensions.csv'; PATHS=HERE/'guest-paths.csv'
EXPECTED=[f'D{i:02d}' for i in range(74)]
STRUCT=['actor','input','output','page_module','entity','event','state','error_exception','document','personal_data','risk','handoff']
BASE=['record_id','dimension_id','group','field_name','question','evidence_state','observed_fact','evidence_url','evidence_type','observed_at','region','access_mode','confidence']
NUM=['metric_name','metric_value','metric_unit','metric_currency','metric_period','metric_territory','metric_classification','metric_method','metric_publisher','source_title','source_publication_date']

def https(v):
 p=urlparse(v); return p.scheme=='https' and bool(p.netloc)

def main():
 with RAW.open(encoding='utf-8',newline='') as f: rows=list(csv.DictReader(f))
 errors=[]
 ids=[r['dimension_id'] for r in rows]
 if ids!=EXPECTED: errors.append('dimension sequence must be D00..D73 exactly once')
 processed=[]
 for r in rows:
  e=[]; did=r.get('dimension_id','?')
  for k in BASE+STRUCT:
   if not r.get(k,'').strip(): e.append(f'missing {k}')
  if r.get('evidence_state') not in {'observed','observed-not-found'}: e.append('invalid evidence_state')
  if r.get('confidence') not in {'high','medium','low'}: e.append('invalid confidence')
  if not https(r.get('evidence_url','')): e.append('evidence_url must be full HTTPS')
  if r.get('evidence_state')=='observed-not-found' and (not r.get('gap_reason','').strip() or not r.get('next_method','').strip()): e.append('not-found lacks gap_reason/next_method')
  if r.get('metric_value','').strip():
   for k in NUM:
    if not r.get(k,'').strip(): e.append(f'numeric claim missing {k}')
  processed.append({**r,'validation_status':'pass' if not e else 'fail','validation_errors':'; '.join(e),'template_version':'RND-D00-D73-v1.1'})
  errors += [f'{did}: {x}' for x in e]
 with OUT.open('w',encoding='utf-8',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(processed[0]),lineterminator='\n'); w.writeheader(); w.writerows(processed)
 with PATHS.open(encoding='utf-8',newline='') as f: paths=list(csv.DictReader(f))
 for i,r in enumerate(paths,1):
  for k in ['path_id','actor','step','goal','page_module','input','event','state_before','state_after','output','error_exception','document','personal_data','risk','handoff','evidence_state','evidence_url','observed_at','confidence']:
   if not r.get(k,'').strip(): errors.append(f'path row {i}: missing {k}')
  if not https(r.get('evidence_url','')): errors.append(f'path row {i}: invalid URL')
 actors=Counter(r['actor'] for r in paths)
 if actors['buyer_guest']<5 or actors['seller_guest']<5: errors.append('guest paths need at least 5 steps per actor')
 print(f"dimensions={len(rows)} unique={len(set(ids))} errors={len(errors)}")
 print('evidence_states='+repr(dict(sorted(Counter(r['evidence_state'] for r in rows).items()))))
 print('confidence='+repr(dict(sorted(Counter(r['confidence'] for r in rows).items()))))
 print('guest_paths='+repr(dict(sorted(actors.items()))))
 if errors: raise SystemExit('\n'.join(errors))
if __name__=='__main__': main()
