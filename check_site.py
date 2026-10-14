from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import json,re
root=Path(__file__).parent/'dist'
class Page(HTMLParser):
 def __init__(self):super().__init__();self.ids=set();self.refs=[];self.h1=0;self.errors=[];self.labels=set();self.fields=[];self.title=False;self.lang=None
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='html':self.lang=a.get('lang')
  if tag=='h1':self.h1+=1
  if tag=='title':self.title=True
  if 'id'in a:
   if a['id']in self.ids:self.errors.append('Duplicate id '+a['id'])
   self.ids.add(a['id'])
  if tag=='img' and not a.get('alt'):self.errors.append('Missing image alt')
  if tag=='label' and 'for'in a:self.labels.add(a['for'])
  if tag in ['input','textarea'] and a.get('type')!='checkbox':self.fields.append(a.get('id'))
  for field in ['href','src']:
   if field in a:self.refs.append(a[field])
pages={};errors=[]
for p in root.rglob('*.html'):
 data=p.read_text();parser=Page();parser.feed(data);pages[p.resolve()]=parser
 if parser.h1!=1:parser.errors.append(f'Expected 1 h1, got {parser.h1}')
 if not parser.title or parser.lang not in ['es','en']:parser.errors.append('Missing title or valid language')
 if re.search(r'@[a-z-]+@',data):parser.errors.append('Unresolved template token')
 if not set(parser.fields)<=parser.labels:parser.errors.append('Unlabelled form field')
 errors.extend(f'{p.relative_to(root)}: {e}'for e in parser.errors)
for p,parser in pages.items():
 for ref in parser.refs:
  u=urlsplit(ref)
  if u.scheme or u.netloc:continue
  target=(p.parent/unquote(u.path)).resolve() if u.path else p
  if not target.exists():errors.append(f'{p.relative_to(root.resolve())}: missing {ref}')
  elif u.fragment and target in pages and u.fragment not in pages[target].ids:errors.append(f'{p.name}: missing fragment {ref}')
result={'html_pages':len(pages),'local_references_checked':sum(len(x.refs)for x in pages.values()),'errors':errors,'browser_visual_QA':'Not run: local server EPERM; file navigation blocked by browser policy; hosting source synchronization DNS failure.'}
(Path(__file__).parent/'validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
print(json.dumps(result,ensure_ascii=False,indent=2))
raise SystemExit(bool(errors))
