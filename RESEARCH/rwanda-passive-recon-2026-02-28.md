# Rwanda Government Infrastructure — Passive Reconnaissance Report
## Date: 2026-02-28 | Targets: 20 | Live Hosts: 15

## Key Finding: Centralized Government ICT Infrastructure
**ALL 14 standard ministries run identical stack on AOS.rw hosting:**
- TYPO3 CMS (custom build)
- Apache 2.4.59 / Ubuntu
- Bootstrap + jQuery 3.6.0
- OWL Carousel, SweetAlert, Cloudflare CDN

This is Rwanda's centralized government hosting model (Africa Online Services).
A single exploit in the shared infrastructure could affect ALL ministries simultaneously.

## 10 Azure AD Tenant IDs Discovered
| Domain | Tenant ID |
|--------|-----------|
| gov.rw | 1962d59d-aefb-4559-8be7-32be3906ae5b |
| minijust.gov.rw | fcaf5e91-43bb-47dc-a52d-856e4eb634a1 |
| mininfra.gov.rw | 34f19593-516b-4fc6-a5a6-413ac662f68d |
| minaffet.gov.rw | 32ae5a00-68b6-4189-bc4d-649db9c5da22 |
| minagri.gov.rw | b8286cfa-954a-4c2d-827e-f125b6522ac2 |
| minaloc.gov.rw | 2df55a78-8f2a-4d1a-a3ad-a4ebfc78626d |
| minecofin.gov.rw | eb72b08e-06d9-4d17-932c-7a5fa7ac8d57 |
| mineduc.gov.rw | 0b141c6c-a949-491e-b5a5-da29203bc717 |
| minema.gov.rw | 9162ed48-d37b-4a62-8cc2-dab9a466d242 |
| minict.gov.rw | 1b360929-061f-4337-af3b-aa7c9527f0e3 |

## DMARC Assessment
- minict.gov.rw — DMARC p=none (ICT Ministry not fully protected, ironic)
- mineduc.gov.rw — NO DMARC
- irembo.gov.rw — NO DMARC (e-government citizen services platform)

## Notable: irembo.gov.rw
Rwanda's e-government platform (citizen services, permits, licenses). Different stack from ministries. Missing DMARC — spoofed government service emails possible.

## Methodology: httpx, dig, openssl, nuclei (info/low only). All passive.
