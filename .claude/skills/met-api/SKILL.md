---
name: met-api
description: Use when calling api.met.no or reading fixtures/met_hamar.json: User-Agent, caching, response layout.
---
# MET Norway Locationforecast 2.0

- Terms: https://api.met.no/doc/TermsOfService
- Send `User-Agent: innlandet-demo/0.1 github.com/coma2441/innlandet-demo`. Never a personal e-mail.
- Respect the `Expires` header; on repeat calls send `If-Modified-Since` with the saved `Last-Modified`.
- Coordinates: at most 4 decimals (Hamar: lat=60.79, lon=11.07).
- Times in the response are UTC (`...Z`); show local time (Europe/Oslo) to people.
- Temperature: `properties.timeseries[].data.instant.details.air_temperature` (degrees C).
- Weather symbol: `properties.timeseries[].data.next_1_hours.summary.symbol_code` (may be missing).
