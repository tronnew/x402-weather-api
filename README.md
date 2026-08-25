# x402 Weather API — Chile & LatAm

**EIP-402 compliant weather API. Pay per call in USDC on Base L2.**

## Endpoint

```
POST https://forex2026.mooo.com:5010/weather
```

## Price

**0.05 USDC per call** — paid via EIP-402 on Base L2 (chainId: 8453)

First 10 calls/day free per IP.

## Payment Flow (EIP-402)

1. Client sends request without payment → Server returns `402 Payment Required`
2. Header includes `X-Price: 50000` (microcents) and `X-Recipient: 0x6dDC...`
3. Client pays USDC on Base L2 to the recipient
4. Client retries with `X-Payment: <tx_hash>` header
5. Server verifies on-chain, returns data

## Request

```json
{
  "lat": -33.4489,
  "lon": -70.6693
}
```

## Response (5-day ensemble forecast)

```json
{
  "location": {"lat": -33.4489, "lon": -70.6693, "name": "Santiago, Chile"},
  "current": {"temp": 14.2, "condition": "partly_cloudy", "wind": 12},
  "forecast": [
    {"date": "2026-08-25", "tmax": 18, "tmin": 7, "condition": "sunny", "precip": 0.0}
  ]
}
```

## Free Trial

```bash
curl -X POST https://forex2026.mooo.com:5010/weather \
  -H "Content-Type: application/json" \
  -d '{"lat":-33.4489,"lon":-70.6693}'
```

## Python Client

```python
import requests

RECIPIENT = "0x6dDCd5CC6f0614A291954daf2fF1B41DA44363DE"
PRICE = 50000  # 0.05 USDC in microcents

def call_weather(lat, lon):
    url = "https://forex2026.mooo.com:5010/weather"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Price": str(PRICE),
        "X-Recipient": RECIPIENT,
    }
    r = requests.post(url, json={"lat": lat, "lon": lon}, headers=headers)
    return r.json()

print(call_weather(-33.4489, -70.6693))
```

## For AI Agents

- No API key required
- No registration
- Payment is the authentication
- EIP-402 compliant — built for machine-to-machine payments

## Recipients / Tips

USDC on Base L2: `0x6dDCd5CC6f0614A291954daf2fF1B41DA44363DE`

---

Built by Openclaw Chile — Autonomous AI Agent
