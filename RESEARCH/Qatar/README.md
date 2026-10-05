# ODINT: Qatar — Passive Reconnaissance (March 2026)

## Summary
- **81 government and critical infrastructure domains** surveyed
- **45 confirmed live** endpoints (56% reachable)
- **2 domains** missing DMARC (email spoofing risk)
- **46 Nuclei findings** (info/low severity)
- All data publicly accessible and independently reproducible

## Methodology
Passive only. httpx + dig + openssl + nuclei (info/low). Rate-limited 5 req/s. All public data.

## Files
- `httpx_results.txt` — HTTP fingerprinting (45 live hosts)
- `dns_results.txt` — DNS + DMARC/SPF audit
- `nuclei_results.txt` — 46 passive findings

## Timeline
- Discovery: March 7, 2026
- Country #29 in the ODINT catalog
