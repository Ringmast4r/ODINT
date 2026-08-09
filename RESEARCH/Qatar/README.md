# ODINT: Qatar — Passive Reconnaissance (March 2026)

## Summary
- **81 government, military, and critical infrastructure domains** surveyed
- **45 confirmed live** endpoints (55% reachable)
- **2 domains** missing DMARC (email spoofing risk)
- **46 passive findings** via Nuclei
- All data publicly accessible and independently reproducible

## Key Findings
| Category | Count | Risk |
|----------|-------|------|
| Live Hosts | 45/81 | Documented |
| Missing DMARC | 2 | High |
| Nuclei Findings | 46 | Info/Low |

## Methodology
Passive only. httpx + dig + openssl + nuclei (info/low). Rate-limited 5 req/s.

## Timeline
- Discovery: March 7, 2026
- Country #29 in the ODINT catalog
