# Phase 1: capturing Etsy search pages

## Page loop

1. Navigate to `https://www.etsy.com/search?q=<niche>&page=<N>` (omit `&page`
   for page 1). Wait for listing cards to render.
2. Run the snippet below with the JavaScript tool. It stores the page in
   `window.__etsyPage` and returns a short summary.
3. Pull the rows out in chunks small enough for your tool's output limit, for
   example `JSON.stringify(window.__etsyPage.slice(0, 12))`, then 12-24, and so
   on. Some browser tools cut long results or block text that looks like
   `key=value` pairs; the snippet strips query strings from URLs for that reason.
4. Add `page` to every row and append them to `01_etsy/listings.json`. Save the
   file before going to the next page.
5. On page 1 only: take a screenshot and compare 3 cards (title, price, badge,
   ad label) with the captured rows. If they disagree, Etsy's markup changed.
   Fall back to the page-text tool and transcribe the cards by hand.

Etsy shows about 60-70 cards per page, about a third of them ads. Ads are
kept (with `"ad": true`) because they show what sellers pay to promote, but the
Style Summary counts badges, not ads.

## Snippet (tested on etsy.com search, October 2026)

```js
(() => {
  const byId = new Map();
  for (const el of document.querySelectorAll('[data-listing-id]')) {
    const id = el.getAttribute('data-listing-id');
    const prev = byId.get(id);
    if (!prev || el.innerText.length > prev.innerText.length) byId.set(id, el);
  }
  const rows = [];
  for (const [id, el] of byId) {
    const t = el.innerText;
    const prices = [...t.matchAll(/(?:US\$|CA\$|A\$|\$|£|€)\s?([\d,]+\.\d{2})/g)].map(m => +m[1].replace(/,/g, ''));
    const title = (el.querySelector('h3')?.innerText || '').trim();
    if (!title || !prices.length) continue;
    rows.push({
      position: rows.length + 1, id, title: title.slice(0, 140),
      shop: (t.match(/from shop\s+([A-Za-z0-9]+)/i) || [])[1] || null,   // null for "Ad by Etsy seller"
      price: Math.min(...prices),
      original_price: prices.length > 1 ? Math.max(...prices) : null,
      badges: ['Bestseller', 'Popular now', 'Star Seller', "Etsy's Pick"].filter(b => t.includes(b)),
      ad: /\bAd (?:by|from)\b|\bAd[・·]|Advertisement/i.test(t),
      format: /digital download/i.test(t) ? 'digital' : 'physical',
      url: (el.querySelector('a[href*="/listing/"]')?.href || '').split('?')[0],
    });
  }
  window.__etsyPage = rows;
  const n = k => rows.filter(r => r.badges.includes(k)).length;
  return `${rows.length} cards | ads ${rows.filter(r => r.ad).length} | Bestseller ${n('Bestseller')} | Popular now ${n('Popular now')}`;
})()
```

Prices are in the shopper's display currency. Note the currency in the JSON
header if it is not USD.

## `01_etsy/listings.json` schema

```json
{
  "query": "art prints",
  "site": "etsy.com",
  "currency": "USD",
  "captured": "2026-10-18",
  "pages": 3,
  "listings": [
    {
      "page": 1, "position": 1, "id": "1234567890",
      "title": "Swallow Bird Linocut Print, Folk Art Botanical",
      "shop": "ExampleShop", "price": 8.99, "original_price": 11.99,
      "badges": ["Bestseller"], "ad": false, "format": "physical",
      "url": "https://www.etsy.com/listing/1234567890/...",
      "style": "Linocut / printmaking"
    }
  ]
}
```

`style` is added after all pages are captured (SKILL.md phase 1, step 4).
Good style labels describe what a shopper sees: "Japanese woodblock style",
"Mid-century retro poster", "Printable bundle (100+ files)", "Custom pet
portrait". Keep bundles and custom/personalized work in their own styles; they
behave differently in eRank.

## If Etsy pushes back

A CAPTCHA, "unusual traffic" or sign-in wall means stop. Tell the user, and let
them clear it in their own browser. Never try to solve it, and do not retry in
a loop. Reading fewer pages is fine: 3 pages of a niche already show the
pattern.
