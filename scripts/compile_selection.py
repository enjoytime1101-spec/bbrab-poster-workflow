"""Compile one preset SVG for the executable Remotion workflow. No model calls."""
import argparse,json,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'templates'))
from aerospace_design import svg,HOLIDAYS,VARIANTS
p=argparse.ArgumentParser();p.add_argument('profile',type=Path);p.add_argument('--variant',choices=VARIANTS,default='orbit');p.add_argument('--output',type=Path,required=True);args=p.parse_args()
d=json.loads(args.profile.read_text())
if set(d)!={'brand','industry','holiday'} or not isinstance(d['brand'],str) or not 1<=len(d['brand'].strip())<=32 or any(ord(c)<32 for c in d['brand']) or d['industry'] not in ('satellite','rocket') or d['holiday'] not in HOLIDAYS:
 p.error('Expected brand (1–32 chars), industry satellite/rocket, and supported holiday')
args.output.mkdir(parents=True,exist_ok=True)
(args.output/'input.json').write_text(json.dumps({'svg':svg(d,args.variant),'variant':args.variant},ensure_ascii=False))
print('Compiled fixed-template input; PNG/MP4 require the Remotion renderer.')
