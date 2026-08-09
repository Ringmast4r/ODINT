# ODINT: Israel — Passive Reconnaissance (March 2026)

## Summary
- **35 government, military, and intelligence domains** surveyed
- **24 confirmed live** endpoints
- **1 domain** missing DMARC (email spoofing risk)
- **Heavy Cloudflare deployment** across government ministries
- All data publicly accessible and independently reproducible

## Key Findings
| Category | Count | Risk |
|----------|-------|------|
| Live Hosts | 24/35 | Documented |
| Missing DMARC | 1/12 | High |
| Tech Stack Exposed | 24 | Low |
| CDN/WAF Detected | 18 | Info |

## Technology Stack Detected
- **Cloudflare** (majority of .gov.il): Bot Management, WAF
- **AWS CloudFront**: Israel Electric Corp (iec.co.il)
- **Sucuri/Cloudproxy**: President's Office
- **Microsoft ASP.NET + SharePoint**: Bank of Israel, CBS
- **Nginx/OpenResty**: Knesset, Haifa Municipality
- **Imperva**: Tel Aviv Stock Exchange

## Notable Observations
- **Mossad (mossad.gov.il)**: 200 OK, Bootstrap framework, HSTS enabled, no CDN
- **Shabak (shabak.gov.il)**: 403 behind Cloudflare Bot Management
- **IDF (idf.il)**: Timeout — not publicly accessible
- **Bank of Israel (boi.org.il)**: Microsoft Power BI exposed in headers

## Methodology
- Passive reconnaissance only — no active exploitation
- Tools: httpx, dig, openssl, nuclei (info/low severity only)
- Rate-limited: 5 requests/second maximum
- All data from public DNS, HTTP headers, and certificate transparency

## Files
- `httpx_results.txt` — Full HTTP fingerprinting results
- `dns_results.txt` — DNS records and DMARC/SPF audit
- `nuclei_results.txt` — Nuclei passive scan findings

## Video
Archive.org: (pending upload)

## Timeline
- Discovery: March 7, 2026
- Country #28 in the ODINT catalog
