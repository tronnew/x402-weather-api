#!/usr/bin/env python3
"""
x402 Weather API Client — Chile & LatAm
EIP-402 compliant. Pay per call in USDC on Base L2.
"""
import requests, json, sys

RECIPIENT = "0x6dDCd5CC6f0614A291954daf2fF1B41DA44363DE"
PRICE = 50000  # 0.05 USDC in microcents
BASE_URL = "https://forex2026.mooo.com:5010"

def call_weather(lat, lon, payment_header=None):
    url = f"{BASE_URL}/weather"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Price": str(PRICE),
        "X-Recipient": RECIPIENT,
    }
    if payment_header:
        headers["X-Payment"] = payment_header
    r = requests.post(url, json={"lat": lat, "lon": lon}, headers=headers)
    return r

def main():
    lat, lon = float(sys.argv[1]) if len(sys.argv) > 1 else -33.4489,                float(sys.argv[2]) if len(sys.argv) > 2 else -70.6693
    r = call_weather(lat, lon)
    print(f"Status: {r.status_code}")
    if r.status_code == 402:
        print("Payment required:", r.headers.get("X-Price"), "wei")
    else:
        print(r.text)

if __name__ == "__main__":
    main()
