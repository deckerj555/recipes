# Recipe repo conventions

Family recipe collection: transcribed handwritten cards plus recipes written with Claude. Match the existing files exactly; consistency matters more than any one recipe's polish.

## Before you push

Show Jeff the commit message and a short summary of what changed, and wait for his OK. Don't push on your own initiative. Never rewrite history or force-push.

## Files

- One Markdown file per recipe, at the top level. No folders for recipes; tags do the organizing.
- Filename is a lowercase hyphenated slug of the dish, short enough to read (`rockfish-maque-choux.md`, not the full title).
- Card photos for family recipes go in `originals/` as `<slug>-front.jpg` and `<slug>-back.jpg`.

## Recipe format

```markdown
---
title: Seared Rockfish over Corn & Okra Maque Choux
serves: 4
tags: [claude, main, fish, cajun, stovetop, mild]
original: https://claude.ai/chat/<id>
---

# Seared Rockfish over Corn & Okra Maque Choux

*One-line description in italics: what it is, how long, any key point.*

## Ingredients

- quantity, then ingredient, then prep ("2 carrots, sliced thin on a sharp diagonal")

## Steps

1. **Short step name.** Instructions. Say why when the technique isn't obvious. *(timer: 5 min)*

## Notes

Swaps, sourcing, make-ahead, what to watch for.
```

- Front matter fields, in this order: `title`, `from` (family recipes only: who the card came from), `serves` (if known), `tags`, `original` (Claude recipes only: link to the chat it came from).
- The `# ` heading matches `title`.
- Every step that involves waiting, cooking, resting or chilling ends with `*(timer: …)*`.
- A variant gets its own `## ` section after Notes ("## Without okra", "## Slow-cooker version") instead of a second file.
- Family recipes end with `## Original card` showing the photos. Transcribe the card's final version: honor handwritten corrections over the printed text.

## Tags

Reuse existing tags before inventing new ones.

- Source: `claude` (written with Claude) or `family` (transcribed card). `favorite` is Jeff's to add; don't add it yourself.
- Course: `main`, `side`, `sauce`, `breakfast`
- Main ingredient: `beef`, `steak`, `pork`, `sausage`, `chicken`, `fish`, `eggs`, `mushrooms`, `vegetarian`, `pasta`, `noodles`, `soup`, `salad`
- Cuisine: `italian`, `french`, `cajun`, `mexican`, `korean`, `japanese`, `chinese`, `asian`, `indian`, `south-african`
- Method: `stovetop`, `roasted`, `baked`, `grilled`, `braise`, `stir-fry`, `slow-cooker`, `one-pan`, `no-cook`
- Other: `quick` (under 45 min), `mild`, `make-ahead`, `freezer`, `leftovers`, `summer`, `fall`, `holiday`

## README index

Every recipe has a row in the README's Recipes table, sorted by title: link, `From` (family recipes only), and tags as comma-separated text. Add or update the row in the same commit as the recipe. If a title changes, change it in the front matter, the `# ` heading and the README row together.

## Commits

- One commit per recipe, so each file's history stays clean.
- A revision is a new commit on the existing file, never a new file.
- Commit message names the recipe and what changed: "Maque choux: poblanos instead of sweet peppers". A new recipe is "Add <title>".
- Git tags can't be pushed from Claude's sandbox. When Jeff wants to mark a version, give him the commit permalink and he'll tag it on GitHub (Releases → Draft a new release → Choose a tag).
