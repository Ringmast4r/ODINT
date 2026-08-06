import sqlite3
from pathlib import Path

con = sqlite3.connect(Path(__file__).resolve().parent.parent / "odint_checklist.db")
con.row_factory = sqlite3.Row

print("=== COLLECTION sections ===")
for r in con.execute(
    """
    select s.name, count(i.id) c from sections s
    join documents d on d.id=s.document_id
    join items i on i.section_id=s.id
    where d.key='collection' group by s.id order by s.sort_order
    """
):
    print(f"{r['c']:4d}  {r['name']}")

print("\n=== MISSION sections ===")
for r in con.execute(
    """
    select s.name, count(i.id) c from sections s
    join documents d on d.id=s.document_id
    join items i on i.section_id=s.id
    where d.key='osint-mission' group by s.id order by s.sort_order
    """
):
    print(f"{r['c']:4d}  {r['name'][:75]}")

blob = " ".join(
    r[0].lower()
    for r in con.execute(
        """
        select i.name||' '||coalesce(i.detail,'') from items i
        join sections s on s.id=i.section_id
        join documents d on d.id=s.document_id
        where d.key='collection'
        """
    )
)
mblob = " ".join(
    r[0].lower()
    for r in con.execute(
        """
        select i.name||' '||coalesce(i.detail,'') from items i
        join sections s on s.id=i.section_id
        join documents d on d.id=s.document_id
        where d.key='osint-mission'
        """
    )
)

keywords = [
    "arcgis",
    "geoserver",
    "wms",
    "wfs",
    "s3",
    "bucket",
    "azure blob",
    "gcs",
    "google cloud storage",
    "shodan",
    "censys",
    "fofa",
    "binaryedge",
    "certificate transparency",
    "crt.sh",
    "wayback",
    "archive.org",
    "pastebin",
    "github",
    "gitlab",
    "bitbucket",
    "subdomain",
    "axfr",
    "firebase",
    "kubernetes",
    "docker",
    "jenkins",
    "gitlab ci",
    "github actions",
    "terraform",
    "confluence",
    "jira",
    "trello",
    "notion",
    "sharepoint",
    "elasticsearch",
    "mongodb",
    "redis",
    "postgres",
    "mysql",
    "graphql",
    "swagger",
    ".git",
    ".env",
    "source map",
    "gravatar",
    "exif",
    "gps",
    "spf",
    "dmarc",
    "dkim",
    "jupyter",
    "snmp",
    "smb",
    "nfs",
    "rsync",
    "apk",
    "mobile",
    "huggingface",
    "kaggle",
    "telegram",
    "breach",
    "have i been pwned",
    "ipfs",
    "whois",
    "rdap",
    "asn",
    "cdn",
    "cloudflare",
    "wordpress",
    "drupal",
    "joomla",
    "owa",
    "exchange",
    "vpn",
    "jwt",
    "oauth",
    "webhook",
    "supply chain",
    "npm",
    "pypi",
    "docker hub",
    "ecr",
    "default credential",
    "phishing",
    "dark web",
    "tor",
    "legal",
    "disclosure",
    "chain of custody",
    "sourcelist",
    "sha256",
]

print("\n=== Keyword coverage (Y = present in names/details) ===")
print(f"{'keyword':32} {'collection':12} {'mission':10}")
missing_c = []
missing_both = []
for k in keywords:
    c = k in blob
    m = k in mblob
    print(f"{k:32} {'Y' if c else 'n':12} {'Y' if m else 'n':10}")
    if not c:
        missing_c.append(k)
    if not c and not m:
        missing_both.append(k)

print("\nMissing from Collection only:", ", ".join(missing_c))
print("Missing from BOTH:", ", ".join(missing_both))
print(
    "\nTotals:",
    con.execute(
        "select d.key, count(i.id) from documents d join sections s on s.document_id=d.id join items i on i.section_id=s.id group by d.key"
    ).fetchall(),
)
