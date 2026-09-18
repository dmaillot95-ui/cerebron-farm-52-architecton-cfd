import subprocess,sys,json,pathlib
r=subprocess.run([sys.executable,"worker/cfd_mvp.py"],check=False)
assert r.returncode==0
x=json.loads(pathlib.Path("artifacts/cfd_mvp.json").read_text())
assert x["passed"] is True
assert x["reynolds"]==1000.0
