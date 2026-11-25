"""Refuse a PR body that names no risk."""
import sys

body = sys.stdin.read()
if not any(ln.startswith("Risk: ") for ln in body.splitlines()):
    sys.exit("check: the PR body names no `Risk:` line")
