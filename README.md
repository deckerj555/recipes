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
| [Bulgogi Marinade](bulgogi-marinade.md) |  | claude, sauce, beef, korean, make-ahead, mild, favorite |
| [Bulgogi Night with Banchan](bulgogi-night-with-banchan.md) |  | claude, main, beef, korean, grilled, mild, favorite |
| [Cold Sesame Noodles](cold-sesame-noodles.md) |  | claude, main, noodles, vegetarian, asian, summer, quick |
| [Creste di Gallo with Nettle-Hazelnut Pesto, Brussels Sprouts & Carrots](creste-di-gallo-nettle-hazelnut-pesto.md) |  | claude, main, pasta, vegetarian, italian, roasted |
| [Flat Iron Steak with Chanterelle Pan Sauce](flat-iron-chanterelle-pan-sauce.md) |  | claude, main, beef, steak, mushrooms, stovetop |
| [Ham Bone Lentil Soup](ham-bone-lentil-soup.md) |  | claude, main, soup, pork, leftovers, slow-cooker, freezer |
| [Italian-Herb Pork Chops with Sautéed Apples and Roasted Delicata](italian-herb-pork-chops.md) |  | claude, main, pork, roasted, one-pan, fall |
| [Mild Chicken Chile Verde](mild-chicken-chile-verde.md) |  | claude, main, chicken, mexican, braise, mild, favorite |
| [Mild Poulet Basquaise](mild-poulet-basquaise.md) |  | claude, main, chicken, french, braise, mild |
| [Miso Glazed Turnips](miso-glazed-turnips.md) |  | claude, side, vegetarian, japanese, stovetop, quick |
| [Morel Risotto Frittata](morel-risotto-frittata.md) |  | claude, main, breakfast, vegetarian, eggs, mushrooms, leftovers |
| [Napa Cabbage Slaw with Honey-Cider Vinaigrette](napa-cabbage-slaw.md) |  | claude, side, salad, vegetarian, no-cook |
| [Palak Paneer (Swasthi's Method)](palak-paneer.md) |  | claude, main, vegetarian, indian, stovetop |
| [Pasta alla Norma](pasta-alla-norma.md) |  | claude, main, pasta, vegetarian, italian, mild |
| [Petrale Sole Meunière with Glazed Salad Turnips](petrale-sole-meuniere-glazed-turnips.md) |  | claude, main, fish, french, stovetop, quick |
| [Ricotta Gnocchi with Brown Butter, Pepitas & Basil](ricotta-gnocchi.md) |  | claude, main, pasta, vegetarian, italian, make-ahead, freezer |
| [Seared Rockfish over Corn & Okra Maque Choux](rockfish-maque-choux.md) |  | claude, main, fish, cajun, stovetop, mild, favorite |

## By tag

- **asian** (1): [Cold Sesame Noodles](cold-sesame-noodles.md)
- **baked** (1): [Bobotie](bobotie.md)
- **beef** (4): [Bobotie](bobotie.md), [Bulgogi Marinade](bulgogi-marinade.md), [Bulgogi Night with Banchan](bulgogi-night-with-banchan.md), [Flat Iron Steak with Chanterelle Pan Sauce](flat-iron-chanterelle-pan-sauce.md)
- **braise** (2): [Mild Chicken Chile Verde](mild-chicken-chile-verde.md), [Mild Poulet Basquaise](mild-poulet-basquaise.md)
- **breakfast** (1): [Morel Risotto Frittata](morel-risotto-frittata.md)
- **cajun** (1): [Seared Rockfish over Corn & Okra Maque Choux](rockfish-maque-choux.md)
- **chicken** (2): [Mild Chicken Chile Verde](mild-chicken-chile-verde.md), [Mild Poulet Basquaise](mild-poulet-basquaise.md)
- **claude** (18): [Bobotie](bobotie.md), [Bulgogi Marinade](bulgogi-marinade.md), [Bulgogi Night with Banchan](bulgogi-night-with-banchan.md), [Cold Sesame Noodles](cold-sesame-noodles.md), [Creste di Gallo with Nettle-Hazelnut Pesto, Brussels Sprouts & Carrots](creste-di-gallo-nettle-hazelnut-pesto.md), [Flat Iron Steak with Chanterelle Pan Sauce](flat-iron-chanterelle-pan-sauce.md), [Ham Bone Lentil Soup](ham-bone-lentil-soup.md), [Italian-Herb Pork Chops with Sautéed Apples and Roasted Delicata](italian-herb-pork-chops.md), [Mild Chicken Chile Verde](mild-chicken-chile-verde.md), [Mild Poulet Basquaise](mild-poulet-basquaise.md), [Miso Glazed Turnips](miso-glazed-turnips.md), [Morel Risotto Frittata](morel-risotto-frittata.md), [Napa Cabbage Slaw with Honey-Cider Vinaigrette](napa-cabbage-slaw.md), [Palak Paneer (Swasthi's Method)](palak-paneer.md), [Pasta alla Norma](pasta-alla-norma.md), [Petrale Sole Meunière with Glazed Salad Turnips](petrale-sole-meuniere-glazed-turnips.md), [Ricotta Gnocchi with Brown Butter, Pepitas & Basil](ricotta-gnocchi.md), [Seared Rockfish over Corn & Okra Maque Choux](rockfish-maque-choux.md)
- **eggs** (1): [Morel Risotto Frittata](morel-risotto-frittata.md)
- **fall** (1): [Italian-Herb Pork Chops with Sautéed Apples and Roasted Delicata](italian-herb-pork-chops.md)
- **favorite** (4): [Bulgogi Marinade](bulgogi-marinade.md), [Bulgogi Night with Banchan](bulgogi-night-with-banchan.md), [Mild Chicken Chile Verde](mild-chicken-chile-verde.md), [Seared Rockfish over Corn & Okra Maque Choux](rockfish-maque-choux.md)
- **fish** (2): [Petrale Sole Meunière with Glazed Salad Turnips](petrale-sole-meuniere-glazed-turnips.md), [Seared Rockfish over Corn & Okra Maque Choux](rockfish-maque-choux.md)
- **freezer** (2): [Ham Bone Lentil Soup](ham-bone-lentil-soup.md), [Ricotta Gnocchi with Brown Butter, Pepitas & Basil](ricotta-gnocchi.md)
- **french** (2): [Mild Poulet Basquaise](mild-poulet-basquaise.md), [Petrale Sole Meunière with Glazed Salad Turnips](petrale-sole-meuniere-glazed-turnips.md)
- **grilled** (1): [Bulgogi Night with Banchan](bulgogi-night-with-banchan.md)
- **indian** (1): [Palak Paneer (Swasthi's Method)](palak-paneer.md)
- **italian** (3): [Creste di Gallo with Nettle-Hazelnut Pesto, Brussels Sprouts & Carrots](creste-di-gallo-nettle-hazelnut-pesto.md), [Pasta alla Norma](pasta-alla-norma.md), [Ricotta Gnocchi with Brown Butter, Pepitas & Basil](ricotta-gnocchi.md)
- **japanese** (1): [Miso Glazed Turnips](miso-glazed-turnips.md)
- **korean** (2): [Bulgogi Marinade](bulgogi-marinade.md), [Bulgogi Night with Banchan](bulgogi-night-with-banchan.md)
- **leftovers** (2): [Ham Bone Lentil Soup](ham-bone-lentil-soup.md), [Morel Risotto Frittata](morel-risotto-frittata.md)
- **main** (15): [Bobotie](bobotie.md), [Bulgogi Night with Banchan](bulgogi-night-with-banchan.md), [Cold Sesame Noodles](cold-sesame-noodles.md), [Creste di Gallo with Nettle-Hazelnut Pesto, Brussels Sprouts & Carrots](creste-di-gallo-nettle-hazelnut-pesto.md), [Flat Iron Steak with Chanterelle Pan Sauce](flat-iron-chanterelle-pan-sauce.md), [Ham Bone Lentil Soup](ham-bone-lentil-soup.md), [Italian-Herb Pork Chops with Sautéed Apples and Roasted Delicata](italian-herb-pork-chops.md), [Mild Chicken Chile Verde](mild-chicken-chile-verde.md), [Mild Poulet Basquaise](mild-poulet-basquaise.md), [Morel Risotto Frittata](morel-risotto-frittata.md), [Palak Paneer (Swasthi's Method)](palak-paneer.md), [Pasta alla Norma](pasta-alla-norma.md), [Petrale Sole Meunière with Glazed Salad Turnips](petrale-sole-meuniere-glazed-turnips.md), [Ricotta Gnocchi with Brown Butter, Pepitas & Basil](ricotta-gnocchi.md), [Seared Rockfish over Corn & Okra Maque Choux](rockfish-maque-choux.md)
- **make-ahead** (2): [Bulgogi Marinade](bulgogi-marinade.md), [Ricotta Gnocchi with Brown Butter, Pepitas & Basil](ricotta-gnocchi.md)
- **mexican** (1): [Mild Chicken Chile Verde](mild-chicken-chile-verde.md)
- **mild** (6): [Bulgogi Marinade](bulgogi-marinade.md), [Bulgogi Night with Banchan](bulgogi-night-with-banchan.md), [Mild Chicken Chile Verde](mild-chicken-chile-verde.md), [Mild Poulet Basquaise](mild-poulet-basquaise.md), [Pasta alla Norma](pasta-alla-norma.md), [Seared Rockfish over Corn & Okra Maque Choux](rockfish-maque-choux.md)
- **mushrooms** (2): [Flat Iron Steak with Chanterelle Pan Sauce](flat-iron-chanterelle-pan-sauce.md), [Morel Risotto Frittata](morel-risotto-frittata.md)
- **no-cook** (1): [Napa Cabbage Slaw with Honey-Cider Vinaigrette](napa-cabbage-slaw.md)
- **noodles** (1): [Cold Sesame Noodles](cold-sesame-noodles.md)
- **one-pan** (1): [Italian-Herb Pork Chops with Sautéed Apples and Roasted Delicata](italian-herb-pork-chops.md)
- **pasta** (3): [Creste di Gallo with Nettle-Hazelnut Pesto, Brussels Sprouts & Carrots](creste-di-gallo-nettle-hazelnut-pesto.md), [Pasta alla Norma](pasta-alla-norma.md), [Ricotta Gnocchi with Brown Butter, Pepitas & Basil](ricotta-gnocchi.md)
- **pork** (2): [Ham Bone Lentil Soup](ham-bone-lentil-soup.md), [Italian-Herb Pork Chops with Sautéed Apples and Roasted Delicata](italian-herb-pork-chops.md)
- **quick** (3): [Cold Sesame Noodles](cold-sesame-noodles.md), [Miso Glazed Turnips](miso-glazed-turnips.md), [Petrale Sole Meunière with Glazed Salad Turnips](petrale-sole-meuniere-glazed-turnips.md)
- **roasted** (2): [Creste di Gallo with Nettle-Hazelnut Pesto, Brussels Sprouts & Carrots](creste-di-gallo-nettle-hazelnut-pesto.md), [Italian-Herb Pork Chops with Sautéed Apples and Roasted Delicata](italian-herb-pork-chops.md)
- **salad** (1): [Napa Cabbage Slaw with Honey-Cider Vinaigrette](napa-cabbage-slaw.md)
- **sauce** (1): [Bulgogi Marinade](bulgogi-marinade.md)
- **side** (2): [Miso Glazed Turnips](miso-glazed-turnips.md), [Napa Cabbage Slaw with Honey-Cider Vinaigrette](napa-cabbage-slaw.md)
- **slow-cooker** (1): [Ham Bone Lentil Soup](ham-bone-lentil-soup.md)
- **soup** (1): [Ham Bone Lentil Soup](ham-bone-lentil-soup.md)
- **south-african** (1): [Bobotie](bobotie.md)
- **steak** (1): [Flat Iron Steak with Chanterelle Pan Sauce](flat-iron-chanterelle-pan-sauce.md)
- **stovetop** (5): [Flat Iron Steak with Chanterelle Pan Sauce](flat-iron-chanterelle-pan-sauce.md), [Miso Glazed Turnips](miso-glazed-turnips.md), [Palak Paneer (Swasthi's Method)](palak-paneer.md), [Petrale Sole Meunière with Glazed Salad Turnips](petrale-sole-meuniere-glazed-turnips.md), [Seared Rockfish over Corn & Okra Maque Choux](rockfish-maque-choux.md)
- **summer** (1): [Cold Sesame Noodles](cold-sesame-noodles.md)
- **vegetarian** (8): [Cold Sesame Noodles](cold-sesame-noodles.md), [Creste di Gallo with Nettle-Hazelnut Pesto, Brussels Sprouts & Carrots](creste-di-gallo-nettle-hazelnut-pesto.md), [Miso Glazed Turnips](miso-glazed-turnips.md), [Morel Risotto Frittata](morel-risotto-frittata.md), [Napa Cabbage Slaw with Honey-Cider Vinaigrette](napa-cabbage-slaw.md), [Palak Paneer (Swasthi's Method)](palak-paneer.md), [Pasta alla Norma](pasta-alla-norma.md), [Ricotta Gnocchi with Brown Butter, Pepitas & Basil](ricotta-gnocchi.md)
