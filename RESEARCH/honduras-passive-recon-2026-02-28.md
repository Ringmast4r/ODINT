# Honduras Government Infrastructure — Passive Reconnaissance Report

## Date: 2026-02-28
## Campaign: ODINT Honduras — Passive Infrastructure Analysis

### Targets: 20 government domains (.gob.hn)
### Live Hosts: 9

## Key Findings

### 🔴 CRITICAL: phpinfo.php Exposed on Health Ministry
- **salud.gob.hn/phpinfo.php** — PHP 7.4.33 configuration exposed
- Reveals: server paths, loaded modules, environment variables, database configs
- PHP 7.4.33 is END OF LIFE (November 2022) — no security patches

### DMARC Policy Assessment
| Domain | DMARC | Status |
|--------|-------|--------|
| presidencia.gob.hn | p=quarantine | ⚠️ Not full reject |
| salud.gob.hn | p=reject | ✅ Protected |
| poderjudicial.gob.hn | p=quarantine | ⚠️ Not full reject |
| sedena.gob.hn | p=quarantine + p=reject | ✅ Protected |
| sedesol.gob.hn | Check needed | — |
| sag.gob.hn | Check needed | — |
| trabajo.gob.hn | Check needed | — |
| seguridad.gob.hn | Check needed | — |
| sefin.gob.hn | Check needed | — |

### Azure AD Tenant IDs (9 discovered)
| Domain | Tenant ID |
|--------|-----------|
| sefin.gob.hn | 73ec3725-b44b-4bf8-933f-7b7c1a76ad7d |
| seguridad.gob.hn | 83329f49-7193-41d4-b2f7-a1e8c16b93b0 |
| poderjudicial.gob.hn | 048343d2-c3fa-4031-a99a-f0203e014a69 |
| presidencia.gob.hn | 3649b9b2-b94c-4f20-b530-6b24130076bf |
| sedesol.gob.hn | 8277303b-82ce-4754-9ef6-81921eb3afb3 |
| salud.gob.hn | 5a3236f6-d93d-4cb8-a530-897a222f3a65 |
| sag.gob.hn | 05fa0eff-5f24-40ad-bed7-b37d9e3623b2 |
| sedena.gob.hn | eea11475-5913-4c91-bb6d-09b294447ee1 |
| trabajo.gob.hn | (check needed) |

### Technology Stacks
| Domain | Server | Key Technologies |
|--------|--------|-----------------|
| presidencia.gob.hn | Cloudflare | Cloudflare CDN |
| salud.gob.hn | Nginx 1.27.2 | Bluehost |
| poderjudicial.gob.hn | IIS 10.0 | SharePoint, ASP.NET 4.0, Windows Server |
| sedena.gob.hn | Cloudflare | Drupal 10, Google Analytics |
| sedesol.gob.hn | Apache 2.4.52 | WordPress 6.9.1, Divi, Ubuntu |
| sag.gob.hn | Apache | WordPress, Elementor 3.34, Complianz |
| trabajo.gob.hn | Apache 2.4.52 | WordPress 6.9.1, Elementor 3.35, Ubuntu |
| seguridad.gob.hn | Apache | WordPress 6.8.3, WooCommerce 10.0, Bootstrap |
| sefin.gob.hn | Apache | WordPress, Slider Revolution 6.5.25, PHP 7.4.33 |

### Notable: SharePoint on poderjudicial.gob.hn (Judiciary)
Honduras Judiciary runs Microsoft SharePoint on IIS/Windows Server — only Windows-based gov site found.

## Methodology
- httpx (rate-limit: 5/s, timeout: 20s)
- dig (DNS records, DMARC analysis)
- openssl (SSL certificate verification)
- nuclei (info/low severity passive templates only)

## Principles
✅ Passive only ✅ Public data ✅ Rate-limited ✅ Documented ✅ No exploitation
