#!/usr/bin/env python3
import csv
from collections import Counter,defaultdict
from pathlib import Path
from urllib.parse import urlparse
H=Path(__file__).parent; RAW=H/'dimensions-raw.csv'; OUT=H/'dimensions.csv'; PATHS=H/'guest-paths.csv'
SITES={'tradekey','ec21','exporthub'}; STRUCT=['actor','input','output','page_module','entity','event','state','error_exception','document','personal_data','risk','handoff']
def https(v):
 p=urlparse(v);return p.scheme=='https' and bool(p.netloc)
def main():
 rows=list(csv.DictReader(RAW.open(encoding='utf-8'))); errors=[]; by=defaultdict(list); processed=[]
 for r in rows:by[r['site']].append(r)
 if set(by)!=SITES:errors.append('site set mismatch')
 for site,items in by.items():
  if [x['dimension_id'] for x in items]!=[f'D{i:02d}' for i in range(74)]:errors.append(site+': dimensions mismatch')
 for r in rows:
  e=[]
  for k in ['site','record_id','dimension_id','field_name','question','evidence_state','observed_fact','evidence_url','evidence_type','observed_at','confidence']+STRUCT:
   if not r.get(k,'').strip():e.append('missing '+k)
  if r['evidence_state'] not in {'observed','observed-not-found'}:e.append('state')
  if r['confidence'] not in {'high','medium','low'}:e.append('confidence')
  if not https(r['evidence_url']):e.append('url')
  if r['evidence_state']=='observed-not-found' and (not r['gap_reason'] or not r['next_method']):e.append('notfound metadata')
  if r.get('metric_value'):
   for k in ['metric_name','metric_unit','metric_currency','metric_period','metric_territory','metric_classification','metric_method','metric_publisher','source_title','source_publication_date']:
    if not r.get(k):e.append('metric '+k)
  processed.append({**r,'validation_status':'pass' if not e else 'fail','validation_errors':';'.join(e),'template_version':'RND-D00-D73-v1.1'})
  errors += [r['site']+'/'+r['dimension_id']+':'+x for x in e]
 with OUT.open('w',encoding='utf-8',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(processed[0]),lineterminator='\n');w.writeheader();w.writerows(processed)
 paths=list(csv.DictReader(PATHS.open(encoding='utf-8'))); pc=Counter((x['site'],x['actor']) for x in paths)
 for x in paths:
  for k in ['site','path_id','actor','step','goal','page_module','state_before','state_after','output','error_exception','risk','handoff','evidence_url','observed_at','confidence']:
   if not x.get(k):errors.append('path missing '+k)
 for s in SITES:
  if pc[(s,'buyer_guest')]<5 or pc[(s,'seller_guest')]<5:errors.append(s+': paths')
 print('rows=',len(rows),'errors=',len(errors),'sites=',{s:len(by[s]) for s in sorted(SITES)})
 print('states=',dict(Counter((x['site'],x['evidence_state']) for x in rows)))
 print('paths=',dict(pc))
 if errors:raise SystemExit('\n'.join(errors))
if __name__=='__main__':main()
