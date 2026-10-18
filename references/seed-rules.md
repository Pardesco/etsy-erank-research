# Phase 2: choosing seed keywords

A seed is a phrase you run through eRank. eRank returns several hundred related
phrases for each one, so seeds only need to cover the territory, not every
variant.

## Rules

1. **Shopper wording, not maker wording.** Shoppers type "japanese wall art"
   (about 2,700 searches a month in one test), not "ukiyo-e print" (3). Name
   the subject, the room, the colour or the gift, the way a buyer would.
2. **2-4 words.** One-word seeds return noise. Five-word seeds return almost
   nothing related.
3. **Weight by badges.** Styles with the most Bestseller / Popular now badges
   get 3-4 seeds. Styles with one badge get one.
4. **Add a `core` group.** 1-3 broad phrases for the niche itself ("art
   prints", "printable wall art"). Every other seed is compared against them.
5. **Cover formats and occasions** the capture showed: digital vs. physical,
   bundles, custom/personalised, seasonal ("christmas wall art").
6. **No IP.** No brands, franchises, characters, celebrities or living or
   in-copyright artists in seeds. Public-domain artists (Monet, Hokusai, Van
   Gogh) are fine as seeds.
7. **Dedupe.** If two seeds differ only by plural or word order, keep one.

## Budget

Each seed costs one eRank keyword search. Check the "Searches: used/limit"
counter at the top of eRank's Keyword Tool. Keep at least 5 searches in reserve
for re-tries. Seeds over budget wait for the next day (see `progress.json`).

## `seeds.csv` example

```csv
seed,group,style,why
art prints,core,,Baseline for the whole niche
japanese wall art,japanese,Japanese woodblock style,Shopper phrasing; 14 badges
woodblock print,japanese,Japanese woodblock style,Format term for the same style
linocut print,printmaking,Linocut / printmaking,4 badges; mostly physical
christmas frame tv art,seasonal,Seasonal Frame TV art,13 badges; digital
custom pet portrait,custom,Custom pet portrait,Service listings; check separately
```

`style` must match the style label in `listings.json` exactly so the workbook
can line up badges with eRank numbers. Leave it blank for `core` seeds.

## Term lists

- `relevance_terms.txt`: a related keyword is "on topic" when it contains any
  of these words. Art prints example: `print, prints, art, poster, painting,
  wall, decor, canvas, illustration, artwork, printable`. Jewellery example:
  `ring, necklace, earrings, bracelet, jewelry, pendant`.
- `exclude_terms.txt`: words that mean a different product, e.g. for art
  prints `shirt, sticker, mug, rug, frame, mirror, decal, wallpaper, clock`.
- `ip_terms_extra.txt`: starts empty. Filled during the phase-4 IP review.
