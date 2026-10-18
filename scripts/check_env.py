"""Preflight: Python version and the two libraries the scripts need."""
import sys

ok = sys.version_info >= (3, 9)
print(f"python {sys.version.split()[0]}: {'ok' if ok else 'need 3.9+'}")
for mod in ("pandas", "openpyxl"):
    try:
        m = __import__(mod)
        print(f"{mod} {m.__version__}: ok")
    except ImportError:
        ok = False
        print(f"{mod}: missing (pip install -r requirements.txt)")
sys.exit(0 if ok else 1)
