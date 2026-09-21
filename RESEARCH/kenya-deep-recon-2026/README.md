# Kenya — Deep Passive Infrastructure Assessment (2026)

## Executive Summary

Comprehensive passive reconnaissance of Kenya government digital infrastructure (`ke`).
This assessment covers subdomain enumeration, technology detection, SSL/TLS analysis,
email security posture, security headers, network topology mapping, and historical URL analysis.

**🎬 Video Documentation:** [https://archive.org/details/odint-kenya-passive-recon-2026](https://archive.org/details/odint-kenya-passive-recon-2026)

## Methodology

| Phase | Tool | Purpose | Rate Limit |
|-------|------|---------|------------|
| 1 | Subfinder + Amass | Multi-source subdomain enumeration | 5 req/s |
| 2 | httpx (enriched) | Live hosts + tech stack + CDN/WAF detection | 5 req/s |
| 3 | WHOIS | Domain registration + registrar analysis | Single query |
| 4 | OpenSSL | SSL/TLS certificate chain analysis | 1 cert/s |
| 5 | dig (TXT) | Email security: SPF, DMARC, DKIM | Passive |
| 6 | curl | Security headers analysis (HSTS, CSP, X-Frame) | 1 req/s |
| 7 | WHOIS (Cymru) | ASN + network topology mapping | Passive |
| 8 | dig (multi-type) | DNS deep analysis (A, AAAA, MX, NS, TXT, SOA) | Passive |
| 9 | GAU | Historical URL archive scraping | Passive |

**All reconnaissance is passive. No active exploitation. No unauthorized access.**

## Key Findings

### Digital Footprint
- **Subdomains discovered:** 1182
- **Live hosts:** 458
- **SSL certificates analyzed:** 20
- **Unique ASN mappings:** 22
- **DNS records:** 25
- **Historical URLs:** 10

### Email Security Posture
| Record | Status |
|--------|--------|
| SPF | Not Found |
| DMARC | Not Found |
| DKIM (default) | Check `email_security.txt` |

### Technology Stack (Top Detections)
```
    247 [[32m200[0m]
    130 [LiteSpeed]
    104 [Apache]
     75 [[33m301[0m,[32m200[0m]
     64 [nginx]
     39 [cloudflare]
     31 [[36mWebmail Login[0m]
     31 [[35mApache HTTP Server[0m]
     30 [[33m302[0m,[32m200[0m]
     29 [[36mcPanel Login[0m]
     29 [[35mHTTP/3,LiteSpeed[0m]
     28 [[31m403[0m]
     27 [[31m401[0m]
     23 [[35mNginx[0m]
     23 [[35m36[0m]
```

### Network Topology (Top ASNs)
```
      5  KoTDA, KE
      2  KENET-AS, KE
      2  Error: no ASN or IP match on line 1.
      1  WIX_COM, IL
      1  UNIFIEDLAYER-AS-1 - Unified Layer, US
```

## Files

| File | Description | Lines |
|------|-------------|-------|
| `subdomains.txt` | All discovered subdomains | 1182 |
| `httpx_enriched.txt` | Live hosts with tech stack, ASN, CDN, titles | 458 |
| `ssl_results.txt` | SSL/TLS certificate details | 1976 |
| `email_security.txt` | SPF, DMARC, DKIM records | 5 |
| `security_headers.txt` | HTTP security headers per host | 23 |
| `network_topology.txt` | Host → IP mappings | 31 |
| `asn_mapping.txt` | IP → ASN organization mappings | 22 |
| `whois_summary.txt` | Domain registration summary | 17 |
| `dns_results.txt` | Full DNS records (A, AAAA, MX, NS, TXT, SOA) | 25 |
| `gau_results.txt` | Historical archived URLs | 10 |

## Compliance Notes

- All data obtained through passive, publicly available sources
- Rate-limited to prevent service impact
- No login attempts, no active scanning, no exploitation
- Findings intended for defensive security improvement
- Contributed to [ODINT](https://github.com/Ringmast4r/ODINT) for the white-hat community

## References

- [ODINT Project](https://github.com/Ringmast4r/ODINT)
- [OptinAmpOut](https://optinampout.com)
