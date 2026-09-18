import json,math,pathlib
# Hagen-Poiseuille benchmark, water-like fluid, laminar circular pipe.
rho=1000.0; mu=1.0e-3; D=0.01; L=1.0; v=0.1
Re=rho*v*D/mu
dp=32.0*mu*L*v/(D*D)
expected_Re=1000.0; expected_dp=32.0
passed=math.isclose(Re,expected_Re,rel_tol=1e-12) and math.isclose(dp,expected_dp,rel_tol=1e-12)
out={"benchmark":"laminar_pipe_closed_form","engine":"PY-CFD-MVP","reynolds":Re,"pressure_drop_pa":dp,"passed":passed,"evidence_level":"E2","limitations":["analytical laminar benchmark","not finite-volume CFD","not physical test"]}
pathlib.Path("artifacts").mkdir(exist_ok=True)
pathlib.Path("artifacts/cfd_mvp.json").write_text(json.dumps(out,indent=2),encoding="utf-8")
print(json.dumps(out,indent=2))
raise SystemExit(0 if passed else 1)
