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
| [Ham Bone Lentil Soup](ham-bone-lentil-soup.md) |  | claude, main, soup, pork, leftovers, slow-cooker, freezer |
| [Miso Glazed Turnips](miso-glazed-turnips.md) |  | claude, side, vegetarian, japanese, stovetop, quick |
| [Morel Risotto Frittata](morel-risotto-frittata.md) |  | claude, main, breakfast, vegetarian, eggs, mushrooms, leftovers |
| [Palak Paneer (Swasthi's Method)](palak-paneer.md) |  | claude, main, vegetarian, indian, stovetop |

## By tag

- **baked** (1): [Bobotie](bobotie.md)
- **beef** (1): [Bobotie](bobotie.md)
- **breakfast** (1): [Morel Risotto Frittata](morel-risotto-frittata.md)
- **claude** (5): [Bobotie](bobotie.md), [Ham Bone Lentil Soup](ham-bone-lentil-soup.md), [Miso Glazed Turnips](miso-glazed-turnips.md), [Morel Risotto Frittata](morel-risotto-frittata.md), [Palak Paneer (Swasthi's Method)](palak-paneer.md)
- **eggs** (1): [Morel Risotto Frittata](morel-risotto-frittata.md)
- **freezer** (1): [Ham Bone Lentil Soup](ham-bone-lentil-soup.md)
- **indian** (1): [Palak Paneer (Swasthi's Method)](palak-paneer.md)
- **japanese** (1): [Miso Glazed Turnips](miso-glazed-turnips.md)
- **leftovers** (2): [Ham Bone Lentil Soup](ham-bone-lentil-soup.md), [Morel Risotto Frittata](morel-risotto-frittata.md)
- **main** (4): [Bobotie](bobotie.md), [Ham Bone Lentil Soup](ham-bone-lentil-soup.md), [Morel Risotto Frittata](morel-risotto-frittata.md), [Palak Paneer (Swasthi's Method)](palak-paneer.md)
- **mushrooms** (1): [Morel Risotto Frittata](morel-risotto-frittata.md)
- **pork** (1): [Ham Bone Lentil Soup](ham-bone-lentil-soup.md)
- **quick** (1): [Miso Glazed Turnips](miso-glazed-turnips.md)
- **side** (1): [Miso Glazed Turnips](miso-glazed-turnips.md)
- **slow-cooker** (1): [Ham Bone Lentil Soup](ham-bone-lentil-soup.md)
- **soup** (1): [Ham Bone Lentil Soup](ham-bone-lentil-soup.md)
- **south-african** (1): [Bobotie](bobotie.md)
- **stovetop** (2): [Miso Glazed Turnips](miso-glazed-turnips.md), [Palak Paneer (Swasthi's Method)](palak-paneer.md)
- **vegetarian** (3): [Miso Glazed Turnips](miso-glazed-turnips.md), [Morel Risotto Frittata](morel-risotto-frittata.md), [Palak Paneer (Swasthi's Method)](palak-paneer.md)
