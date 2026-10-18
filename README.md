# etsy-erank-research

A free Claude skill that does Etsy product research from start to finish:

1. **Bestseller hunt.** Claude in Chrome reads Etsy search pages for your niche
   and logs every listing, with its Bestseller / Popular now badges, price, and
   whether it is digital or physical. It groups the listings into styles and
   saves a spreadsheet.
2. **Seed keywords.** Claude turns the styles into shopper-worded seed
   keywords, weighted by how many badges each style earned.
3. **eRank exports.** In your logged-in eRank account, Claude searches each seed
   in the Keyword Tool and uses eRank's own Export button for the Keyword Ideas
   and Top Listings tables.
4. **Analysis + report.** A script scores every related keyword by demand per
   competing listing and keyword difficulty, flags brand and franchise names,
   and builds one Excel workbook. Claude reviews it, spot-checks the best
   phrases on Etsy, and writes a plain-English report: what to make, what to
   title it, and what to avoid.

Example from one run (Etsy "art prints", US, October 2026): 55 seeds, 15,574
related keywords and 5,464 top listings. The run showed that badge-heavy styles
like Frame TV art were the most crowded (17 searches per 1,000 listings), while
pressed flower art had 80. "japanese wall art" gets about 4x the searches of
"japanese art print" (2,693 vs. 621 a month). See
[`examples/art-prints-report.md`](examples/art-prints-report.md).

## Requirements

| You need | Why |
|---|---|
| **Claude Code** on a paid Claude plan (Pro, Max, Team or Enterprise) | Runs the skill |
| **Google Chrome + the [Claude in Chrome](https://claude.com/chrome) extension**, connected to Claude Code (`claude --chrome`, or `/chrome` in a session) | Reads Etsy and drives eRank in your own browser |
| **An eRank account**, Pro recommended ([eRank, affiliate link](https://erank.com?fpr=randall)) | The keyword data. Pro is $9.99/month with 200 keyword searches a day. Each seed uses 1 search |
| **Python 3.9+** with pandas and openpyxl (`pip install -r requirements.txt`) | Builds the spreadsheets |

You log in to Etsy (optional) and eRank yourself. Claude never asks for or
types a password.

## Install

```bash
# personal skill, available in every project
git clone https://github.com/Pardesco/etsy-erank-research ~/.claude/skills/etsy-erank-research
pip install -r ~/.claude/skills/etsy-erank-research/requirements.txt
```

On Windows the folder is `%USERPROFILE%\.claude\skills\etsy-erank-research`.
To use it in one project only, clone it into that project's `.claude/skills/`.

## Use

Start Claude Code with Chrome connected, log in to eRank in that Chrome, then
ask:

```text
/etsy-erank-research  research "ceramic mugs" on Etsy: 3 pages, 25 seeds, USA
```

or in plain words: *"Research what to sell in the Etsy niche 'dog bandanas'
with eRank."* Already have a bestseller spreadsheet? Say so, and Claude starts
at the seed step.

Claude shows the seed list and the eRank search cost before it spends any
searches. A 30-seed run takes about 30-45 minutes, mostly waiting on page
loads, and can resume the next day if your daily searches run out.

### Output

```
etsy-research/<niche>-<date>/
  01_etsy/etsy_bestsellers.xlsx      Style Summary, Badged, All Listings
  02_seeds/seeds.csv                 seeds, groups and why each was chosen
  03_erank/exports/                  eRank's own CSV exports, two per seed
  04_results/research.xlsx           Seeds, Style Matrix, Clean Opportunities, Best by Group,
                                     Better Phrasing, flagged list, all keywords, Top Listings,
                                     Top Tags, Top Shops, Price Bands
  04_results/REPORT.md               the written findings
```

## How it treats Etsy and eRank

- It uses the normal web pages and eRank's Export button at human pace, inside
  your plan's daily limit. It does not call private APIs.
- It stops on a CAPTCHA, login wall or rate-limit message and hands control
  back to you.
- It reads a few Etsy search pages, not individual listings.
- You are responsible for using both sites within their terms.

## Limits

- eRank numbers are estimates. They are good for ranking options, not for
  forecasting sales.
- The brand / franchise / artist screen is a keyword filter plus Claude's
  review. It is not legal advice.
- Etsy and eRank change their pages. If a capture or button stops matching,
  Claude falls back to screenshots and page text. Please open an issue.

## Disclosure

Not affiliated with, endorsed by, or sponsored by Etsy or eRank. The eRank link
above is an affiliate link: if you sign up through it I may earn a commission,
at no extra cost to you. The skill works the same with any eRank account.

## License

MIT. See [LICENSE](LICENSE).
