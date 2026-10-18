# Phase 3: driving eRank's Keyword Tool

eRank's layout changes from time to time. Find things by their visible labels,
take a screenshot when unsure, and never guess a click.

## Before the first seed

1. Open `https://erank.com` in a new tab. If you see a login page, ask the user
   to log in and wait. Never type their credentials.
2. Go to **Keyword Research > Keyword Tool**.
3. In the top search bar, check the marketplace dropdown (left of the search
   box) says **Etsy**, and the country dropdown (right of it) is the country
   the user chose.
4. Note the **Searches: used/limit** counter beside the search button (for
   example `17/200` on eRank Pro). Write it to `progress.json`.

## Per seed

1. Click the search box, select all, type the seed, press Enter.
2. Wait until the heading under "Keyword Tool" shows the seed and the Keyword
   Statistics panel (Avg. Searches, Avg. Clicks, CTR, Competition) has numbers.
3. Tabs under the charts: **Keyword Ideas**, Near Matches, Search Results
   Analysis, **Top Listings**, Marketplaces.
4. **Keyword Ideas** tab: click **Export** (right side, above the table), then
   **Download as CSV**. Then run:
   `python <skill>/scripts/collect_download.py 03_erank/exports <seed-slug>__keywords`
5. **Top Listings** tab: click **Export**, then **Download as CSV**. If the tab
   has a **Show All Tags** toggle, turn it on first so tags are included. Then:
   `python <skill>/scripts/collect_download.py 03_erank/exports <seed-slug>__listings`
6. If `collect_download.py` reports nothing new, the click missed. Take a
   screenshot, retry once, then mark the seed `skipped`.
7. Update `progress.json`.

`<seed-slug>` is the seed lowercased with every run of non-letters/digits
replaced by `-`: `christmas frame tv art` becomes `christmas-frame-tv-art`.
`analyze.py` uses the same rule to match files to seeds.

Switching tabs and exporting do not use extra searches; only a new search does.
Excel exports also work (`collect_download.py` keeps the extension).

## `03_erank/progress.json`

```json
{
  "country": "USA",
  "searches_counter": "41/200",
  "updated": "2026-10-18T14:05:00",
  "seeds": {
    "japanese wall art": {"status": "done", "files": ["japanese-wall-art__keywords.csv", "japanese-wall-art__listings.csv"]},
    "woodblock print": {"status": "skipped", "reason": "Top Listings export menu missing"}
  }
}
```

## Pace and limits

- One seed at a time, at the pace of the UI. A seed takes about a minute.
- Stop with 5 searches left. eRank's counter resets daily; tell the user the run
  resumes then.
- If eRank shows a rate-limit, upgrade or error banner, stop and tell the
  user. Do not work around it.
- The free eRank plan has a much lower daily limit and may hide columns or
  exports. The skill is built and tested on eRank Pro.
