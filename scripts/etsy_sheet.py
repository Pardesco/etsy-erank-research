"""Build the phase-1 spreadsheet from 01_etsy/listings.json.

Usage: python <skill>/scripts/etsy_sheet.py 01_etsy/listings.json
Writes etsy_bestsellers.xlsx next to the JSON: All Listings, Badged, Style Summary.
"""
import json
import sys
from pathlib import Path

import pandas as pd


def main():
    src = Path(sys.argv[1] if len(sys.argv) > 1 else "01_etsy/listings.json").resolve()
    data = json.loads(src.read_text(encoding="utf-8"))
    L = pd.DataFrame(data.get("listings", []))
    if L.empty:
        sys.exit(f"{src}: no listings")
    for col in ("style", "badges", "ad", "format", "original_price", "url"):
        if col not in L:
            L[col] = None
    L["style"] = L["style"].fillna("(unassigned)")
    L["badges"] = L["badges"].map(lambda b: b if isinstance(b, list) else [])
    L["Badges"] = L["badges"].map(", ".join)
    L["Bestseller"] = L["badges"].map(lambda b: "Bestseller" in b)
    L["Popular now"] = L["badges"].map(lambda b: "Popular now" in b)
    L["Badged"] = L["badges"].map(lambda b: bool(set(b) & {"Bestseller", "Popular now", "Etsy's Pick"}))
    cols = ["page", "position", "Badges", "ad", "format", "price", "original_price", "shop", "title", "style", "url"]
    listings = L[[c for c in cols if c in L]].rename(columns=str.capitalize)

    total_badged = int(L["Badged"].sum()) or 1
    rows = []
    for style, sub in L.groupby("style"):
        b = sub[sub["Badged"]]
        rows.append({"Style": style, "Listings seen": len(sub), "Badged": len(b),
                     "Bestseller": int(sub["Bestseller"].sum()), "Popular now": int(sub["Popular now"].sum()),
                     "Ads": int(sub["ad"].fillna(False).astype(bool).sum()),
                     "Physical": int((sub["format"] == "physical").sum()), "Digital": int((sub["format"] == "digital").sum()),
                     "Median price $": round(sub["price"].median(), 2) if sub["price"].notna().any() else None,
                     "Median badged price $": round(b["price"].median(), 2) if len(b) and b["price"].notna().any() else None,
                     "Share of badged listings": round(len(b) / total_badged, 3)})
    summary = pd.DataFrame(rows).sort_values(["Badged", "Listings seen"], ascending=False)

    out = src.with_name("etsy_bestsellers.xlsx")
    with pd.ExcelWriter(out, engine="openpyxl") as xw:
        summary.to_excel(xw, sheet_name="Style Summary", index=False)
        listings[L["Badged"].values].to_excel(xw, sheet_name="Badged", index=False)
        listings.to_excel(xw, sheet_name="All Listings", index=False)
    print(f"wrote {out} | {len(L)} listings, {int(L['Badged'].sum())} badged, {L['style'].nunique()} styles "
          f"from '{data.get('query', '?')}' pages 1-{data.get('pages', '?')}")
    print(summary.head(8)[["Style", "Badged", "Listings seen", "Median price $"]].to_string(index=False))


if __name__ == "__main__":
    main()
