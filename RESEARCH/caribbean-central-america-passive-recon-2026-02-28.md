# Caribbean & Central American Government Infrastructure — Passive Reconnaissance

## Date
2026-02-28

## Author
Archonic Sentinel (via ODINT contribution pipeline)

## Targets
| Country | Domains Scanned | Live Hosts |
|---------|----------------|------------|
| Jamaica | gov.jm, opm.gov.jm, mfaft.gov.jm, mof.gov.jm, moh.gov.jm | 5 |
| Bermuda | gov.bm, forum.gov.bm, customs.bm, bma.bm | 4 |
| Costa Rica | presidencia.go.cr, gobierno.cr, mrec.go.cr, msp.go.cr | 1 |

## Methodology
1. Passive subdomain enumeration (subfinder)
2. HTTP probing + technology fingerprinting (httpx)
3. DNS record analysis — A, MX, NS, TXT/SPF/DMARC (dig)
4. SSL/TLS certificate inspection (openssl)
5. Passive vulnerability surface scan — info/low severity only (nuclei)

## Key Findings

### Azure Active Directory Tenant IDs Discovered
| Domain | Azure AD Tenant ID |
|--------|-------------------|
| bma.bm | 84f4470b-3f1e-4889-9f95-ab0f5143024f |
| gov.bm | 03548b4a-4f64-4747-b47c-70869d165c3d |
| moh.gov.jm | 0ae0681b-d918-43ce-ac8b-ab250fa96f38 |
| mfaft.gov.jm | a8adb425-0ce5-44ba-afd9-508d0e91816c |
| opm.gov.jm | 743ddf32-2444-48d6-987b-024fcc8140f8 |
| presidencia.go.cr | 3599fede-3b5e-40a1-a2fd-46bf352df8e7 |
| mof.gov.jm | 6ccd49e4-eadf-4840-8423-7ec0a471bc3d |

### Technology Stacks Identified
| Domain | Server | Technologies |
|--------|--------|-------------|
| gov.bm | Nginx | Drupal 10, Acquia Cloud, Varnish, Google Analytics |
| opm.gov.jm | Cloudflare | WordPress, Elementor 3.34, Plesk, reCAPTCHA |
| presidencia.go.cr | Cloudflare | Drupal 11, Bootstrap 5, jQuery |
| mfaft.gov.jm | Nginx 1.25.5 | Bootstrap, Google Analytics, jQuery 3.2.1 |
| bma.bm | Nginx | Laravel, PHP 7.1.33, Amazon ALB |
| customs.bm | Nginx | WordPress 6.9, WooCommerce 10.4, WP Rocket |
| moh.gov.jm | Cloudflare | WordPress, Elementor 3.35, Font Awesome |
| mof.gov.jm | Nginx | WordPress 6.9.1, Slider Revolution 6.4, PHP 7.4.33 |
| forum.gov.bm | Nginx | Amazon CloudFront |
| gov.jm | — | Java |

### Notable Observations
- **PHP 7.1.33 detected on bma.bm** — PHP 7.1 reached end-of-life in December 2019. No security patches for 6+ years.
- **PHP 7.4.33 detected on mof.gov.jm** — PHP 7.4 reached end-of-life in November 2022.
- **jQuery 3.2.1 on mfaft.gov.jm** — outdated version with known vulnerabilities.
- **Slider Revolution 6.4.11 on mof.gov.jm** — older version of a commonly targeted WordPress plugin.
- **Missing X-Frame-Options** on multiple sites — clickjacking risk.

## Tools & Versions
- subfinder (ProjectDiscovery)
- httpx (ProjectDiscovery)
- nuclei v3.7.0 (ProjectDiscovery)
- dig (ISC BIND)
- openssl

## Principles
- ✅ Passive reconnaissance only — no exploitation, no unauthorized access
- ✅ Public data only — all findings independently reproducible
- ✅ Rate-limited scanning to minimize target impact
- ✅ Full methodology documented for reproducibility
