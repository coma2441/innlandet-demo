"""Acceptance check for tasks/001-probe.md. Exit 0 = PASS, anything else = FAIL."""
import json
from datetime import datetime

data = json.load(open("out/probe.json", encoding="utf-8"))
assert data["source_url"].startswith("https://api.met.no/"), "wrong source"
items = data["items"]
assert len(items) >= 24, f"expected >= 24 hourly items, got {len(items)}"
times = []
for it in items:
    assert it["title"].strip(), "empty title"
    times.append(datetime.fromisoformat(it["date"].replace("Z", "+00:00")))
    # domain-specific: a plausible temperature for Innlandet
    assert -50 <= it["air_temperature"] <= 45, f"implausible temperature {it['air_temperature']}"
assert times == sorted(times), "times not ascending"
print("PASS")
