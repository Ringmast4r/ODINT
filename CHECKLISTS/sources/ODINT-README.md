# ODINT Mission Objectives

**Observatory for Digital Infrastructure and Network Transparency**

---

## Mission Statement

ODINT conducts **OSINT-ONLY** security audits of government digital infrastructure for the purpose of transparency, accountability, and public record.

**THIS IS NOT HACKING. THIS IS NOT EXPLOITATION. THIS IS DOCUMENTATION.**

We are the "Wayback Machine" for government security posture, with the defiance of "The Pirate Bay" and the transparency mission of "WikiLeaks" — systematically documenting what is publicly accessible, exposed, or misconfigured so that:

1. Citizens know what data their governments are exposing
2. Journalists have evidence for accountability reporting
3. Human rights organizations can document abuses
4. History has a record of what authoritarian regimes tried to hide
5. Democratic accountability is strengthened through transparency

### Methodology: OSINT (Open Source Intelligence) ONLY

- Passive reconnaissance
- Publicly accessible data
- No exploitation or intrusion
- No unauthorized access
- No active attacks
- Legal in all jurisdictions

**WE DOCUMENT. WE ARCHIVE. WE HOLD POWER ACCOUNTABLE.**

---

## Project Information

| Field | Value |
|-------|-------|
| Target Country/Region | _(per project)_ |
| Project Codename | _(per project)_ |
| Start Date | _(per project)_ |
| Last Updated | _(per project)_ |
| Status | `[ ] Enumeration` `[ ] Active Collection` `[ ] Analysis` `[ ] Complete` |

---

## Table of Contents

- [Section 0: File Organization Rules](#section-0-file-organization-rules)
- [Section 0.3: Database Schema](#section-03-database-schema)
- [Section 0.4: HTTP & Edge-Level Documentation](#section-04-http--edge-level-documentation)
- [Section 0.5: Recommended Tools Reference](#section-05-recommended-tools-reference)
- [Section 0.6: Additional OSINT Sources](#section-06-additional-osint-sources)
- [Section 1: Target Source Categories](#section-1-target-source-categories)
- [Section 2: Collection Folders](#section-2-collection-folders)
- [Section 3: Full Technology Stack Enumeration](#section-3-full-technology-stack-enumeration)
- [Section 4: Path & Directory Enumeration](#section-4-path--directory-enumeration)
- [Section 5: API Enumeration & Hunting](#section-5-api-enumeration--hunting)
- [Section 6: Critical Data Hunting](#section-6-critical-data-hunting)
- [Section 7: Target Priority Order](#section-7-target-priority-order)
- [Section 8: Technical Audit Checklist](#section-8-technical-audit-checklist)
- [Section 10: Threat Classification](#section-10-threat-classification)
- [Section 11: Methodology Checklist](#section-11-methodology-checklist)
- [Section 12: Operational Protocols](#section-12-operational-protocols)
- [Section 13: Tracking & Metrics](#section-13-tracking--metrics)
- [Sections 14–19: Logs & Templates](#sections-1419-logs--templates)

---

## Section 0: File Organization Rules

> **ALL FILES MUST BE ORGANIZED INTO SUBFOLDERS — NO EXCEPTIONS**

### Rule 1: Every Download Goes in Its Designated Subfolder

| Data Type | Folder |
|-----------|--------|
| Hashes | `/hashes/` |
| Usernames | `/usernames/` |
| Emails | `/personnel/` |
| GPS coords | `/gps-coords/` |
| API responses | `/apis/` |
| Documents | `/documents/` |
| Photos | `/photos/` |
| Videos | `/videos/` |

### Rule 2: Naming Convention

```
[domain]_[type]_[date].[ext]
```

**Examples:**
- `presidency.gov.xx_users_2026-01-20.json`
- `military.gov.xx_api-response_2026-01-20.json`
- `ministry.gov.xx_gravatar-hashes_2026-01-20.txt`

### Rule 3: Always Maintain Chain of Custody

Every file should have:
- Source URL documented
- Collection timestamp
- SHA256 hash of original file
- Collector identification

### Rule 4: Compartmentalization Purpose

This organization allows us to:
- Know exactly what we **HAVE** collected
- Know exactly what we are **MISSING**
- Track progress by folder completeness
- Generate reports per data type
- Share specific data with partners
- Maintain evidence integrity

### Rule 5: Folder Checklist Per Target

For each domain audited, these folders should be populated:

| Folder | Contents |
|--------|----------|
| `/apis/` | All API responses |
| `/archives/` | Wayback/historical snapshots |
| `/backups/` | Any exposed backups found |
| `/configs/` | Configuration files |
| `/credentials/` | Exposed keys/tokens (DO NOT USE) |
| `/documents/` | PDFs, Office docs |
| `/domains/` | Domain/subdomain lists |
| `/geolocation/` | IP geolocation data |
| `/gps-coords/` | GPS/EXIF coordinates |
| `/hashes/` | All extracted hashes |
| `/infrastructure/` | Hosting/CDN/network info |
| `/ip-ranges/` | IP addresses, netblocks |
| `/keys/` | SSH/PGP keys found |
| `/logs/` | Exposed log files |
| `/metadata/` | Document/image metadata |
| `/notes/` | Research notes |
| `/personnel/` | Emails, names, org charts |
| `/photos/` | Images with EXIF |
| `/raw/` | Unprocessed bulk data |
| `/reports/` | Analysis writeups |
| `/source-code/` | Exposed source files |
| `/ssl-certificates/` | Cert data |
| `/subdomains/` | Subdomain enumeration |
| `/tech-stacks/` | Technology fingerprints |
| `/usernames/` | All usernames found |
| `/videos/` | Video files |
| `/filenames/` | Raw filename patterns & enumeration |

### Rule 6: sourcelist.txt is Mandatory

Every project folder **MUST** contain a `sourcelist.txt` that:
- Lists ALL target domains
- Shows scan status for each
- Documents findings per domain
- Tracks what's been audited vs pending

### Rule 7: Nothing Goes in Root Folder

The root project folder should ONLY contain:
- `sourcelist.txt`
- This mission objectives file (if copied)
- Subfolders listed above

**NO loose files. NO downloads in root. EVER.**

### Standard Folder Structure

```
/[COUNTRY-NAME]/
├── [COUNTRY-NAME].db           # SQLite database
├── sourcelist.txt              # Master list of all targets + status
├── MISSION_OBJECTIVES.txt      # Copy of this template (optional)
│
├── /apis/                      # API responses, schemas, documentation
│   ├── /[domain1.gov.xx]/
│   └── /[domain2.gov.xx]/
│
├── /archives/                  # Wayback snapshots, historical data
├── /backups/                   # Exposed .bak, .sql, .zip files
├── /configs/                   # .env, config files, settings
├── /credentials/               # API keys, tokens (DOCUMENT ONLY)
├── /critical-findings/         # HIGH SEVERITY - immediate action items
│
├── /documents/                 # ALL document types, organized by domain
│   ├── /[domain1.gov.xx]/
│   │   ├── /pdf/
│   │   ├── /doc/
│   │   ├── /xls/
│   │   ├── /ppt/
│   │   ├── /csv/
│   │   ├── /txt/
│   │   └── /other/
│   └── /[domain2.gov.xx]/
│
├── /domains/                   # Domain lists, WHOIS data
├── /downloads/                 # Staging area for bulk downloads
│
├── /data-files/                # Structured data files by domain
│   ├── /[domain1.gov.xx]/
│   │   ├── /json/
│   │   ├── /xml/
│   │   ├── /csv/
│   │   ├── /sql/
│   │   └── /other/
│   └── ...
│
├── /geolocation/               # IP geolocation, server locations
├── /gps-coords/                # EXIF GPS, facility coordinates
├── /hashes/                    # MD5, SHA, Gravatar, password hashes
│
├── /html/                      # Raw HTML pages archived
│   └── /[domain1.gov.xx]/
│
├── /infrastructure/            # Hosting, CDN, network architecture
├── /ip-ranges/                 # IPs, netblocks, ASN data
├── /keys/                      # SSH, PGP, encryption keys
├── /logs/                      # Exposed log files
├── /metadata/                  # Document/image metadata extracts
├── /notes/                     # Research notes, observations
├── /personnel/                 # Emails, names, org charts, contacts
│
├── /photos/                    # ALL images, organized by domain
│   └── /[domain1.gov.xx]/
│       ├── /jpg/
│       ├── /png/
│       ├── /gif/
│       ├── /tiff/
│       ├── /webp/
│       ├── /svg/
│       └── /raw/
│
├── /videos/                    # ALL video files, organized by domain
│   └── /[domain1.gov.xx]/
│       ├── /mp4/
│       ├── /mov/
│       ├── /avi/
│       ├── /webm/
│       └── /other/
│
├── /audio/                     # Audio files
│   └── /[domain1.gov.xx]/
│       ├── /mp3/
│       ├── /wav/
│       └── /other/
│
├── /raw/                       # Unprocessed bulk data
├── /reports/                   # Analysis reports, writeups
├── /scripts/                   # Collection/analysis scripts used
│
├── /source-code/               # Exposed source files by domain
│   └── /[domain1.gov.xx]/
│       ├── /js/
│       ├── /css/
│       ├── /php/
│       ├── /git/
│       └── /other/
│
├── /sources/                   # Source attribution, chain of custody
├── /ssl-certificates/          # Certificate data, CT logs
├── /subdomains/                # Subdomain enumeration results
├── /tech-stacks/               # Technology fingerprints
├── /usernames/                 # Enumerated usernames, accounts
├── /filenames/                 # Raw filename enumeration & patterns
│
├── /social-media/              # Social media account archives
│   ├── /twitter/
│   ├── /facebook/
│   ├── /instagram/
│   ├── /youtube/
│   ├── /telegram/
│   └── /linkedin/
│
├── /mobile-apps/               # APK/IPA files and analysis
│   ├── /apk/
│   ├── /decompiled/
│   └── /extracted-data/
│
├── /code-repos/                # GitHub/GitLab repository archives
│   └── /[org-name]/
│
├── /github/                    # GitHub OSINT data
│   ├── /users/
│   ├── /gists/
│   ├── /organizations/
│   ├── /commits/
│   ├── /issues/
│   └── /actions/
│
├── /dns-records/               # Complete DNS enumeration
│   └── /[domain1.gov.xx]/
│
├── /cloud-storage/             # Exposed S3/Azure/GCS findings
├── /breach-data/               # Data from breach databases
├── /shodan-censys/             # Internet scan data
│
├── /wayback/                   # Wayback Machine archives
│   └── /[domain1.gov.xx]/
│
├── /google-dorks/              # Google dorking results
├── /geospatial/                # Maps, satellite imagery, coordinates
├── /network/                   # BGP, ASN, network topology
│
└── /http-data/                 # HTTP-level data per domain
    └── /[domain1.gov.xx]/
        ├── response_headers_[date].txt
        ├── ssl_certificate_[date].txt
        ├── ssl_chain_[date].pem
        ├── cookies_[date].txt
        ├── meta_tags_[date].txt
        ├── scripts_inventory_[date].txt
        ├── third_party_resources_[date].txt
        ├── /error_pages/
        └── /screenshots/
```

### Rule 8: Documentation is the Mission

We are not hackers. We are **ARCHIVISTS** and **AUDITORS**.

Our job is to:
- **DOCUMENT** what governments expose publicly
- **ARCHIVE** evidence before it disappears
- **ORGANIZE** findings for journalists & researchers
- **PRESERVE** chain of custody for legal proceedings
- **CREATE** accountability through transparency

Every file we collect is **EVIDENCE** for:
- Future investigations
- Journalism
- Human rights documentation
- Historical record
- Democratic accountability

### Rule 9: What We Do vs What We Don't Do

| WE DO | WE DON'T |
|-------|----------|
| Access public URLs | Bypass authentication |
| Read exposed APIs | Brute force passwords |
| Download public documents | Exploit vulnerabilities |
| Extract metadata | Inject code or payloads |
| Enumerate subdomains (passive) | Perform active scanning |
| Check robots.txt/sitemap | Ignore access restrictions |
| Archive public pages | Access "private" areas |
| Document misconfigurations | Take advantage of them |
| Record what we find | Modify or delete anything |
| Share with journalists | Sell data or extort |

> If a door is **OPEN**, we document that it's open. We do **NOT** walk through it.

### Rule 10: Raw File Preservation

ALL files must be downloaded in their **ORIGINAL FORMAT**:

**Photos:**
- Download original JPG/PNG/TIFF — NOT thumbnails
- NEVER screenshot instead of download
- NEVER convert formats (preserves EXIF)
- NEVER resize or compress
- EXIF data contains: GPS, camera, date, software, author

**Documents:**
- Download original PDF/DOC/XLS — NOT previews
- Metadata contains: author, org, software, edit history

**Videos:**
- Download original MP4/MOV/AVI
- Metadata contains: GPS, camera, timestamps

### Rule 11: Filename Enumeration & Analysis

Raw filenames are **INTELLIGENCE**. Always capture them.

**What filenames reveal:**
- Naming conventions (how they organize)
- Date formats (YYYY-MM-DD vs DD-MM-YYYY)
- Project codes / internal references
- Personnel names / initials
- Department abbreviations
- Version numbering schemes

**Filename patterns to look for:**
| Pattern | Intelligence |
|---------|-------------|
| `IMG_20260120_143052.jpg` | Date/time stamps |
| `informe_confidencial_v3.pdf` | Version numbers, classification |
| `juan_garcia_cv.doc` | Personnel names |
| `MIN-DEF-2026-0042.pdf` | Internal reference numbers |
| `backup_db_20260101.sql` | Backup schedules |
| `DSC_0001.JPG` | Camera defaults (unedited) |

### Rule 12: Domain-Based Subfolder Organization

Every file type folder **MUST** have subfolders per domain/organization:

```
CORRECT:
/photos/presidency.gov.xx/jpg/foto_oficial_2026.jpg
/documents/military.gov.xx/pdf/informe_anual.pdf

INCORRECT:
/photos/foto_oficial_2026.jpg          # NO! Missing domain folder
/documents/informe_anual.pdf           # NO! Missing domain folder
```

### Rule 13: Download Everything — All File Types

If it's on the server and publicly accessible, **DOWNLOAD IT**.

<details>
<summary><strong>Complete File Type Reference</strong></summary>

**Documents:** `.pdf` `.doc` `.docx` `.xls` `.xlsx` `.ppt` `.pptx` `.odt` `.ods` `.odp` `.rtf` `.txt`

**Data Files:** `.json` `.xml` `.csv` `.tsv` `.sql` `.db` `.sqlite` `.yaml` `.toml` `.ini`

**Images:** `.jpg` `.jpeg` `.png` `.gif` `.tiff` `.tif` `.bmp` `.webp` `.svg` `.ico` `.raw` `.cr2` `.nef`

**Video:** `.mp4` `.mov` `.avi` `.wmv` `.webm` `.mkv` `.flv` `.m4v`

**Audio:** `.mp3` `.wav` `.ogg` `.m4a` `.flac` `.wma`

**Archives:** `.zip` `.rar` `.7z` `.tar` `.gz` `.tar.gz` `.bz2`

**Web/Code:** `.html` `.htm` `.css` `.js` `.php` `.asp` `.jsp` `.py`

**Other:** `.log` `.bak` `.old` `.tmp` `.swp` `.env` `.config` `.key` `.pem` `.crt` `.p12`

</details>

### Rule 14: Completeness Checklist

Before marking a domain as "SCANNED", verify ALL of the following:

<details>
<summary><strong>Pre-Scan Checklist</strong></summary>

- [ ] Domain resolves (DNS check)
- [ ] Site is accessible (HTTP 200)
- [ ] robots.txt downloaded & analyzed
- [ ] sitemap.xml downloaded & parsed
- [ ] .well-known/ directory checked

</details>

<details>
<summary><strong>Enumeration Checklist</strong></summary>

- [ ] All subdomains discovered (CT logs, passive DNS)
- [ ] All IP addresses resolved
- [ ] WHOIS/RDAP data captured
- [ ] SSL certificate downloaded
- [ ] CT log history checked
- [ ] Wayback Machine snapshots reviewed

</details>

<details>
<summary><strong>Technology Checklist</strong></summary>

- [ ] CMS identified (WordPress, Drupal, etc.)
- [ ] Server headers captured
- [ ] Framework/language identified
- [ ] All plugins/themes enumerated
- [ ] Version numbers documented
- [ ] Third-party services identified

</details>

<details>
<summary><strong>API Checklist</strong></summary>

- [ ] /wp-json/ checked (if WordPress)
- [ ] /api/ paths enumerated
- [ ] /graphql endpoint checked
- [ ] Swagger/OpenAPI docs searched
- [ ] All API namespaces discovered
- [ ] API responses archived

</details>

<details>
<summary><strong>User/Identity Checklist</strong></summary>

- [ ] User enumeration attempted
- [ ] All usernames extracted
- [ ] All emails extracted
- [ ] Gravatar hashes generated
- [ ] Personnel names documented

</details>

<details>
<summary><strong>File Discovery Checklist</strong></summary>

- [ ] All PDFs downloaded
- [ ] All Office docs downloaded
- [ ] All images downloaded (ORIGINAL, not thumbnails)
- [ ] All videos downloaded
- [ ] All data files (JSON, CSV, XML) downloaded
- [ ] Backup files searched (.bak, .old, .sql)
- [ ] Config files searched (.env, .config)
- [ ] Log files searched
- [ ] Source code exposure checked (.git, etc.)

</details>

<details>
<summary><strong>Metadata Checklist</strong></summary>

- [ ] EXIF extracted from all images
- [ ] Metadata extracted from all documents
- [ ] GPS coordinates catalogued
- [ ] Author information catalogued
- [ ] Software versions catalogued
- [ ] Creation dates catalogued

</details>

<details>
<summary><strong>Path Enumeration Checklist</strong></summary>

- [ ] /admin/ paths checked
- [ ] /backup/ paths checked
- [ ] /uploads/ directory checked
- [ ] /wp-content/uploads/ checked (if WP)
- [ ] /data/ paths checked
- [ ] /files/ paths checked
- [ ] /private/ paths checked
- [ ] /temp/ paths checked
- [ ] Debug endpoints checked

</details>

<details>
<summary><strong>Hash Checklist</strong></summary>

- [ ] All MD5 hashes extracted
- [ ] All SHA hashes extracted
- [ ] All Gravatar hashes extracted
- [ ] Hash types identified
- [ ] Hashes cross-referenced

</details>

<details>
<summary><strong>Documentation Checklist</strong></summary>

- [ ] Source URLs documented for every file
- [ ] Timestamps recorded for all collection
- [ ] SHA256 hashes of originals computed
- [ ] Chain of custody maintained
- [ ] Notes added for anomalies

</details>

<details>
<summary><strong>Final Verification</strong></summary>

- [ ] All folders have content (or marked N/A)
- [ ] No files in root folder
- [ ] sourcelist.txt updated with status
- [ ] Critical findings flagged
- [ ] Nothing left to collect

</details>

### Rule 15: Common Oversights

<details>
<summary><strong>Often Forgotten Files</strong></summary>

- [ ] `favicon.ico` (can contain metadata)
- [ ] `apple-touch-icon.png`
- [ ] `manifest.json` / `site.webmanifest`
- [ ] `browserconfig.xml`
- [ ] `crossdomain.xml`
- [ ] `clientaccesspolicy.xml`
- [ ] `security.txt`
- [ ] `humans.txt`
- [ ] `ads.txt`
- [ ] License / README / CHANGELOG / VERSION files
- [ ] Backup index files (`index.html.bak`, `index.php.old`)

</details>

<details>
<summary><strong>Often Overlooked Data Sources</strong></summary>

- [ ] HTML comments (view-source)
- [ ] JavaScript files (hardcoded URLs, API keys)
- [ ] CSS files (background image URLs)
- [ ] Source maps (`.js.map`, `.css.map`)
- [ ] Error pages (404, 500 — often leak info)
- [ ] Login / password reset / registration pages
- [ ] Contact forms (may reveal backend)
- [ ] Search functionality (may expose data)
- [ ] RSS/Atom feeds
- [ ] Mobile versions (`m.domain.com`)
- [ ] Staging/dev subdomains

</details>

<details>
<summary><strong>Hidden in Plain Sight</strong></summary>

- [ ] WordPress `readme.html` (version disclosure)
- [ ] Drupal `CHANGELOG.txt`
- [ ] Server-status pages (Apache)
- [ ] phpinfo() pages
- [ ] Debug/trace endpoints
- [ ] Health check endpoints (`/health`, `/status`)
- [ ] Metrics endpoints (`/metrics`, `/prometheus`)

</details>

<details>
<summary><strong>Infrastructure Leaks</strong></summary>

- [ ] HTTP headers (`Server`, `X-Powered-By`)
- [ ] Cookie names (can reveal framework)
- [ ] Session ID formats
- [ ] Error message formats
- [ ] Stack traces (if exposed)
- [ ] Default credentials pages
- [ ] Installation/setup pages left accessible

</details>

---

## Section 0.3: Database Schema

Each country/region project should have its own SQLite database file:

```
/[COUNTRY-NAME]/[COUNTRY-NAME].db
```

This database stores all collected data with proper relationships and enables:
- Querying across all collected data
- Cross-referencing hashes, emails, usernames
- Tracking collection progress
- Generating reports
- Finding correlations

### Database Tables (28 Tables)

| Category | Tables |
|----------|--------|
| **Core** | `countries`, `domains`, `subdomains` |
| **Technology & Infrastructure** | `tech_stacks`, `http_headers`, `ssl_certificates`, `dns_records`, `cookies` |
| **WordPress Specific** | `wordpress_sites`, `wordpress_users` |
| **Hashes** | `hashes`, `hash_correlations` |
| **Personnel & Identity** | `personnel`, `usernames`, `emails` |
| **Files & Documents** | `files`, `file_metadata`, `filenames` |
| **GPS & Geolocation** | `gps_coordinates`, `ip_geolocation` |
| **APIs & Endpoints** | `api_endpoints` |
| **Credentials** | `credentials` |
| **Findings** | `findings` |
| **Social Media** | `social_media` |
| **Archives** | `wayback_snapshots` |
| **Tracking** | `scan_log`, `collection_progress` |

### Key Table Schemas

```sql
-- DOMAINS TABLE
CREATE TABLE domains (
    id INTEGER PRIMARY KEY,
    domain TEXT UNIQUE NOT NULL,
    domain_type TEXT,               -- government, military, media, etc.
    priority_category TEXT,         -- P1-presidency, P2-military, etc.
    status TEXT DEFAULT 'pending',  -- pending, scanning, complete
    is_wordpress INTEGER DEFAULT 0,
    ip_address TEXT,
    asn TEXT,
    hosting_provider TEXT,
    cdn_provider TEXT,
    local_folder_path TEXT,
    last_scanned TEXT
);

-- WORDPRESS USERS (CRITICAL FOR HASH COLLECTION)
CREATE TABLE wordpress_users (
    id INTEGER PRIMARY KEY,
    wordpress_site_id INTEGER,
    wp_user_id INTEGER,
    username TEXT NOT NULL,
    display_name TEXT,
    gravatar_hash TEXT,             -- MD5 hash from avatar URL
    gravatar_hash_type TEXT,        -- md5 or sha256
    email_cracked TEXT,             -- If hash was reversed
    extracted_at TEXT
);

-- HASHES (MASTER TABLE)
CREATE TABLE hashes (
    id INTEGER PRIMARY KEY,
    domain_id INTEGER,
    hash_value TEXT NOT NULL,
    hash_type TEXT NOT NULL,        -- md5, sha1, sha256, gravatar_md5, etc.
    hash_source TEXT,               -- api, database, file, gravatar
    source_url TEXT,
    associated_username TEXT,
    associated_email TEXT,
    cracked_value TEXT,
    crack_method TEXT,
    discovered_at TEXT
);

-- EMAILS
CREATE TABLE emails (
    id INTEGER PRIMARY KEY,
    domain_id INTEGER,
    email TEXT UNIQUE NOT NULL,
    source TEXT,                    -- api, document, whois, breach
    gravatar_hash TEXT,             -- MD5 of lowercase email
    in_breach_database INTEGER,
    discovered_at TEXT
);

-- FILES
CREATE TABLE files (
    id INTEGER PRIMARY KEY,
    domain_id INTEGER,
    file_type TEXT NOT NULL,        -- pdf, jpg, json, etc.
    original_filename TEXT,
    original_url TEXT,
    local_path TEXT NOT NULL,
    sha256_hash TEXT,
    has_exif INTEGER DEFAULT 0,
    has_gps INTEGER DEFAULT 0,
    downloaded_at TEXT
);

-- GPS COORDINATES
CREATE TABLE gps_coordinates (
    id INTEGER PRIMARY KEY,
    domain_id INTEGER,
    file_id INTEGER,
    latitude REAL NOT NULL,
    longitude REAL NOT NULL,
    source TEXT,                    -- exif, api, document
    source_file TEXT,
    location_description TEXT,
    facility_type TEXT
);

-- FINDINGS
CREATE TABLE findings (
    id INTEGER PRIMARY KEY,
    domain_id INTEGER,
    severity TEXT NOT NULL,         -- critical, high, medium, low, info
    finding_type TEXT,
    title TEXT NOT NULL,
    description TEXT,
    evidence_file_path TEXT,
    status TEXT DEFAULT 'open',
    discovered_at TEXT
);
```

### Useful Views (Pre-Built Queries)

- `v_wordpress_exposed` — All WP sites with exposed user APIs
- `v_gravatar_hashes` — All gravatar hashes with source info
- `v_critical_findings` — High/critical severity findings
- `v_country_progress` — Collection statistics
- `v_gps_locations` — All GPS coordinates with context

### Example Queries

```sql
-- Get all gravatar hashes
SELECT hash_value, associated_username, source_url, cracked_value
FROM hashes WHERE hash_type = 'gravatar_md5';

-- Find duplicate hashes across domains (same person on multiple sites)
SELECT hash_value, COUNT(*) as occurrences, GROUP_CONCAT(source_url)
FROM hashes WHERE hash_type = 'gravatar_md5'
GROUP BY hash_value HAVING COUNT(*) > 1;

-- Get all files with GPS data
SELECT f.original_filename, f.local_path, g.latitude, g.longitude
FROM files f
JOIN gps_coordinates g ON g.file_id = f.id;

-- Get WordPress users with their hashes
SELECT d.domain, wu.username, wu.display_name, wu.gravatar_hash, wu.email_cracked
FROM wordpress_users wu
JOIN wordpress_sites ws ON wu.wordpress_site_id = ws.id
JOIN domains d ON ws.domain_id = d.id;

-- Collection progress
SELECT
    COUNT(DISTINCT d.id) as total_domains,
    SUM(CASE WHEN d.status = 'complete' THEN 1 ELSE 0 END) as completed,
    SUM(d.is_wordpress) as wordpress_sites,
    (SELECT COUNT(*) FROM hashes) as total_hashes,
    (SELECT COUNT(*) FROM emails) as total_emails,
    (SELECT COUNT(*) FROM files) as total_files,
    (SELECT COUNT(*) FROM gps_coordinates) as gps_coords
FROM domains d;
```

### Database Architecture

```
TWO DATABASE LEVELS:

1. MASTER DATABASE (root folder):
   /THE WORLD AT LARGE/
   ├── ODINT_MASTER.db        # Indexes ALL countries
   ├── /Greenland/
   ├── /Antarctica/
   └── /Venezuela/

2. COUNTRY DATABASE (per country):
   /[COUNTRY-NAME]/
   ├── [COUNTRY-NAME].db      # All data for this country
   ├── sourcelist.txt
   └── /[subfolders]/
```

**Why two levels:**
- `MASTER.db` = Bird's eye view of ALL operations
- `Country.db` = Deep dive into specific country
- Can query across all countries from master
- Can work offline on single country
- Enables cross-country correlation

---

## Section 0.4: HTTP & Edge-Level Documentation

For **EVERY** website accessed, capture ALL of the following:

### HTTP Response Headers

<details>
<summary><strong>Server Identification</strong></summary>

- [ ] `Server:` (Apache, nginx, IIS, LiteSpeed, etc.)
- [ ] `X-Powered-By:` (PHP, ASP.NET, Express, etc.)
- [ ] `X-AspNet-Version:`
- [ ] `X-AspNetMvc-Version:`
- [ ] `X-Generator:` (WordPress, Drupal, etc.)
- [ ] `X-Drupal-Cache:`
- [ ] `X-Varnish:`
- [ ] `Via:` (proxy information)
- [ ] `X-Served-By:`
- [ ] `X-Backend-Server:`

</details>

<details>
<summary><strong>CDN & Caching Headers</strong></summary>

- [ ] `X-Cache:` (HIT/MISS)
- [ ] `CF-Ray:` (Cloudflare ray ID)
- [ ] `CF-Cache-Status:`
- [ ] `X-CDN:`
- [ ] `X-Akamai-*:`
- [ ] `X-Fastly-*:`
- [ ] `X-Amz-Cf-*:` (CloudFront)
- [ ] `Age:`
- [ ] `Cache-Control:`
- [ ] `ETag:`
- [ ] `Last-Modified:`

</details>

<details>
<summary><strong>Security Headers</strong></summary>

- [ ] `Strict-Transport-Security:` (HSTS)
- [ ] `Content-Security-Policy:`
- [ ] `X-Content-Type-Options:`
- [ ] `X-Frame-Options:`
- [ ] `X-XSS-Protection:`
- [ ] `Referrer-Policy:`
- [ ] `Permissions-Policy:`
- [ ] `Cross-Origin-Opener-Policy:`
- [ ] `Cross-Origin-Embedder-Policy:`
- [ ] `Cross-Origin-Resource-Policy:`

</details>

<details>
<summary><strong>CORS Headers</strong></summary>

- [ ] `Access-Control-Allow-Origin:`
- [ ] `Access-Control-Allow-Methods:`
- [ ] `Access-Control-Allow-Headers:`
- [ ] `Access-Control-Allow-Credentials:`
- [ ] `Access-Control-Expose-Headers:`
- [ ] `Access-Control-Max-Age:`

> Misconfigured CORS = security finding!

</details>

<details>
<summary><strong>Cloud Provider Headers</strong></summary>

**AWS:** `X-Amz-Request-Id`, `X-Amz-Id-2`, `X-Amz-Bucket-Region`, `X-Amz-Cf-Pop`

**Azure:** `X-Azure-Ref`, `X-MS-Request-Id`, `X-AspNet-Version`

**Google Cloud:** `X-Cloud-Trace-Context`, `X-GFE-*`, `X-Google-*`

**Cloudflare:** `CF-Ray`, `CF-Cache-Status`, `CF-Request-ID`

</details>

<details>
<summary><strong>WAF/Protection Indicators</strong></summary>

- [ ] `X-Sucuri-*:`
- [ ] `X-Mod-Security:`
- [ ] `X-Protected-By:`
- [ ] `X-WAF-*:`
- [ ] `Server: cloudflare`
- [ ] `Server: AkamaiGHost`

</details>

### TLS/SSL Details

<details>
<summary><strong>Certificate Information</strong></summary>

- [ ] Subject (CN, O, OU, L, ST, C)
- [ ] Issuer (full chain)
- [ ] Serial number
- [ ] Valid from / Valid to
- [ ] Signature algorithm
- [ ] Public key algorithm & size
- [ ] Subject Alternative Names (SANs)
- [ ] Certificate fingerprint (SHA256)
- [ ] Certificate chain (full)
- [ ] OCSP stapling status
- [ ] Certificate Transparency SCTs

</details>

<details>
<summary><strong>TLS Connection Details</strong></summary>

- [ ] TLS version (1.0, 1.1, 1.2, 1.3)
- [ ] Cipher suite used
- [ ] Key exchange algorithm
- [ ] Perfect Forward Secrecy (PFS)
- [ ] ALPN (HTTP/2, HTTP/3)

</details>

<details>
<summary><strong>SSL/TLS Security Issues</strong></summary>

- [ ] SSLv2/SSLv3 enabled? (vulnerability)
- [ ] TLS 1.0/1.1 enabled? (deprecated)
- [ ] Weak cipher suites?
- [ ] Certificate expiring soon?
- [ ] Self-signed certificate?
- [ ] Certificate name mismatch?
- [ ] Incomplete certificate chain?
- [ ] HSTS enabled? HSTS preload?

</details>

### Cookies

For **EVERY** cookie set, document:
- Cookie name & value
- Domain & path
- Expires / Max-Age
- `Secure` flag, `HttpOnly` flag, `SameSite` attribute
- First-party vs third-party

**Common cookies to look for:** `PHPSESSID`, `JSESSIONID`, `ASP.NET_SessionId`, `wordpress_logged_in_*`, `__cfduid`, `_ga`, `_gid`, `_fbp`, `AWSALB`, `BIGipServer*`

> Cookie names can reveal: framework, hosting, security tools, analytics

### HTML Meta Tags & Page Head

- Basic meta tags (`title`, `description`, `keywords`, `author`, `generator`, `robots`)
- Open Graph tags (`og:title`, `og:description`, `og:image`, etc.)
- Twitter Card tags (`twitter:card`, `twitter:site`, `twitter:creator`, etc.)
- Schema.org / JSON-LD structured data
- Canonical URLs, alternate hreflang, manifest, favicons

### JavaScript Analysis

- **Framework detection:** React, Vue, Angular, jQuery, Bootstrap, Next.js, etc.
- **Analytics & tracking:** Google Analytics, GTM, Facebook Pixel, Hotjar, Clarity, etc.
- **Third-party scripts:** CDN libraries, chat widgets, payment processors, error tracking
- **Inline scripts:** Hardcoded API keys, URLs, config objects, debug flags
- **Source maps:** `.js.map` / `.css.map` files (can reveal source code)

### Error Responses

Intentionally trigger and document error pages (400, 401, 403, 404, 405, 500, 502, 503). For each, capture:
- Full HTML response
- Server software / framework revealed
- File paths / stack traces / internal IPs
- Custom vs default error page

### Response Storage Format

```
/http-data/[domain]/
├── response_headers_[date].txt
├── ssl_certificate_[date].txt
├── ssl_chain_[date].pem
├── cookies_[date].txt
├── meta_tags_[date].txt
├── scripts_inventory_[date].txt
├── third_party_[date].txt
├── /error_pages/
│   ├── 404.html
│   └── 500.html
└── /screenshots/
    ├── homepage_[date].png
    └── login_[date].png
```

---

## Section 0.5: Recommended Tools Reference

| Category | Tools |
|----------|-------|
| **Subdomain & DNS** | Amass (passive), Subfinder, Assetfinder, crt.sh, SecurityTrails, DNSdumpster, dig/nslookup, MassDNS |
| **Tech Fingerprinting** | Wappalyzer, WhatWeb, BuiltWith, Netcraft, httpx, curl |
| **WordPress** | WPScan (`--enumerate u`), curl `/wp-json/wp/v2/users`, WordPress API |
| **Metadata Extraction** | ExifTool, pdfinfo, mat2, FOCA, Metagoofil |
| **Screenshot & Archiving** | Eyewitness, gowitness, Wayback Machine, Archive.today, SingleFile, wget |
| **Hash Analysis** | hashid, hash-identifier, hashcat, john, CrackStation |
| **API Testing** | curl, httpie, Postman, Insomnia, GraphQL Playground, Swagger UI |
| **Google Dorking** | Manual searches, Dorkbot, GHDB |
| **Social Media** | Sherlock, social-analyzer, Twint, Instaloader, yt-dlp, gallery-dl |
| **Network Analysis** | Shodan, Censys, Hurricane Electric BGP, RIPEstat, ipinfo.io, whois |
| **Code Repos** | GitHub search, GitDorker, Gitrob, TruffleHog, gitleaks |
| **Breach Data** | Have I Been Pwned, DeHashed, IntelX, h8mail |
| **Geospatial** | Google Earth Pro, Sentinel Hub, OpenStreetMap, Mapillary |
| **Document Analysis** | ExifTool, pdfparser, oletools, Apache Tika |
| **File Downloading** | wget, curl, aria2c, httrack |
| **Mobile App Analysis** | apktool, jadx, MobSF, Frida, dex2jar |
| **Certificate Analysis** | openssl, sslyze, testssl.sh, crt.sh |
| **Automation** | Python + requests, Scrapy, BeautifulSoup, Selenium, Playwright |

---

## Section 0.6: Additional OSINT Sources

<details>
<summary><strong>Social Media Accounts</strong></summary>

- [ ] Twitter/X official accounts
- [ ] Facebook pages
- [ ] Instagram accounts
- [ ] YouTube channels
- [ ] TikTok accounts
- [ ] LinkedIn company pages
- [ ] Telegram channels
- [ ] WhatsApp (if public groups)
- [ ] VK (Russia/CIS)
- [ ] Weibo (China)

> Download ALL posts, images, videos, follower lists. Archive before deletion.

</details>

<details>
<summary><strong>Code Repositories</strong></summary>

- [ ] GitHub organizations
- [ ] GitLab instances
- [ ] Bitbucket repos
- [ ] Self-hosted Git servers
- [ ] npm / PyPI packages published
- [ ] Docker Hub images

> Search for: API keys, credentials, internal URLs, employee names

</details>

<details>
<summary><strong>Mobile Applications</strong></summary>

- [ ] Google Play Store apps
- [ ] Apple App Store apps
- [ ] APK download and analysis
- [ ] Embedded API endpoints
- [ ] Hardcoded credentials
- [ ] Certificate pinning info

</details>

<details>
<summary><strong>Cloud Storage Exposure</strong></summary>

- [ ] Amazon S3 buckets
- [ ] Azure Blob storage
- [ ] Google Cloud Storage buckets
- [ ] DigitalOcean Spaces
- [ ] Misconfigured cloud storage

</details>

<details>
<summary><strong>DNS Records (Complete Enumeration)</strong></summary>

- [ ] A records (IPv4)
- [ ] AAAA records (IPv6)
- [ ] MX records (mail servers)
- [ ] TXT records (SPF, DKIM, DMARC, verification)
- [ ] NS records (nameservers)
- [ ] SOA records (authority)
- [ ] CNAME records (aliases)
- [ ] SRV records (services)
- [ ] CAA records (certificate authority)
- [ ] PTR records (reverse DNS)

</details>

<details>
<summary><strong>Email Infrastructure</strong></summary>

- [ ] MX record analysis
- [ ] SPF record parsing
- [ ] DKIM selector enumeration
- [ ] DMARC policy check
- [ ] Email gateway identification
- [ ] Webmail portals
- [ ] Outlook Web Access / Exchange autodiscover

</details>

<details>
<summary><strong>Google Dorking Templates</strong></summary>

```
site:target.gov.xx filetype:pdf
site:target.gov.xx filetype:xls
site:target.gov.xx filetype:doc
site:target.gov.xx filetype:sql
site:target.gov.xx filetype:log
site:target.gov.xx filetype:bak
site:target.gov.xx filetype:env
site:target.gov.xx "index of"
site:target.gov.xx inurl:admin
site:target.gov.xx inurl:login
site:target.gov.xx inurl:api
site:target.gov.xx "password"
site:target.gov.xx ext:php inurl:config
"@target.gov.xx" (email search)
```

</details>

<details>
<summary><strong>Internet-Wide Scan Data</strong></summary>

Shodan, Censys, ZoomEye, BinaryEdge, GreyNoise, FOFA

> Search by: IP, domain, org, ASN, SSL cert

</details>

<details>
<summary><strong>Breach/Leak Data</strong></summary>

Have I Been Pwned (domain search), DeHashed, LeakCheck, Snusbase, IntelX

> Search for: @target.gov.xx emails in breaches

</details>

<details>
<summary><strong>Paste Sites</strong></summary>

Pastebin, GitHub Gists, Ghostbin, JustPaste.it, Dpaste

> Search for: domain mentions, leaked credentials, configs

</details>

<details>
<summary><strong>Archive & Historical</strong></summary>

Wayback Machine, Archive.today, Google Cache, Bing Cache, Common Crawl

> Systematic archiving of ALL pages before changes

</details>

<details>
<summary><strong>WHOIS History</strong></summary>

DomainTools, WhoisXML API, SecurityTrails — historical ownership, registrant changes, name server changes

</details>

<details>
<summary><strong>Certificate Transparency (Deep)</strong></summary>

crt.sh, Censys certificates, Google CT logs, Facebook CT logs, historical certificates, wildcard certs (reveal subdomains)

</details>

<details>
<summary><strong>Job Postings & Procurement</strong></summary>

Government job portals, LinkedIn, Indeed, procurement/tender documents, RFP/RFQ

> Reveals: tech stack, vendors, internal systems, org structure

</details>

<details>
<summary><strong>Legal & Public Records</strong></summary>

Court records, corporate registries, sanctions lists, FOIA requests, government gazettes, parliamentary records, budget documents

</details>

<details>
<summary><strong>Geospatial Intelligence</strong></summary>

Google Maps/Street View, Bing Maps, Yandex Maps, satellite imagery, OpenStreetMap, building footprints

> Cross-reference with GPS from EXIF

</details>

<details>
<summary><strong>Network Intelligence</strong></summary>

BGP routing data, ASN ownership, IP range allocation, peering relationships, Hurricane Electric BGP Toolkit, RIPE/ARIN databases

</details>

<details>
<summary><strong>Reverse Image Search</strong></summary>

Google Images, TinEye, Yandex Images, Bing Visual Search

> Use on: official portraits, facility photos, document images

</details>

<details>
<summary><strong>Metadata Deep Dive</strong></summary>

ExifTool on all images, PDF metadata (pdfinfo), Office document metadata, video metadata (ffprobe), embedded thumbnails, edit history, printer/scanner metadata

</details>

---

## Section 1: Target Source Categories

### Government — Core
- [ ] Primary government portals
- [ ] Executive branch websites
- [ ] Legislative websites
- [ ] Official gazette/legal publications

### Government — Ministries & Agencies
- [ ] Ministry websites enumerated
- [ ] Agency portals identified
- [ ] Statistical offices
- [ ] Regulatory bodies

### Law Enforcement & Judiciary
- [ ] Police/security services
- [ ] Court systems
- [ ] Prison/corrections
- [ ] Intelligence agencies (public-facing)

### Military & Defense
- [ ] Defense ministry
- [ ] Armed forces branches
- [ ] Military contractors
- [ ] Defense procurement

### State-Owned Enterprises
- [ ] Telecom providers
- [ ] Banks/financial institutions
- [ ] Energy/utilities
- [ ] Transportation
- [ ] Media/broadcasting

### Education & Research
- [ ] Universities
- [ ] Research institutes
- [ ] National academies
- [ ] Educational portals

### Infrastructure & Registries
- [ ] Domain registrars (ccTLD)
- [ ] WHOIS services
- [ ] Certificate authorities
- [ ] National registries

### Diplomatic Representations
- [ ] Embassies
- [ ] Consulates
- [ ] Foreign missions

### Media
- [ ] State media outlets
- [ ] Public broadcasters
- [ ] News agencies

### Regional/Local Government
- [ ] Municipalities
- [ ] Regional governments
- [ ] Local councils

### Business & Tourism
- [ ] Tourism boards
- [ ] Investment agencies
- [ ] Trade promotion

### Developer/Vendor
- [ ] Government IT contractors
- [ ] Web development firms
- [ ] Hosting providers
- [ ] Software vendors

---

## Section 2: Collection Folders

| Folder | Contents |
|--------|----------|
| `/apis` | REST API endpoints, GraphQL schemas, Swagger specs, archived responses |
| `/archives` | Wayback snapshots, historical versions, deleted content, timelines |
| `/backups` | `.bak` files, `.sql` dumps, database exports, config backups |
| `/configs` | `.env` files, configuration files, settings exports, `.htaccess` |
| `/credentials` | Exposed API keys, tokens, password files, auth artifacts |
| `/critical-findings` | High-severity vulnerabilities, immediate risks, evidence, timelines |
| `/documents` | PDFs, Office docs, government publications, reports |
| `/domains` | Primary domains, registration info, historical ownership |
| `/downloads` | Raw downloads staging, bulk exports, datasets |
| `/geolocation` | IP geolocation, server locations, facility locations |
| `/gps-coords` | EXIF GPS, location coordinates, facility coordinates |
| `/hashes` | MD5, SHA256, Gravatar hashes, cracking results |
| `/infrastructure` | Hosting providers, CDN mapping, load balancers, network architecture |
| `/ip-ranges` | IP addresses, netblocks, ASN info, BGP data |
| `/keys` | SSH public keys, PGP keys, API keys, encryption keys |
| `/logs` | Exposed log files, error logs, access logs, debug output |
| `/metadata` | Document metadata, author info, software versions, dates |
| `/notes` | Research notes, observations, anomalies, follow-up questions |
| `/personnel` | Named individuals, org charts, contacts, roles |
| `/photos` | Images with EXIF preserved, screenshots, visual evidence |
| `/raw` | Raw API responses, unprocessed data, original files |
| `/reports` | Analysis reports, summaries, findings writeups |
| `/scripts` | Collection scripts, analysis tools, automation code |
| `/source-code` | Exposed source files, `.git` directories, code snippets |
| `/sources` | Source documentation, attribution records, chain of custody |
| `/ssl-certificates` | Certificate downloads, CT log entries, expiry tracking |
| `/subdomains` | Subdomain enumeration, passive DNS, CT log discoveries |
| `/tech-stacks` | CMS identification, framework fingerprints, version info |
| `/usernames` | Username enumeration, account names, user IDs |
| `/videos` | Video downloads, metadata, transcripts, screenshots |

---

## Section 3: Full Technology Stack Enumeration

<details>
<summary><strong>Server Infrastructure</strong></summary>

- [ ] Web server (Apache, Nginx, IIS, LiteSpeed, Caddy)
- [ ] Server OS fingerprint
- [ ] Reverse proxy detection
- [ ] Load balancer identification
- [ ] WAF detection (Cloudflare, Akamai, AWS WAF, ModSecurity)
- [ ] DDoS protection services

</details>

<details>
<summary><strong>Content Management Systems</strong></summary>

- [ ] WordPress (version, theme, plugins)
- [ ] Drupal (version, modules)
- [ ] Joomla (version, extensions)
- [ ] Sitecore, Umbraco, Adobe Experience Manager
- [ ] Headless CMS (Contentful, Strapi, Directus)
- [ ] Custom CMS identification

</details>

<details>
<summary><strong>Frontend Frameworks & Libraries</strong></summary>

- [ ] React / Vue.js / Angular / Svelte
- [ ] Next.js / Nuxt.js / SvelteKit
- [ ] jQuery (version), Bootstrap (version)
- [ ] Tailwind CSS, Material UI

</details>

<details>
<summary><strong>Backend Frameworks</strong></summary>

- [ ] Node.js / Express
- [ ] Django / Flask (Python)
- [ ] Ruby on Rails
- [ ] Laravel / Symfony (PHP)
- [ ] ASP.NET / .NET Core
- [ ] Spring Boot (Java)
- [ ] Go / Rust frameworks

</details>

<details>
<summary><strong>Database Systems</strong></summary>

- [ ] MySQL / MariaDB / PostgreSQL
- [ ] Microsoft SQL Server / Oracle
- [ ] MongoDB / Redis / Elasticsearch
- [ ] SQLite indicators

</details>

<details>
<summary><strong>Hosting & Cloud Providers</strong></summary>

- [ ] AWS (S3, EC2, CloudFront)
- [ ] Azure, Google Cloud Platform
- [ ] DigitalOcean, Cloudflare, Vercel, Netlify
- [ ] Heroku, OVH, Hetzner
- [ ] On-premise indicators

</details>

<details>
<summary><strong>CDN & Caching</strong></summary>

Cloudflare, Akamai, Fastly, AWS CloudFront, Azure CDN, Varnish, Redis, Memcached

</details>

<details>
<summary><strong>Authentication & SSO</strong></summary>

- [ ] OAuth, SAML, OpenID Connect
- [ ] LDAP/Active Directory indicators
- [ ] MFA indicators
- [ ] National ID systems (NemID, BankID, etc.)

</details>

<details>
<summary><strong>Analytics, Tracking & Third-Party Services</strong></summary>

- [ ] Google Analytics, Matomo, Adobe Analytics, Hotjar, Clarity
- [ ] Facebook Pixel, tag managers
- [ ] Payment processors, email services, chat widgets
- [ ] Search services, maps, social media integrations

</details>

<details>
<summary><strong>Security Tools & Build Tools</strong></summary>

- [ ] Wordfence, Sucuri, reCAPTCHA/hCaptcha
- [ ] Rate limiting, CSP, HSTS
- [ ] Webpack, Vite, source map exposure

</details>

---

## Section 4: Path & Directory Enumeration

<details>
<summary><strong>Standard Paths</strong></summary>

`/robots.txt` `/sitemap.xml` `/sitemap_index.xml` `/.well-known/` `/.well-known/security.txt` `/humans.txt` `/ads.txt` `/crossdomain.xml` `/clientaccesspolicy.xml`

</details>

<details>
<summary><strong>Admin & Login Paths</strong></summary>

`/admin/` `/administrator/` `/login/` `/wp-admin/` `/wp-login.php` `/user/login` `/panel/` `/dashboard/` `/cpanel/` `/webmail/` `/portal/`

</details>

<details>
<summary><strong>API Paths</strong></summary>

`/api/` `/api/v1/` `/api/v2/` `/rest/` `/graphql` `/graphiql` `/wp-json/` `/wp-json/wp/v2/` `/_api/` `/services/` `/webservices/`

</details>

<details>
<summary><strong>Documentation Paths</strong></summary>

`/swagger/` `/swagger-ui/` `/swagger.json` `/openapi.json` `/api-docs/` `/docs/` `/documentation/` `/redoc/`

</details>

<details>
<summary><strong>Configuration & Sensitive Paths</strong></summary>

`/.git/` `/.git/config` `/.gitignore` `/.env` `/.env.local` `/.env.production` `/config.php` `/wp-config.php` `/wp-config.php.bak` `/web.config` `/.htaccess` `/.htpasswd` `/config/database.yml` `/config/secrets.yml`

</details>

<details>
<summary><strong>Backup & Archive Paths</strong></summary>

`/backup/` `/backups/` `/bak/` `/old/` `/archive/` `/temp/` `/tmp/` `/dump/` `/sql/` `/database/` `/db/` `/data/` `/export/` `/uploads/` `/files/` `/private/`

Common backup extensions: `*.bak` `*.backup` `*.old` `*.orig` `*.swp` `*.sql` `*.sql.gz` `*.tar.gz` `*.zip` `*.7z`

</details>

<details>
<summary><strong>Log File Paths</strong></summary>

`/logs/` `/log/` `/error.log` `/access.log` `/debug.log` `/application.log` `/wp-content/debug.log`

</details>

<details>
<summary><strong>Debug & Development Paths</strong></summary>

`/debug/` `/test/` `/dev/` `/staging/` `/beta/` `/phpinfo.php` `/info.php` `/server-status` `/server-info` `/.DS_Store` `/elmah.axd` `/trace.axd`

</details>

<details>
<summary><strong>CMS-Specific Paths</strong></summary>

**WordPress:** `/wp-content/` `/wp-content/uploads/` `/wp-content/plugins/` `/wp-content/themes/` `/wp-includes/` `/xmlrpc.php` `/readme.html`

**Drupal:** `/core/` `/modules/` `/sites/default/` `/CHANGELOG.txt` `/update.php`

**Joomla:** `/components/` `/modules/` `/plugins/` `/administrator/` `/configuration.php`

</details>

<details>
<summary><strong>Source Code Paths</strong></summary>

`/.svn/` `/.hg/` `/.bzr/` `/CVS/` `/.idea/` `/.vscode/` `/node_modules/` `/vendor/` `/composer.json` `/package.json` `/yarn.lock` `/Gemfile` `/requirements.txt`

</details>

---

## Section 5: API Enumeration & Hunting

### API Discovery Methods

- [ ] Check `/robots.txt` for API hints
- [ ] Analyze JavaScript files for endpoints
- [ ] Monitor network requests in browser
- [ ] Check mobile app traffic
- [ ] Review HTML comments for API references
- [ ] Search GitHub for target API references
- [ ] Check Wayback Machine for historical APIs
- [ ] Analyze error messages for endpoint leaks

### WordPress REST API (`/wp-json/`)

```
/                           # Root namespace discovery
/wp/v2/users                # USER ENUMERATION
/wp/v2/users?per_page=100   # All users
/wp/v2/posts                # Posts
/wp/v2/pages                # Pages
/wp/v2/media                # Media library
/wp/v2/categories           # Categories
/wp/v2/tags                 # Tags
/wp/v2/comments             # Comments
/wp/v2/search               # Search
/oembed/1.0/                # oEmbed
/wc/v3/                     # WooCommerce
/yoast/v1/                  # Yoast SEO
/acf/v3/                    # Advanced Custom Fields
```

### GraphQL Enumeration

Endpoints: `/graphql` `/graphiql` `/v1/graphql` `/api/graphql` `/query`

Check for: introspection query, `__schema`, `__type`, field enumeration, mutation discovery

### REST API Common Endpoints

```
/api/users    /api/me       /api/profile  /api/admin
/api/auth     /api/login    /api/token    /api/config
/api/settings /api/status   /api/health   /api/version
/api/search   /api/data     /api/export   /api/upload
/api/files    /api/documents /api/reports
```

### API Documentation Endpoints

```
/swagger.json       /openapi.json       /api-docs
/swagger-ui         /swagger-ui.html    /redoc
/rapidoc            /swagger-resources
```

### Drupal JSONAPI

```
/jsonapi            /jsonapi/node/article
/jsonapi/user/user  /jsonapi/taxonomy_term/
/jsonapi/file/file  /jsonapi/media/
```

### API Parameter Fuzzing (passive observation)

```
?page= ?per_page= ?limit= ?offset= ?sort= ?order=
?filter= ?search= ?q= ?query= ?fields= ?include=
?exclude= ?expand= ?embed= ?format= ?id=
```

### API Security Checks

- [ ] Authentication required?
- [ ] API keys exposed in JS?
- [ ] CORS misconfiguration?
- [ ] Rate limiting present?
- [ ] Error message verbosity?
- [ ] Version disclosure?
- [ ] Debug mode enabled?
- [ ] HTTPS enforced?

---

## Section 6: Critical Data Hunting

> **THESE ARE THE MOST VALUABLE FINDS — ALWAYS BE ON ALERT**

### Hashes

- [ ] MD5 hashes in API responses
- [ ] SHA1/SHA256 hashes exposed
- [ ] Gravatar hashes (`avatar_urls` in WordPress)
- [ ] Password hashes in database dumps
- [ ] Session token hashes, API key hashes, file integrity hashes

> **ACTION:** Extract ALL hashes to `/hashes/`. Attempt identification. Cross-reference with lookup services.

### WordPress Gravatar Hashes — Highest Priority

Gravatar hashes are MD5 hashes of user email addresses. They appear in the WordPress REST API:

```json
{
  "id": 1,
  "name": "Admin User",
  "slug": "admin",
  "avatar_urls": {
    "24": "https://secure.gravatar.com/avatar/[MD5_HASH]?s=24",
    "48": "https://secure.gravatar.com/avatar/[MD5_HASH]?s=48",
    "96": "https://secure.gravatar.com/avatar/[MD5_HASH]?s=96"
  }
}
```

**Extraction process:**
1. Query `GET /wp-json/wp/v2/users?per_page=100`
2. Extract all `avatar_urls` from response
3. Parse the MD5 hash from each URL
4. Document: `[username] | [display_name] | [MD5_hash] | [source_url] | [timestamp]`
5. Save to `/hashes/[domain]_gravatar_hashes_[date].txt`

**Cross-correlation value:** The same gravatar hash appears on every WordPress site, Gravatar.com profiles, GitHub, Stack Overflow — one hash can track identity across the internet.

**Storage format:**
```
# Gravatar Hash Extraction
# Source: https://target.gov.xx/wp-json/wp/v2/users
# Extracted: 2026-01-20 14:30:00 UTC
# Total Users: 10

USERNAME        | DISPLAY NAME      | MD5 HASH                         | USER ID
----------------|-------------------|----------------------------------|--------
admin           | Administrator     | d41d8cd98f00b204e9800998ecf8427e | 1
jgarcia         | Juan Garcia       | 5d41402abc4b2a76b9719d911017c592 | 2
```

### Usernames

- [ ] WordPress user enumeration (`/wp-json/wp/v2/users`)
- [ ] Usernames in API responses, error messages, URL paths
- [ ] Admin/system/service account names
- [ ] Usernames in document metadata, email addresses, code comments

> **ACTION:** Extract ALL usernames to `/usernames/`. Correlate across systems. Build personnel profiles.

### Email Addresses

- [ ] Emails in API responses, document metadata, WHOIS, SSL certificates
- [ ] Emails in contact pages, source code, JavaScript, error messages
- [ ] Admin/support/developer emails, personal emails of officials

> **ACTION:** Extract ALL emails to `/personnel/`. Generate Gravatar hashes. Cross-reference across systems.

### GPS Coordinates

- [ ] EXIF GPS data in images
- [ ] Coordinates in document metadata, API responses, JavaScript/config
- [ ] Coordinates in KML/GeoJSON files, embedded maps

> **ACTION:** Extract ALL coordinates to `/gps-coords/`. Map to facilities. Correlate with personnel.

### API Keys & Tokens

- [ ] API keys in JavaScript files, HTML source, mobile app configs
- [ ] AWS/Azure/Google/Stripe keys
- [ ] OAuth tokens, JWT tokens (decode for claims), session tokens

> **ACTION:** Extract to `/credentials/`. DO NOT use keys — document only.

### Personally Identifiable Information (PII)

- [ ] Full names, national ID numbers, phone numbers, addresses
- [ ] Dates of birth, passport numbers, bank account numbers

> **ACTION:** Handle with extreme care. Assess human rights implications.

### Internal Infrastructure Data

- [ ] Internal IP addresses, hostnames, database connection strings
- [ ] LDAP/AD structure, VPN configs, network diagrams
- [ ] Staging/dev environment URLs

### Sensitive Documents

- [ ] Classified markings, internal memos, personnel files
- [ ] Financial records, contracts, security policies
- [ ] Incident reports, audit logs, surveillance records

> **ACTION:** Archive immediately. Assess human rights relevance.

### Raw Filenames

- [ ] Filenames from `/uploads/` directories, download links, galleries
- [ ] Filenames in API responses, directory listings, sitemap.xml
- [ ] Filenames in error messages, JavaScript, PDF internal links

**Intelligence value of filenames:**
| Filename Pattern | Intelligence |
|-----------------|-------------|
| `informe_ministro_2026.pdf` | Reveals hierarchy |
| `backup_usuarios_20260101.sql` | Backup schedules |
| `foto_base_militar_GPS.jpg` | Location intel |
| `nomina_policia_enero.xls` | Payroll data exists |
| `acta_secreta_001.doc` | Classification schemes |
| `proyecto_aguila_fase2.ppt` | Project codenames |

### Raw Photos & Media

- [ ] Download ORIGINAL files, not thumbnails
- [ ] NEVER screenshot instead of download
- [ ] NEVER convert or compress
- [ ] Preserve original filename
- [ ] Extract EXIF immediately (GPS, camera model, date/time, software, author)
- [ ] Military photos often contain GPS of bases

---

## Section 7: Target Priority Order

> **ALWAYS AUDIT IN THIS ORDER**

| Priority | Category | Rationale |
|----------|----------|-----------|
| **P1** | Presidency / Executive | Highest value targets, most sensitive data |
| **P2** | Military & Defense | Strategic intelligence value |
| **P3** | Intelligence & Security Services | Surveillance infrastructure documentation |
| **P4** | Law Enforcement | Human rights documentation |
| **P5** | Core Government Ministries | Citizen data exposure |
| **P6** | State Media & Propaganda | Propaganda infrastructure mapping |
| **P7** | State-Owned Enterprises | Infrastructure & economic data |
| **P8** | Regional & Local Government | Distributed infrastructure |
| **P9** | Education & Research | Intellectual property, personnel |
| **P10** | Other Government Services | Citizen data, lower priority |

<details>
<summary><strong>Priority 1 — Presidency / Executive (Highest)</strong></summary>

- [ ] Presidential palace/office website
- [ ] President's official page
- [ ] Executive office portals
- [ ] Cabinet websites
- [ ] Prime Minister / Vice President / First Lady offices
- [ ] Presidential press office & communications

</details>

<details>
<summary><strong>Priority 2 — Military & Defense</strong></summary>

- [ ] Ministry of Defense
- [ ] Army, Navy, Air Force
- [ ] Special Forces, National Guard
- [ ] Military intelligence (public-facing)
- [ ] Defense contractors & academies
- [ ] Veterans affairs, procurement/logistics

</details>

<details>
<summary><strong>Priority 3 — Intelligence & Security Services</strong></summary>

- [ ] Intelligence agencies (public portals)
- [ ] Secret police / internal security
- [ ] Counterterrorism & cybersecurity agencies
- [ ] Border security & immigration services
- [ ] National security council

</details>

<details>
<summary><strong>Priority 4 — Law Enforcement</strong></summary>

- [ ] National police & federal investigation
- [ ] Criminal investigation & forensics
- [ ] Prison/corrections & parole
- [ ] Police academies

</details>

<details>
<summary><strong>Priority 5 — Core Government Ministries</strong></summary>

- [ ] Interior/Home Affairs, Foreign Affairs, Justice
- [ ] Finance/Treasury, Communications/IT
- [ ] Central Bank, Tax authority, Customs
- [ ] Civil registry, Electoral commission

</details>

<details>
<summary><strong>Priority 6 — State Media</strong></summary>

- [ ] State television & radio
- [ ] Official news agencies & newspapers
- [ ] State social media accounts
- [ ] Propaganda/information ministries

</details>

<details>
<summary><strong>Priority 7–10 — Lower Priority</strong></summary>

- State-owned enterprises (telecom, banks, energy, transport)
- Regional/local government
- Education & research institutions
- Health, social services, agriculture, tourism, culture

</details>

---

## Section 8: Technical Audit Checklist

For each target:

- [ ] **Domain Enumeration** — Primary domains, subdomain brute-force (passive), CT search, passive DNS, WHOIS/RDAP, historical DNS
- [ ] **Infrastructure Mapping** — IP resolution, netblock ID, ASN lookup, hosting/CDN/geo
- [ ] **Document Discovery** — PDFs, Office docs, data exports, spreadsheets, database dumps, archives
- [ ] **SSL/TLS Analysis** — Certificate details, issuer, validity, SANs, chain, CT log monitoring
- [ ] **Metadata Extraction** — Author info, timestamps, software versions, EXIF/GPS, edit history
- [ ] **Identity Correlation** — Email enumeration, username collection, hash extraction, Gravatar correlation, social media, personnel ID

---

## Section 10: Threat Classification

| Priority | Category | Focus |
|----------|----------|-------|
| **High** | Authoritarian Regimes | Surveillance, censorship, human rights, opposition tracking, propaganda |
| **High** | Large Infrastructure | Complex systems, interconnected services, large user DBs, critical infrastructure |
| **Medium** | Territorial/Disputed | Sovereignty systems, disputed territory, cross-border, international coordination |
| **Standard** | General Audit | Democratic transparency, public accountability, data exposure, security posture |

---

## Section 11: Methodology Checklist

For each target domain:

1. [ ] **VERIFY** — DNS resolution, site is live
2. [ ] **ROBOTS** — Check robots.txt and sitemap.xml
3. [ ] **SUBDOMAINS** — Passive enumeration (crt.sh, DNS)
4. [ ] **FINGERPRINT** — Tech stack identification
5. [ ] **APIs** — Check for exposed API endpoints
6. [ ] **WAYBACK** — Historical analysis
7. [ ] **CERTIFICATES** — CT log search
8. [ ] **SENSITIVE** — Check for .git, .env, backups
9. [ ] **DOCUMENTS** — Enumerate public documents
10. [ ] **METADATA** — Extract from all files
11. [ ] **DOCUMENT** — Record findings with timestamps
12. [ ] **ARCHIVE** — Preserve evidence

---

## Section 12: Operational Protocols

### Legal Compliance

- [x] All methods are PASSIVE reconnaissance
- [x] All data is PUBLICLY ACCESSIBLE
- [x] No active exploitation or intrusion
- [x] No unauthorized access attempts
- [x] Methodology is reproducible and documentable

### Ethical Standards

- [x] Journalist/activist data scrubbed within 24 hours on request
- [x] Vulnerable individual protection prioritized
- [x] Responsible disclosure considered case-by-case
- [x] Human rights implications assessed
- [x] Partner org coordination maintained

### Evidence Handling

- [x] Chain of custody documented
- [x] Timestamps on all collection
- [x] Checksums for file integrity
- [x] Original files preserved
- [x] Backup copies maintained

---

## Section 13: Tracking & Metrics

### Domain Statistics

| Metric | Count |
|--------|-------|
| Total Domains Scanned | |
| Subdomains Discovered | |
| IPs Enumerated | |
| SSL Certificates Analyzed | |

### Technology Findings

| Metric | Count |
|--------|-------|
| WordPress Sites Found | |
| Drupal Sites Found | |
| Custom CMS Sites | |
| APIs Documented | |
| GraphQL Endpoints | |

### WordPress User Enumeration

| Metric | Count |
|--------|-------|
| WP Sites with Exposed Users | |
| WP Sites with Protected Users | |
| Total WP Users Enumerated | |
| Total Gravatar MD5 Hashes | |
| Total Gravatar SHA256 Hashes | |
| Gravatar Hashes Cracked | |
| Emails Recovered from Hashes | |

### Critical Data Extracted

| Metric | Count |
|--------|-------|
| Usernames Enumerated | |
| Emails Directly Exposed | |
| Emails from Cracked Hashes | |
| Total Unique Emails | |
| MD5 Hashes Extracted | |
| SHA1 Hashes Extracted | |
| SHA256 Hashes Extracted | |
| Total Hashes Cracked | |
| GPS Coordinates Found | |
| API Keys/Tokens | |
| Filenames Captured | |

### Personnel Identified

| Metric | Count |
|--------|-------|
| Named Individuals | |
| With Email Addresses | |
| With Phone Numbers | |
| With Photos | |
| Cross-Site Correlations | |

### Findings by Severity

| Severity | Count |
|----------|-------|
| Critical | |
| High | |
| Medium | |
| Low/Informational | |

### Targets by Priority

| Priority | Completed / Total |
|----------|-------------------|
| P1 — Presidency | / |
| P2 — Military | / |
| P3 — Intelligence | / |
| P4 — Law Enforcement | / |
| P5 — Core Govt | / |
| P6 — State Media | / |
| P7 — State Enterprises | / |
| P8 — Regional/Local | / |
| P9 — Education | / |
| P10 — Other | / |

---

## Sections 14–19: Logs & Templates

### Section 14: Next Actions

- [ ] _(action item)_
- [ ] _(action item)_

### Section 15: Notes & Observations

_(research notes go here)_

### Section 16: WordPress Site Inventory

| Domain | Users API | Users | Hashes | Theme/Plugins |
|--------|-----------|-------|--------|---------------|
| | EXPOSED / PROTECTED | | | |

### Section 17: Gravatar Hash Master Log

| MD5 Hash | Username | Display Name | Source Domain | Cracked Email |
|----------|----------|-------------|---------------|---------------|
| | | | | |

**Cross-Site Correlations (same hash on multiple sites):**

| Hash | Sites Where Found |
|------|-------------------|
| | |

### Section 18: Critical Findings Log

| Date | Severity | Target | Finding |
|------|----------|--------|---------|
| | | | |

### Section 19: Hash Cracking Log

| Hash | Type | Status | Cracked Value | Date |
|------|------|--------|---------------|------|
| | MD5 | CRACKED / PENDING | | |

---

## Template Info

| Field | Value |
|-------|-------|
| Template Version | 2.0 |
| Last Updated | January 2026 |
| Organization | ODINT — Observatory for Digital Infrastructure and Network Transparency |
| Purpose | OSINT Security Audit & Government Accountability Documentation |

> *"We document. We archive. We hold power accountable."*
