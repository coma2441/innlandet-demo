"""Task 001: fetch the MET Norway forecast for Hamar and write out/probe.json.

Usage: python3 harness/probe.py [--offline]
"""
import argparse
import json
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parent.parent
URL = "https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=60.79&lon=11.07"
USER_AGENT = "innlandet-demo/0.1 github.com/coma2441/innlandet-demo"
FIXTURE = ROOT / "fixtures" / "met_hamar.json"
OUT = ROOT / "out" / "probe.json"
HOURS = 24
LOCAL_TZ = ZoneInfo("Europe/Oslo")


def fetch():
    """Call the API, save the raw response to the fixture, return parsed JSON."""
    req = urllib.request.Request(URL, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            body = resp.read()
    except (urllib.error.URLError, TimeoutError) as e:
        sys.exit(f"probe: could not fetch {URL}: {e}\nTry again with --offline.")
    FIXTURE.parent.mkdir(parents=True, exist_ok=True)
    FIXTURE.write_bytes(body)
    return json.loads(body.decode("utf-8"))


def load_fixture():
    if not FIXTURE.exists():
        sys.exit(f"probe: no fixture at {FIXTURE.relative_to(ROOT)}; run once without --offline.")
    return json.loads(FIXTURE.read_text(encoding="utf-8"))


def to_items(raw):
    items = []
    for entry in raw["properties"]["timeseries"][:HOURS]:
        temp = entry["data"]["instant"]["details"]["air_temperature"]
        when = datetime.fromisoformat(entry["time"].replace("Z", "+00:00"))
        title = f"Hamar {when.astimezone(LOCAL_TZ):%H:%M}: {temp} °C"
        symbol = entry["data"].get("next_1_hours", {}).get("summary", {}).get("symbol_code")
        if symbol:
            title += f", {symbol}"
        items.append({"title": title, "date": entry["time"], "air_temperature": temp})
    return sorted(items, key=lambda it: it["date"])


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--offline", action="store_true", help=f"read {FIXTURE.relative_to(ROOT)} instead of calling the API")
    args = parser.parse_args()

    raw = load_fixture() if args.offline else fetch()
    result = {
        "source_url": URL,
        "fetched_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "offline": args.offline,
        "items": to_items(raw),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    mode = "offline" if args.offline else "live"
    print(f"wrote {len(result['items'])} items to {OUT.relative_to(ROOT)} ({mode})")


if __name__ == "__main__":
    main()
