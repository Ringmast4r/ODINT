# ODINT Checklists

Reference checklists for ODINT OSINT work. Part of the main [ODINT](https://github.com/Ringmast4r/ODINT) repo.

**Three lists (kept separate):**

| Document | Items | Role |
|----------|------:|------|
| **Collection Checklist** | 1,265 | What to collect on a target site (numbered field inventory) |
| **OSINT Mission Set** | ~1,742 | How to run the op (Mission Objectives + unique Mission MD items, deduped) |
| **Country Coverage** | 264 | Cyber Recon Tour country/region tracker |

## Quick start

Open the offline viewer in a browser:

```text
CHECKLISTS/viewer.html
```

Rebuild DB + viewer from sources:

```bash
cd CHECKLISTS
python scripts/import_all.py
```

## Layout

```text
CHECKLISTS/
  viewer.html                 # offline searchable UI
  odint_checklist.db          # SQLite for the viewer
  ODINT-Collection-Checklist.md
  ODINT MISSION OBJECTIVES.txt
  scripts/import_all.py       # rebuild
  sources/                    # imported source copies
```

Related copies also live under `CYBER RECON TOUR/MISC/` (mission objectives, collection checklist).

## Methodology

OSINT-only: passive reconnaissance of publicly accessible data. Document and archive — do not exploit.
