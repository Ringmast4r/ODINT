# Guatemala Government Infrastructure — Passive Reconnaissance Report

## Date: 2026-02-28
## Targets: 20 government domains (.gob.gt)
## Live Hosts: 16

## Critical Findings

### phpinfo.php Exposed — Agriculture Ministry
- maga.gob.gt/info.php — PHP 7.4.33 (EOL), Apache 2.4.6/CentOS, OpenSSL 1.0.2k (EOL)

### PHP Error Logs Exposed — Constitutional Court
- cc.gob.gt/php_errors.log — Server errors publicly accessible

### DMARC Missing on Key Domains
- vicepresidencia.gob.gt, guatemala.gob.gt, mspas.gob.gt, congreso.gob.gt

### 14 Azure AD Tenant IDs — All Unique
Each ministry maintains separate Microsoft 365 tenants.

### Deprecated Software
- maga.gob.gt: Apache 2.4.6, PHP 7.4.33, OpenSSL 1.0.2k, Slider Rev 5.4.8
- mineduc.gob.gt: jQuery 1.4.2 (2010), Prototype.js, SWFObject (Flash era)

## Methodology
httpx, dig, openssl, nuclei (info/low only). All passive. Rate-limited.
