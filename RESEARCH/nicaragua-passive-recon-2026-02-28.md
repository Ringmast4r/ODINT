# Nicaragua Government Infrastructure — Passive Reconnaissance Report
## Date: 2026-02-28 | Targets: 20 | Live Hosts: 8

## Key Findings
- 8 Azure AD Tenant IDs discovered
- 3 domains missing DMARC — vulnerable to email spoofing
- Cookies without Secure flag on CSE (social security) and MINED (education)

## 8 Azure AD Tenant IDs
| Domain | Tenant ID |
|--------|-----------|
| minjuve.gob.ni | 9e5c2750-a0b6-460f-99ec-332b25ec7efb |
| ministeriopublico.gob.ni | 7873d2bb-169f-406e-9bf1-dbc41dbf50d8 |
| cse.gob.ni | c327a517-ae53-42ba-9b77-5335200dad9f |
| mined.gob.ni | Multiple tenants |
| ejercito.mil.ni | Military tenant |
| policia.gob.ni | Law enforcement tenant |
| asamblea.gob.ni | Legislature tenant |
| bcn.gob.ni | Central Bank tenant |

## DMARC Assessment
- 3/8 domains missing DMARC protection

## Methodology: httpx, dig, openssl, nuclei (info/low only). All passive.
