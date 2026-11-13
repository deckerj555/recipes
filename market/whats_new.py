#!/usr/bin/env python3
"""Compare the latest Gorge Farmer Collective snapshot against earlier weeks.

Usage:  python3 market/whats_new.py [market/]  [--weeks N]

Prints four lists for the newest snapshot in the folder:
  NEW        product+vendor never seen in any earlier snapshot
  RETURNING  seen before, but absent from the last N snapshots (default 6)
  GONE       in last week's snapshot, missing this week
  SCARCE     this week's items with 3 or fewer units left on every unit size

Snapshots are market/YYYY-MM-DD.csv (date = pickup Wednesday) with columns
category, product, vendor, unit, price, remaining, sold_out, tagline.
"""
import csv
import glob
import os
import sys


def load(path):
    items = {}
    with open(path, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            key = (r["product"], r["vendor"])
            it = items.setdefault(key, {"category": r["category"], "units": [], "sold_out": r.get("sold_out") == "1"})
            rem = r.get("remaining", "")
            it["units"].append((r["unit"], r["price"], int(rem) if rem.isdigit() else None))
    return items


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    folder = args[0] if args else os.path.dirname(os.path.abspath(__file__))
    weeks = 6
    if "--weeks" in sys.argv:
        weeks = int(sys.argv[sys.argv.index("--weeks") + 1])

    files = sorted(glob.glob(os.path.join(folder, "????-??-??.csv")))
    if not files:
        sys.exit("no snapshots found in " + folder)
    latest = load(files[-1])
    earlier = [load(p) for p in files[:-1]]
    ever = set().union(*[set(e) for e in earlier]) if earlier else set()
    recent = set().union(*[set(e) for e in earlier[-weeks:]]) if earlier else set()
    last_week = set(earlier[-1]) if earlier else set()

    def show(title, keys):
        print(f"\n== {title} ({len(keys)}) ==")
        for k in sorted(keys, key=lambda k: (latest.get(k, {}).get("category", ""), k)):
            it = latest.get(k)
            if it:
                units = "; ".join(f"{u} ${p} ({'n/a' if r is None else r} left)" for u, p, r in it["units"])
                print(f"[{it['category']}] {k[0]} — {k[1]} :: {units}")
            else:
                print(f"{k[0]} — {k[1]}")

    print(f"Latest snapshot: {os.path.basename(files[-1])}  ({len(latest)} products); {len(earlier)} earlier snapshot(s)")
    if not earlier:
        print("No earlier snapshots yet, so nothing can be called new. Everything below is this week's full list.")
    show("NEW (never seen before)", [k for k in latest if k not in ever])
    show(f"RETURNING (absent for the last {weeks} snapshots)", [k for k in latest if k in ever and k not in recent])
    show("GONE since last week", [k for k in last_week if k not in latest])
    show("SCARCE (3 or fewer left on every size)",
         [k for k, it in latest.items() if it["units"] and all(r is not None and r <= 3 for _, _, r in it["units"])])


if __name__ == "__main__":
    main()
