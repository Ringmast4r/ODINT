# ODINT: Kuwait — Passive Reconnaissance (March 2026)

## Summary
- **80 government, military, and infrastructure domains** surveyed
- **43 confirmed live** endpoints
- **3 domains** missing DMARC (email spoofing risk)
- **26 nuclei findings** (info/low severity)
- All data publicly accessible and independently reproducible

## Methodology
Passive only. httpx + dig + openssl + nuclei (info/low). Rate-limited 5 req/s. All public data.

## Files
- httpx_results.txt — HTTP fingerprinting
- dns_results.txt — DNS + DMARC/SPF audit
- nuclei_results.txt — Passive findings

## Timeline
- Discovery: March 8, 2026
- Country #30 in the ODINT catalog
