# El Salvador Government Infrastructure — Passive Reconnaissance Report
## Date: 2026-02-28 | Targets: 20 | Live Hosts: 14

## Critical Findings

### Severely Outdated Software
| Domain | Issue |
|--------|-------|
| seguridad.gob.sv | PHP 7.3.6 (EOL Dec 2021) — Ministry of Public Security |
| cultura.gob.sv | PHP 7.4.33 (EOL Nov 2022) — Ministry of Culture |
| mined.gob.sv | WordPress 5.4.12 (2021) — Education Ministry |
| gobernacion.gob.sv | WordPress 5.4.17 (2021) — Governance Ministry |

### 12 Azure AD Tenant IDs
All ministries use separate Microsoft 365 tenants.

### Tech Stack Overview
- WordPress dominates (10+ sites): 5.4.x through 6.9.1
- Cloudflare CDN on majority
- Drupal 9 on asamblea.gob.sv (Legislature)
- Google Cloud CDN on vivienda, mop, minec

### Hosting Diversity
Unlike Rwanda (centralized), El Salvador uses mixed hosting:
Google Cloud, Cloudflare, Apache/Ubuntu

## DMARC Status
- Multiple ministries missing DMARC
- gobernacion cookie without Secure/HttpOnly flags

## Methodology: httpx, dig, openssl, nuclei (info/low only). All passive.
