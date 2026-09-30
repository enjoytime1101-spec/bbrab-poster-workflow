"""Basic publication scan; not a guarantee of absence of sensitive data."""
import pathlib,re,subprocess,sys
patterns=[rb'gh[pousr]_[A-Za-z0-9]{30,}',rb'github_pat_[A-Za-z0-9_]{30,}',rb'sk-[A-Za-z0-9_-]{20,}',rb'-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----',rb'/Us' + rb'ers/[^/\s]+/',rb'(?i)authorization\s*:\s*bearer\s+[A-Za-z0-9._~-]{16,}']
root=pathlib.Path(__file__).resolve().parents[1]
files=subprocess.check_output(['git','ls-files','-z'],cwd=root).decode().split('\0')
bad=[]
for name in filter(None,files):
 p=root/name
 if p.suffix in ('.sqlite','.sqlite3','.db','.pem') or p.name.startswith('.env'):bad.append(name)
 if any(re.search(pattern,p.read_bytes()) for pattern in patterns):bad.append(name)
if '--history' in sys.argv:
 lines=subprocess.check_output(['git','rev-list','--objects','--all'],cwd=root).decode().splitlines()
 for line in lines:
  oid=line.split(' ',1)[0]
  if subprocess.check_output(['git','cat-file','-t',oid],cwd=root).strip()==b'blob':
   raw=subprocess.check_output(['git','cat-file','blob',oid],cwd=root)
   if any(re.search(pattern,raw) for pattern in patterns):bad.append('history blob '+oid)
print('Publication scan passed.' if not bad else '\n'.join(sorted(set(bad))))
sys.exit(bool(bad))
