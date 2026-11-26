# Family Recipes

Every recipe is one Markdown file at the top level of this repo. Card photos for handwritten family recipes live in [`originals/`](originals/). Recipes we've retired live in [`archive/`](archive/) and are listed at the bottom.

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
- *Name a version:* create a revision tag, e.g. `git tag sukiyaki-v2 && git push --tags`. On GitHub, tags are created from **Releases → Draft a new release → Choose a tag**, pointing at the commit you want.

**Editing.** Edit right on GitHub (pencil icon) or locally. Write the commit message as what changed, e.g. "Sukiyaki: cut sugar to 3 tbsp".

## Recipes


| Recipe | From | Tags |
|---|---|---|
| [Beef and Cabbage Stir-Fry](beef-and-cabbage-stir-fry.md) |  | claude, main, beef, chinese, stir-fry, quick, mild |
| [Beef Bulgogi](beef-bulgogi.md) |  | claude, martha-stewart, main, beef, korean, stir-fry |
| [Beef Teriyaki Stir-Fry](beef-teriyaki-stir-fry.md) |  | claude, main, beef, japanese, stir-fry, quick, mild |
| [Bulgogi Marinade](bulgogi-marinade.md) |  | claude, sauce, beef, korean, make-ahead, mild, favorite |
| [Bulgogi Night with Banchan](bulgogi-night-with-banchan.md) |  | claude, main, beef, korean, grilled, mild, favorite |
| [Butternut Squash Bake](butternut-squash-bake.md) | Bob | family, side, vegetarian, baked, holiday |
| [Cold Sesame Noodles](cold-sesame-noodles.md) |  | claude, main, noodles, vegetarian, asian, summer, quick |
| [Dream Biscuits (ATK Easiest-Ever Biscuits)](dream-biscuits.md) |  | claude, atk, side, baked, quick, mild |
| [Flat Iron Steak with Chanterelle Pan Sauce](flat-iron-chanterelle-pan-sauce.md) |  | claude, main, beef, steak, mushrooms, stovetop |
| [Ham Bone Lentil Soup](ham-bone-lentil-soup.md) |  | claude, main, soup, pork, leftovers, slow-cooker, freezer |
| [Italian Herb Sausages, Garlicky Kale & Brown Sugar Acorn Squash](sausages-kale-acorn-squash.md) |  | claude, main, pork, sausage, roasted, fall |
| [Italian-Herb Pork Chops with Sautéed Apples and Roasted Delicata](italian-herb-pork-chops.md) |  | claude, main, pork, roasted, one-pan, fall |
| [Kenji's Ski House Soup](ski-house-soup.md) |  | claude, kenji, main, soup, vegetarian, stovetop, mild |
| [Kenji's Weeknight Mushroom Pasta](kenji-mushroom-pasta.md) |  | claude, kenji, main, pasta, mushrooms, italian, stovetop, quick, mild |
| [Latkes with Jonagold Applesauce and Fried Eggs](latkes.md) |  | claude, main, eggs, vegetarian, stovetop, mild |
| [Mary Ann's Chili](mary-anns-chili.md) | Mary Ann | family, main, beef, stovetop, quick |
| [Mild Chicken Chile Verde](mild-chicken-chile-verde.md) |  | claude, main, chicken, mexican, braise, mild, favorite |
| [Mild Japanese Pork & Kabocha Curry](japanese-pork-curry.md) |  | claude, kenji, main, pork, japanese, stovetop, mild |
| [Mild Poulet Basquaise](mild-poulet-basquaise.md) |  | claude, main, chicken, french, braise, mild |
| [Miso Glazed Turnips](miso-glazed-turnips.md) |  | claude, side, vegetarian, japanese, stovetop, quick |
| [Modern Sukiyaki](sukiyaki-modern.md) |  | claude, main, beef, japanese, stovetop, mild |
| [Morel Risotto Frittata](morel-risotto-frittata.md) |  | claude, main, breakfast, vegetarian, eggs, mushrooms, leftovers |
| [Napa Cabbage Slaw with Honey-Cider Vinaigrette](napa-cabbage-slaw.md) |  | claude, side, salad, vegetarian, no-cook |
| [Paella](paella.md) | Cook's Illustrated | family, cooks-illustrated, main, chicken, sausage, seafood, spanish, holiday |
| [Palak Paneer (Swasthi's Method)](palak-paneer.md) |  | claude, main, vegetarian, indian, stovetop |
| [Paprikash](paprikash.md) |  | claude, martha-stewart, main, chicken, hungarian, stovetop, quick, mild |
| [Petrale Sole Meunière with Glazed Salad Turnips](petrale-sole-meuniere-glazed-turnips.md) |  | claude, main, fish, french, stovetop, quick |
| [Petrale Sole Meunière with Roasted Brussels Sprouts](petrale-sole-brussels-sprouts.md) |  | claude, main, fish, french, roasted, quick |
| [Poached Quince with Italian Sausage & Roasted Brussels Sprouts](poached-quince-sausage-brussels.md) |  | claude, main, pork, sausage, roasted, fall, mild, make-ahead |
| [Reverse-Seared Pork Chops with Cranberry-Apple Chutney](pork-chops-cranberry-chutney.md) |  | claude, main, pork, roasted, stovetop, fall, mild, make-ahead |
| [Ricotta Gnocchi with Brown Butter, Pepitas & Basil](ricotta-gnocchi.md) |  | claude, main, pasta, vegetarian, italian, make-ahead, freezer |
| [RJS Stew with Dumplings](rjs-stew.md) | RJS | family, main, beef, stovetop |
| [Seared Rockfish over Corn & Okra Maque Choux](rockfish-maque-choux.md) |  | claude, main, fish, cajun, stovetop, mild, favorite |
| [Seattle-Style Teriyaki Sauce](seattle-style-teriyaki-sauce.md) |  | claude, kenji, sauce, japanese, make-ahead, mild |
| [Shio Koji Flank Steak with Honey-Roasted Carrots](shio-koji-flank-steak.md) |  | claude, main, beef, steak, japanese, stovetop, roasted, mild, make-ahead |
| [Shrimp Jambalaya](shrimp-jambalaya.md) |  | claude, martha-stewart, main, sausage, seafood, cajun, stovetop |
| [Sukiyaki (ski-a-ki)](sukiyaki.md) | Dad | family, main, beef, japanese, stovetop |
| [Tomato and Egg over Rice](tomato-and-egg-over-rice.md) |  | claude, main, eggs, vegetarian, chinese, stovetop, quick, mild |

## By tag

- **asian** (1): [Cold Sesame Noodles](cold-sesame-noodles.md)
- **atk** (1): [Dream Biscuits (ATK Easiest-Ever Biscuits)](dream-biscuits.md)
- **baked** (2): [Butternut Squash Bake](butternut-squash-bake.md), [Dream Biscuits (ATK Easiest-Ever Biscuits)](dream-biscuits.md)
- **beef** (11): [Beef and Cabbage Stir-Fry](beef-and-cabbage-stir-fry.md), [Beef Bulgogi](beef-bulgogi.md), [Beef Teriyaki Stir-Fry](beef-teriyaki-stir-fry.md), [Bulgogi Marinade](bulgogi-marinade.md), [Bulgogi Night with Banchan](bulgogi-night-with-banchan.md), [Flat Iron Steak with Chanterelle Pan Sauce](flat-iron-chanterelle-pan-sauce.md), [Mary Ann's Chili](mary-anns-chili.md), [Modern Sukiyaki](sukiyaki-modern.md), [RJS Stew with Dumplings](rjs-stew.md), [Shio Koji Flank Steak with Honey-Roasted Carrots](shio-koji-flank-steak.md), [Sukiyaki (ski-a-ki)](sukiyaki.md)
- **braise** (2): [Mild Chicken Chile Verde](mild-chicken-chile-verde.md), [Mild Poulet Basquaise](mild-poulet-basquaise.md)
- **breakfast** (1): [Morel Risotto Frittata](morel-risotto-frittata.md)
- **cajun** (2): [Seared Rockfish over Corn & Okra Maque Choux](rockfish-maque-choux.md), [Shrimp Jambalaya](shrimp-jambalaya.md)
- **chicken** (4): [Mild Chicken Chile Verde](mild-chicken-chile-verde.md), [Mild Poulet Basquaise](mild-poulet-basquaise.md), [Paella](paella.md), [Paprikash](paprikash.md)
- **chinese** (2): [Beef and Cabbage Stir-Fry](beef-and-cabbage-stir-fry.md), [Tomato and Egg over Rice](tomato-and-egg-over-rice.md)
- **claude** (31): [Beef and Cabbage Stir-Fry](beef-and-cabbage-stir-fry.md), [Beef Bulgogi](beef-bulgogi.md), [Beef Teriyaki Stir-Fry](beef-teriyaki-stir-fry.md), [Bulgogi Marinade](bulgogi-marinade.md), [Bulgogi Night with Banchan](bulgogi-night-with-banchan.md), [Cold Sesame Noodles](cold-sesame-noodles.md), [Dream Biscuits (ATK Easiest-Ever Biscuits)](dream-biscuits.md), [Flat Iron Steak with Chanterelle Pan Sauce](flat-iron-chanterelle-pan-sauce.md), [Ham Bone Lentil Soup](ham-bone-lentil-soup.md), [Italian Herb Sausages, Garlicky Kale & Brown Sugar Acorn Squash](sausages-kale-acorn-squash.md), [Italian-Herb Pork Chops with Sautéed Apples and Roasted Delicata](italian-herb-pork-chops.md), [Kenji's Ski House Soup](ski-house-soup.md), [Kenji's Weeknight Mushroom Pasta](kenji-mushroom-pasta.md), [Mild Chicken Chile Verde](mild-chicken-chile-verde.md), [Mild Japanese Pork & Kabocha Curry](japanese-pork-curry.md), [Mild Poulet Basquaise](mild-poulet-basquaise.md), [Miso Glazed Turnips](miso-glazed-turnips.md), [Modern Sukiyaki](sukiyaki-modern.md), [Morel Risotto Frittata](morel-risotto-frittata.md), [Napa Cabbage Slaw with Honey-Cider Vinaigrette](napa-cabbage-slaw.md), [Palak Paneer (Swasthi's Method)](palak-paneer.md), [Paprikash](paprikash.md), [Petrale Sole Meunière with Glazed Salad Turnips](petrale-sole-meuniere-glazed-turnips.md), [Petrale Sole Meunière with Roasted Brussels Sprouts](petrale-sole-brussels-sprouts.md), [Poached Quince with Italian Sausage & Roasted Brussels Sprouts](poached-quince-sausage-brussels.md), [Ricotta Gnocchi with Brown Butter, Pepitas & Basil](ricotta-gnocchi.md), [Seared Rockfish over Corn & Okra Maque Choux](rockfish-maque-choux.md), [Seattle-Style Teriyaki Sauce](seattle-style-teriyaki-sauce.md), [Shio Koji Flank Steak with Honey-Roasted Carrots](shio-koji-flank-steak.md), [Shrimp Jambalaya](shrimp-jambalaya.md), [Tomato and Egg over Rice](tomato-and-egg-over-rice.md)
- **cooks-illustrated** (1): [Paella](paella.md)
- **eggs** (2): [Morel Risotto Frittata](morel-risotto-frittata.md), [Tomato and Egg over Rice](tomato-and-egg-over-rice.md)
- **fall** (3): [Italian Herb Sausages, Garlicky Kale & Brown Sugar Acorn Squash](sausages-kale-acorn-squash.md), [Italian-Herb Pork Chops with Sautéed Apples and Roasted Delicata](italian-herb-pork-chops.md), [Poached Quince with Italian Sausage & Roasted Brussels Sprouts](poached-quince-sausage-brussels.md)
- **family** (5): [Butternut Squash Bake](butternut-squash-bake.md), [Mary Ann's Chili](mary-anns-chili.md), [Paella](paella.md), [RJS Stew with Dumplings](rjs-stew.md), [Sukiyaki (ski-a-ki)](sukiyaki.md)
- **favorite** (4): [Bulgogi Marinade](bulgogi-marinade.md), [Bulgogi Night with Banchan](bulgogi-night-with-banchan.md), [Mild Chicken Chile Verde](mild-chicken-chile-verde.md), [Seared Rockfish over Corn & Okra Maque Choux](rockfish-maque-choux.md)
- **fish** (3): [Petrale Sole Meunière with Glazed Salad Turnips](petrale-sole-meuniere-glazed-turnips.md), [Petrale Sole Meunière with Roasted Brussels Sprouts](petrale-sole-brussels-sprouts.md), [Seared Rockfish over Corn & Okra Maque Choux](rockfish-maque-choux.md)
- **freezer** (2): [Ham Bone Lentil Soup](ham-bone-lentil-soup.md), [Ricotta Gnocchi with Brown Butter, Pepitas & Basil](ricotta-gnocchi.md)
- **french** (3): [Mild Poulet Basquaise](mild-poulet-basquaise.md), [Petrale Sole Meunière with Glazed Salad Turnips](petrale-sole-meuniere-glazed-turnips.md), [Petrale Sole Meunière with Roasted Brussels Sprouts](petrale-sole-brussels-sprouts.md)
- **grilled** (1): [Bulgogi Night with Banchan](bulgogi-night-with-banchan.md)
- **holiday** (2): [Butternut Squash Bake](butternut-squash-bake.md), [Paella](paella.md)
- **hungarian** (1): [Paprikash](paprikash.md)
- **indian** (1): [Palak Paneer (Swasthi's Method)](palak-paneer.md)
- **italian** (2): [Kenji's Weeknight Mushroom Pasta](kenji-mushroom-pasta.md), [Ricotta Gnocchi with Brown Butter, Pepitas & Basil](ricotta-gnocchi.md)
- **japanese** (7): [Beef Teriyaki Stir-Fry](beef-teriyaki-stir-fry.md), [Mild Japanese Pork & Kabocha Curry](japanese-pork-curry.md), [Miso Glazed Turnips](miso-glazed-turnips.md), [Modern Sukiyaki](sukiyaki-modern.md), [Seattle-Style Teriyaki Sauce](seattle-style-teriyaki-sauce.md), [Shio Koji Flank Steak with Honey-Roasted Carrots](shio-koji-flank-steak.md), [Sukiyaki (ski-a-ki)](sukiyaki.md)
- **kenji** (4): [Kenji's Ski House Soup](ski-house-soup.md), [Kenji's Weeknight Mushroom Pasta](kenji-mushroom-pasta.md), [Mild Japanese Pork & Kabocha Curry](japanese-pork-curry.md), [Seattle-Style Teriyaki Sauce](seattle-style-teriyaki-sauce.md)
- **korean** (3): [Beef Bulgogi](beef-bulgogi.md), [Bulgogi Marinade](bulgogi-marinade.md), [Bulgogi Night with Banchan](bulgogi-night-with-banchan.md)
- **leftovers** (2): [Ham Bone Lentil Soup](ham-bone-lentil-soup.md), [Morel Risotto Frittata](morel-risotto-frittata.md)
- **main** (30): [Beef and Cabbage Stir-Fry](beef-and-cabbage-stir-fry.md), [Beef Bulgogi](beef-bulgogi.md), [Beef Teriyaki Stir-Fry](beef-teriyaki-stir-fry.md), [Bulgogi Night with Banchan](bulgogi-night-with-banchan.md), [Cold Sesame Noodles](cold-sesame-noodles.md), [Flat Iron Steak with Chanterelle Pan Sauce](flat-iron-chanterelle-pan-sauce.md), [Ham Bone Lentil Soup](ham-bone-lentil-soup.md), [Italian Herb Sausages, Garlicky Kale & Brown Sugar Acorn Squash](sausages-kale-acorn-squash.md), [Italian-Herb Pork Chops with Sautéed Apples and Roasted Delicata](italian-herb-pork-chops.md), [Kenji's Ski House Soup](ski-house-soup.md), [Kenji's Weeknight Mushroom Pasta](kenji-mushroom-pasta.md), [Mary Ann's Chili](mary-anns-chili.md), [Mild Chicken Chile Verde](mild-chicken-chile-verde.md), [Mild Japanese Pork & Kabocha Curry](japanese-pork-curry.md), [Mild Poulet Basquaise](mild-poulet-basquaise.md), [Modern Sukiyaki](sukiyaki-modern.md), [Morel Risotto Frittata](morel-risotto-frittata.md), [Paella](paella.md), [Palak Paneer (Swasthi's Method)](palak-paneer.md), [Paprikash](paprikash.md), [Petrale Sole Meunière with Glazed Salad Turnips](petrale-sole-meuniere-glazed-turnips.md), [Petrale Sole Meunière with Roasted Brussels Sprouts](petrale-sole-brussels-sprouts.md), [Poached Quince with Italian Sausage & Roasted Brussels Sprouts](poached-quince-sausage-brussels.md), [Ricotta Gnocchi with Brown Butter, Pepitas & Basil](ricotta-gnocchi.md), [RJS Stew with Dumplings](rjs-stew.md), [Seared Rockfish over Corn & Okra Maque Choux](rockfish-maque-choux.md), [Shio Koji Flank Steak with Honey-Roasted Carrots](shio-koji-flank-steak.md), [Shrimp Jambalaya](shrimp-jambalaya.md), [Sukiyaki (ski-a-ki)](sukiyaki.md), [Tomato and Egg over Rice](tomato-and-egg-over-rice.md)
- **make-ahead** (5): [Bulgogi Marinade](bulgogi-marinade.md), [Poached Quince with Italian Sausage & Roasted Brussels Sprouts](poached-quince-sausage-brussels.md), [Ricotta Gnocchi with Brown Butter, Pepitas & Basil](ricotta-gnocchi.md), [Seattle-Style Teriyaki Sauce](seattle-style-teriyaki-sauce.md), [Shio Koji Flank Steak with Honey-Roasted Carrots](shio-koji-flank-steak.md)
- **martha-stewart** (3): [Beef Bulgogi](beef-bulgogi.md), [Paprikash](paprikash.md), [Shrimp Jambalaya](shrimp-jambalaya.md)
- **mexican** (1): [Mild Chicken Chile Verde](mild-chicken-chile-verde.md)
- **mild** (17): [Beef and Cabbage Stir-Fry](beef-and-cabbage-stir-fry.md), [Beef Teriyaki Stir-Fry](beef-teriyaki-stir-fry.md), [Bulgogi Marinade](bulgogi-marinade.md), [Bulgogi Night with Banchan](bulgogi-night-with-banchan.md), [Dream Biscuits (ATK Easiest-Ever Biscuits)](dream-biscuits.md), [Kenji's Ski House Soup](ski-house-soup.md), [Kenji's Weeknight Mushroom Pasta](kenji-mushroom-pasta.md), [Mild Chicken Chile Verde](mild-chicken-chile-verde.md), [Mild Japanese Pork & Kabocha Curry](japanese-pork-curry.md), [Mild Poulet Basquaise](mild-poulet-basquaise.md), [Modern Sukiyaki](sukiyaki-modern.md), [Paprikash](paprikash.md), [Poached Quince with Italian Sausage & Roasted Brussels Sprouts](poached-quince-sausage-brussels.md), [Seared Rockfish over Corn & Okra Maque Choux](rockfish-maque-choux.md), [Seattle-Style Teriyaki Sauce](seattle-style-teriyaki-sauce.md), [Shio Koji Flank Steak with Honey-Roasted Carrots](shio-koji-flank-steak.md), [Tomato and Egg over Rice](tomato-and-egg-over-rice.md)
- **mushrooms** (3): [Flat Iron Steak with Chanterelle Pan Sauce](flat-iron-chanterelle-pan-sauce.md), [Kenji's Weeknight Mushroom Pasta](kenji-mushroom-pasta.md), [Morel Risotto Frittata](morel-risotto-frittata.md)
- **no-cook** (1): [Napa Cabbage Slaw with Honey-Cider Vinaigrette](napa-cabbage-slaw.md)
- **noodles** (1): [Cold Sesame Noodles](cold-sesame-noodles.md)
- **one-pan** (1): [Italian-Herb Pork Chops with Sautéed Apples and Roasted Delicata](italian-herb-pork-chops.md)
- **pasta** (2): [Kenji's Weeknight Mushroom Pasta](kenji-mushroom-pasta.md), [Ricotta Gnocchi with Brown Butter, Pepitas & Basil](ricotta-gnocchi.md)
- **pork** (5): [Ham Bone Lentil Soup](ham-bone-lentil-soup.md), [Italian Herb Sausages, Garlicky Kale & Brown Sugar Acorn Squash](sausages-kale-acorn-squash.md), [Italian-Herb Pork Chops with Sautéed Apples and Roasted Delicata](italian-herb-pork-chops.md), [Mild Japanese Pork & Kabocha Curry](japanese-pork-curry.md), [Poached Quince with Italian Sausage & Roasted Brussels Sprouts](poached-quince-sausage-brussels.md)
- **quick** (11): [Beef and Cabbage Stir-Fry](beef-and-cabbage-stir-fry.md), [Beef Teriyaki Stir-Fry](beef-teriyaki-stir-fry.md), [Cold Sesame Noodles](cold-sesame-noodles.md), [Dream Biscuits (ATK Easiest-Ever Biscuits)](dream-biscuits.md), [Kenji's Weeknight Mushroom Pasta](kenji-mushroom-pasta.md), [Mary Ann's Chili](mary-anns-chili.md), [Miso Glazed Turnips](miso-glazed-turnips.md), [Paprikash](paprikash.md), [Petrale Sole Meunière with Glazed Salad Turnips](petrale-sole-meuniere-glazed-turnips.md), [Petrale Sole Meunière with Roasted Brussels Sprouts](petrale-sole-brussels-sprouts.md), [Tomato and Egg over Rice](tomato-and-egg-over-rice.md)
- **roasted** (5): [Italian Herb Sausages, Garlicky Kale & Brown Sugar Acorn Squash](sausages-kale-acorn-squash.md), [Italian-Herb Pork Chops with Sautéed Apples and Roasted Delicata](italian-herb-pork-chops.md), [Petrale Sole Meunière with Roasted Brussels Sprouts](petrale-sole-brussels-sprouts.md), [Poached Quince with Italian Sausage & Roasted Brussels Sprouts](poached-quince-sausage-brussels.md), [Shio Koji Flank Steak with Honey-Roasted Carrots](shio-koji-flank-steak.md)
- **salad** (1): [Napa Cabbage Slaw with Honey-Cider Vinaigrette](napa-cabbage-slaw.md)
- **sauce** (2): [Bulgogi Marinade](bulgogi-marinade.md), [Seattle-Style Teriyaki Sauce](seattle-style-teriyaki-sauce.md)
- **sausage** (4): [Italian Herb Sausages, Garlicky Kale & Brown Sugar Acorn Squash](sausages-kale-acorn-squash.md), [Paella](paella.md), [Poached Quince with Italian Sausage & Roasted Brussels Sprouts](poached-quince-sausage-brussels.md), [Shrimp Jambalaya](shrimp-jambalaya.md)
- **seafood** (2): [Paella](paella.md), [Shrimp Jambalaya](shrimp-jambalaya.md)
- **side** (4): [Butternut Squash Bake](butternut-squash-bake.md), [Dream Biscuits (ATK Easiest-Ever Biscuits)](dream-biscuits.md), [Miso Glazed Turnips](miso-glazed-turnips.md), [Napa Cabbage Slaw with Honey-Cider Vinaigrette](napa-cabbage-slaw.md)
- **slow-cooker** (1): [Ham Bone Lentil Soup](ham-bone-lentil-soup.md)
- **soup** (2): [Ham Bone Lentil Soup](ham-bone-lentil-soup.md), [Kenji's Ski House Soup](ski-house-soup.md)
- **spanish** (1): [Paella](paella.md)
- **steak** (2): [Flat Iron Steak with Chanterelle Pan Sauce](flat-iron-chanterelle-pan-sauce.md), [Shio Koji Flank Steak with Honey-Roasted Carrots](shio-koji-flank-steak.md)
- **stir-fry** (3): [Beef and Cabbage Stir-Fry](beef-and-cabbage-stir-fry.md), [Beef Bulgogi](beef-bulgogi.md), [Beef Teriyaki Stir-Fry](beef-teriyaki-stir-fry.md)
- **stovetop** (16): [Flat Iron Steak with Chanterelle Pan Sauce](flat-iron-chanterelle-pan-sauce.md), [Kenji's Ski House Soup](ski-house-soup.md), [Kenji's Weeknight Mushroom Pasta](kenji-mushroom-pasta.md), [Mary Ann's Chili](mary-anns-chili.md), [Mild Japanese Pork & Kabocha Curry](japanese-pork-curry.md), [Miso Glazed Turnips](miso-glazed-turnips.md), [Modern Sukiyaki](sukiyaki-modern.md), [Palak Paneer (Swasthi's Method)](palak-paneer.md), [Paprikash](paprikash.md), [Petrale Sole Meunière with Glazed Salad Turnips](petrale-sole-meuniere-glazed-turnips.md), [RJS Stew with Dumplings](rjs-stew.md), [Seared Rockfish over Corn & Okra Maque Choux](rockfish-maque-choux.md), [Shio Koji Flank Steak with Honey-Roasted Carrots](shio-koji-flank-steak.md), [Shrimp Jambalaya](shrimp-jambalaya.md), [Sukiyaki (ski-a-ki)](sukiyaki.md), [Tomato and Egg over Rice](tomato-and-egg-over-rice.md)
- **summer** (1): [Cold Sesame Noodles](cold-sesame-noodles.md)
- **vegetarian** (9): [Butternut Squash Bake](butternut-squash-bake.md), [Cold Sesame Noodles](cold-sesame-noodles.md), [Kenji's Ski House Soup](ski-house-soup.md), [Miso Glazed Turnips](miso-glazed-turnips.md), [Morel Risotto Frittata](morel-risotto-frittata.md), [Napa Cabbage Slaw with Honey-Cider Vinaigrette](napa-cabbage-slaw.md), [Palak Paneer (Swasthi's Method)](palak-paneer.md), [Ricotta Gnocchi with Brown Butter, Pepitas & Basil](ricotta-gnocchi.md), [Tomato and Egg over Rice](tomato-and-egg-over-rice.md)

## Archive

Retired recipes, kept for reference. They're out of the tag index above.

| Recipe | From | Tags |
|---|---|---|
| [Bobotie](archive/bobotie.md) |  | claude, main, beef, south-african, baked |
| [Creste di Gallo with Nettle-Hazelnut Pesto, Brussels Sprouts & Carrots](archive/creste-di-gallo-nettle-hazelnut-pesto.md) |  | claude, main, pasta, vegetarian, italian, roasted |
| [Pasta alla Norma](archive/pasta-alla-norma.md) |  | claude, main, pasta, vegetarian, italian, mild |
