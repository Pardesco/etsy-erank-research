# Phase 4: what the numbers mean

| Column | Meaning |
|---|---|
| Avg searches/mo | eRank's estimate of monthly Etsy searches for the exact phrase |
| Avg clicks/mo, CTR % | Clicks on results. CTR over 100% means shoppers open several listings per search, a sign of browsing intent |
| Competition (listings) | Etsy listings eRank counts for the phrase. Blank = not measured |
| KD (0-100) | eRank keyword difficulty. Higher = harder for a new listing to rank |
| Searches per 1k listings | `searches × 1000 / competition`. Demand per unit of supply |
| Opportunity score | `searches per 1k listings × (1 − KD/125)`. Missing KD counts as 100 |

## Filters

- **Opportunities**: at least `--min-searches` (default 100) searches a month,
  measured competition, and on topic per `relevance_terms.txt`.
- **Clean Opportunities**: opportunities without an IP flag and without a
  "different product" word.
- **Better Phrasing**: for each seed, the best clean related phrase with more
  searches *and* lower KD than the seed. These are retitling wins.

## Reading the workbook

1. **Seeds**, sorted by searches per 1k listings: the crowded vs. open map.
   Compare each seed with the `core` seeds.
2. **Style Matrix** (when phase 1 ran): badges on Etsy next to eRank numbers.
   Many badges plus a low ratio means "sells, but crowded".
3. **Clean Opportunities** and **Best by Group**: the long tail to build
   listings around.
4. **Better Phrasing**: wording changes for existing listings.
5. **Top Tags**: tags shared by many top listings, with their own eRank volume.
6. **Price Bands**: P25 / median / P75 per seed and format. Format is inferred
   from titles and tags, so check a few by eye.

## Caveats to repeat in the report

- eRank numbers are estimates. Use them to rank options, not to forecast sales.
- Low competition on a brand or living artist's name usually means legal risk,
  not opportunity.
- Est. sales and revenue are eRank's view-based estimates, not Etsy data.
- A phrase can mean something else on Etsy (wrong product or audience). The
  phase-4 spot check exists for that reason.
