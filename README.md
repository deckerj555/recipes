# Family Recipes

Every recipe is one Markdown file at the top level of this repo. Card photos for handwritten family recipes live in [`originals/`](originals/).

## How it's organized

**Tags.** Each recipe starts with a small front-matter block, like this:

```yaml
---
title: Sukiyaki (ski-a-ki)
from: Dad
serves: 4
tags: [family, main, beef, japanese, stovetop]
---
```

GitHub shows that block as a table at the top of the recipe. The index below groups recipes by tag; you can also search the repo for a word like `tags:` plus `beef`.

- `family` — transcribed from a handwritten card (photo in `originals/`)
- `claude` — written with Claude; `original:` links to the chat it came from
- `favorite` — a proven hit at our table

**Revisions.** Every change is a commit, so any version of a recipe can be referenced:

- *History of one recipe:* open the file on GitHub and click **History**.
- *Link to an exact version:* on the file page press `y` (or use **…→ Copy permalink**). The link includes the commit hash and never changes.
- *Name a version:* create a revision tag, e.g. `git tag sukiyaki-v2 && git push --tags`. A few are already set up as examples (see **Tags** on GitHub).

**Editing.** Edit right on GitHub (pencil icon) or locally. Write the commit message as what changed, e.g. "Sukiyaki: cut sugar to 3 tbsp".

## Recipes


| Recipe | From | Tags |
|---|---|---|
| [Bobotie](bobotie.md) |  | claude, main, beef, south-african, baked |
| [Cold Sesame Noodles](cold-sesame-noodles.md) |  | claude, main, noodles, vegetarian, asian, summer, quick |
| [Ham Bone Lentil Soup](ham-bone-lentil-soup.md) |  | claude, main, soup, pork, leftovers, slow-cooker, freezer |
| [Mild Chicken Chile Verde](mild-chicken-chile-verde.md) |  | claude, main, chicken, mexican, braise, mild, favorite |
| [Miso Glazed Turnips](miso-glazed-turnips.md) |  | claude, side, vegetarian, japanese, stovetop, quick |
| [Morel Risotto Frittata](morel-risotto-frittata.md) |  | claude, main, breakfast, vegetarian, eggs, mushrooms, leftovers |
| [Palak Paneer (Swasthi's Method)](palak-paneer.md) |  | claude, main, vegetarian, indian, stovetop |
| [Pasta alla Norma](pasta-alla-norma.md) |  | claude, main, pasta, vegetarian, italian, mild |

## By tag

- **asian** (1): [Cold Sesame Noodles](cold-sesame-noodles.md)
- **baked** (1): [Bobotie](bobotie.md)
- **beef** (1): [Bobotie](bobotie.md)
- **braise** (1): [Mild Chicken Chile Verde](mild-chicken-chile-verde.md)
- **breakfast** (1): [Morel Risotto Frittata](morel-risotto-frittata.md)
- **chicken** (1): [Mild Chicken Chile Verde](mild-chicken-chile-verde.md)
- **claude** (8): [Bobotie](bobotie.md), [Cold Sesame Noodles](cold-sesame-noodles.md), [Ham Bone Lentil Soup](ham-bone-lentil-soup.md), [Mild Chicken Chile Verde](mild-chicken-chile-verde.md), [Miso Glazed Turnips](miso-glazed-turnips.md), [Morel Risotto Frittata](morel-risotto-frittata.md), [Palak Paneer (Swasthi's Method)](palak-paneer.md), [Pasta alla Norma](pasta-alla-norma.md)
- **eggs** (1): [Morel Risotto Frittata](morel-risotto-frittata.md)
- **favorite** (1): [Mild Chicken Chile Verde](mild-chicken-chile-verde.md)
- **freezer** (1): [Ham Bone Lentil Soup](ham-bone-lentil-soup.md)
- **indian** (1): [Palak Paneer (Swasthi's Method)](palak-paneer.md)
- **italian** (1): [Pasta alla Norma](pasta-alla-norma.md)
- **japanese** (1): [Miso Glazed Turnips](miso-glazed-turnips.md)
- **leftovers** (2): [Ham Bone Lentil Soup](ham-bone-lentil-soup.md), [Morel Risotto Frittata](morel-risotto-frittata.md)
- **main** (7): [Bobotie](bobotie.md), [Cold Sesame Noodles](cold-sesame-noodles.md), [Ham Bone Lentil Soup](ham-bone-lentil-soup.md), [Mild Chicken Chile Verde](mild-chicken-chile-verde.md), [Morel Risotto Frittata](morel-risotto-frittata.md), [Palak Paneer (Swasthi's Method)](palak-paneer.md), [Pasta alla Norma](pasta-alla-norma.md)
- **mexican** (1): [Mild Chicken Chile Verde](mild-chicken-chile-verde.md)
- **mild** (2): [Mild Chicken Chile Verde](mild-chicken-chile-verde.md), [Pasta alla Norma](pasta-alla-norma.md)
- **mushrooms** (1): [Morel Risotto Frittata](morel-risotto-frittata.md)
- **noodles** (1): [Cold Sesame Noodles](cold-sesame-noodles.md)
- **pasta** (1): [Pasta alla Norma](pasta-alla-norma.md)
- **pork** (1): [Ham Bone Lentil Soup](ham-bone-lentil-soup.md)
- **quick** (2): [Cold Sesame Noodles](cold-sesame-noodles.md), [Miso Glazed Turnips](miso-glazed-turnips.md)
- **side** (1): [Miso Glazed Turnips](miso-glazed-turnips.md)
- **slow-cooker** (1): [Ham Bone Lentil Soup](ham-bone-lentil-soup.md)
- **soup** (1): [Ham Bone Lentil Soup](ham-bone-lentil-soup.md)
- **south-african** (1): [Bobotie](bobotie.md)
- **stovetop** (2): [Miso Glazed Turnips](miso-glazed-turnips.md), [Palak Paneer (Swasthi's Method)](palak-paneer.md)
- **summer** (1): [Cold Sesame Noodles](cold-sesame-noodles.md)
- **vegetarian** (5): [Cold Sesame Noodles](cold-sesame-noodles.md), [Miso Glazed Turnips](miso-glazed-turnips.md), [Morel Risotto Frittata](morel-risotto-frittata.md), [Palak Paneer (Swasthi's Method)](palak-paneer.md), [Pasta alla Norma](pasta-alla-norma.md)
