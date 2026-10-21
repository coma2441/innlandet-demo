"""Acceptance check for tasks/003-summary.md. Exit 0 = PASS, anything else = FAIL."""
import json
import re

probe = json.load(open("out/probe.json", encoding="utf-8"))
temps = [it["air_temperature"] for it in probe["items"][:24]]
text = open("out/summary.md", encoding="utf-8").read()

words = len(text.split())
assert 20 <= words <= 80, f"summary has {words} words, expected 20-80"
assert "Hamar" in text, "summary does not mention Hamar"
# every temperature in the summary must occur in the source (traceability)
found = [float(x.replace("−", "-")) for x in re.findall(r"([-−]?\d+(?:\.\d+)?)\s*(?:°\s*C|°|degrees)", text)]
assert found, "no temperatures in the summary"
for t in found:
    assert t in temps, f"temperature {t} is not in out/probe.json"
# domain-specific: a commuter needs the range
assert min(temps) in found, f"lowest temperature {min(temps)} missing"
assert max(temps) in found, f"highest temperature {max(temps)} missing"
print("PASS")
