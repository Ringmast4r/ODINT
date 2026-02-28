# Passive Government Infrastructure Reconnaissance Workflow

## Overview
End-to-end passive OSINT pipeline for government domain reconnaissance.
Designed for ODINT contributions — all techniques are non-intrusive.

## Pipeline
```
Target List → Subdomain Enum → HTTP Probe → DNS/SSL Analysis → Passive Vuln Scan → Report
```

## Step 1: Target Selection
Select government domains from ODINT's CYBER RECON TOUR directory.
```bash
cat "CYBER RECON TOUR/Caribbean/jamaican-websites.txt" | grep gov
```

## Step 2: Subdomain Enumeration
```bash
subfinder -d gov.jm -silent -timeout 30 -o subdomains_gov_jm.txt
```
Uses passive sources: certificate transparency logs, DNS aggregators, web archives.

## Step 3: HTTP Fingerprinting
```bash
cat all_targets.txt | httpx -silent \
    -status-code -title -tech-detect -server -content-length \
    -follow-redirects -timeout 15 -rate-limit 50
```

## Step 4: DNS & SSL Analysis
```bash
# DNS records
dig +short A <domain>
dig +short MX <domain>
dig +short NS <domain>
dig +short TXT <domain>
dig +short TXT _dmarc.<domain>

# SSL certificate
echo | openssl s_client -servername <domain> -connect <domain>:443 2>/dev/null | \
    openssl x509 -noout -subject -issuer -dates
```

## Step 5: Passive Nuclei Scan
```bash
nuclei -l live_hosts.txt \
    -severity info,low \
    -tags tech,ssl,dns,misconfig,exposure \
    -rate-limit 5 -timeout 15
```

## Step 6: Data Organization
Structure findings for ODINT repository format:
- `LEADS/` — new subdomains and domains discovered
- `RESEARCH/` — infrastructure analysis reports
- `METHODOLOGIES/` — workflow documentation (this file)

## Rate Limiting
- httpx: 50 req/s maximum
- nuclei: 5 req/s for government targets
- DNS queries: 0.5s delay between targets

## Legal & Ethical
- All targets are publicly accessible websites
- All techniques are passive — no exploitation
- All data is publicly available (DNS, HTTP headers, SSL certs)
- Research conducted for public interest
