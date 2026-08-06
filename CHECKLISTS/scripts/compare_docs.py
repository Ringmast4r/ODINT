import sqlite3
from pathlib import Path

con = sqlite3.connect(Path(__file__).resolve().parent.parent / "odint_checklist.db")
con.row_factory = sqlite3.Row

docs = list(con.execute("SELECT id, key, name, description FROM documents ORDER BY sort_order"))
for d in docs:
    n = con.execute(
        """SELECT COUNT(*) FROM items i
           JOIN sections s ON s.id=i.section_id WHERE s.document_id=?""",
        (d["id"],),
    ).fetchone()[0]
    secs = list(
        con.execute(
            """SELECT name,
                      (SELECT COUNT(*) FROM items i WHERE i.section_id=s.id) c
               FROM sections s WHERE document_id=? ORDER BY sort_order""",
            (d["id"],),
        )
    )
    print("=" * 70)
    print(f"{d['name']} | {n} items | key={d['key']}")
    print(d["description"])
    print(f"sections: {len(secs)}")
    for s in secs:
        print(f"  {s['c']:4d}  {s['name'][:75]}")
    samples = con.execute(
        """SELECT i.name FROM items i JOIN sections s ON s.id=i.section_id
           WHERE s.document_id=? ORDER BY i.sort_order LIMIT 6""",
        (d["id"],),
    )
    print("sample items:")
    for r in samples:
        print("   -", r[0][:95])


def names(doc_id):
    return {
        r[0].strip().lower()
        for r in con.execute(
            """SELECT i.name FROM items i
               JOIN sections s ON s.id=i.section_id WHERE s.document_id=?""",
            (doc_id,),
        )
    }


sets = {d["key"]: names(d["id"]) for d in docs}
print("=" * 70)
print("OVERLAP (exact item name match, case-insensitive)")
keys = list(sets)
for i, a in enumerate(keys):
    for b in keys[i + 1 :]:
        inter = sets[a] & sets[b]
        print(
            f"  {a} ∩ {b}: {len(inter)} exact overlaps "
            f"(sizes {len(sets[a])} / {len(sets[b])})"
        )
        if inter and len(inter) <= 12:
            for x in sorted(inter)[:12]:
                print(f"      · {x[:80]}")
        elif inter:
            for x in sorted(inter)[:8]:
                print(f"      · {x[:80]}")
            print(f"      … +{len(inter)-8} more")
