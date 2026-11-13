# Market snapshots

One CSV per pickup week of the Gorge Farmer Collective catalog, written by the Thursday meal-plan task so it can tell what's new at the market. Not recipes; the recipe index ignores this folder.

- Filename is the pickup Wednesday: `2026-11-18.csv`.
- Columns: `category, product, vendor, unit, price, remaining, sold_out, tagline`. One row per unit size.
- Excluded categories: Donations/Merch, Flowers, Artisan Farm Goods, Microgreens, Coffee & Tea.
- `python3 market/whats_new.py` lists what's new, returning (absent six-plus weeks), gone since last week, and scarce.

A product counts as **new** when its product-plus-vendor pair has never appeared in an earlier snapshot. History starts 2026-11-18.
