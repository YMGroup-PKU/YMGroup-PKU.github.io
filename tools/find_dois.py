#!/usr/bin/env python3
"""Look up DOIs from Crossref for publications that have no link yet.

Reads PAPERS from gen_publications.py, queries Crossref by title (+venue),
validates the best match by title similarity and year, and prints a report.
Accepted matches are also written to tools/doi_results.tsv for applying.

Run with the proxy exported, e.g.:
    export https_proxy=http://127.0.0.1:7897 http_proxy=http://127.0.0.1:7897
    python3 tools/find_dois.py
"""
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
from difflib import SequenceMatcher

sys.path.insert(0, os.path.dirname(__file__))
from gen_publications import PAPERS  # noqa: E402

MAILTO = "yaomin.zhao@pku.edu.cn"
OUT = os.path.join(os.path.dirname(__file__), "doi_results.tsv")


def norm(s):
    s = re.sub(r"<[^>]+>", "", s)
    s = s.replace("–", "-").replace("—", "-")
    s = re.sub(r"[^a-z0-9 ]", " ", s.lower())
    return re.sub(r"\s+", " ", s).strip()


def query(title, venue):
    q = urllib.parse.quote(title + " " + venue)
    url = ("https://api.crossref.org/works?query.bibliographic=%s&rows=5&mailto=%s"
           % (q, MAILTO))
    req = urllib.request.Request(url, headers={"User-Agent": "doi-finder/1.0 (%s)" % MAILTO})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)["message"]["items"]


def best_match(title, year, items):
    tnorm = norm(title)
    best = None
    for it in items:
        cand = (it.get("title") or [""])[0]
        if not cand:
            continue
        sim = SequenceMatcher(None, tnorm, norm(cand)).ratio()
        yr = None
        dp = (it.get("issued", {}).get("date-parts") or [[None]])[0]
        if dp and dp[0]:
            yr = dp[0]
        if best is None or sim > best[0]:
            best = (sim, it.get("DOI"), cand, yr,
                    (it.get("container-title") or [""])[0])
    return best


def main():
    rows = []
    for entry in PAPERS:
        slug, year, category, authors, title, venue, volpart, extra, url = entry
        if url:
            continue  # already has a link
        try:
            items = query(title, venue)
            b = best_match(title, year, items)
        except Exception as e:  # network hiccup
            print("ERR  %-32s %s" % (slug, e))
            rows.append((slug, "", "ERROR", str(e), ""))
            time.sleep(0.5)
            continue
        if not b:
            print("MISS %-32s (no candidates)" % slug)
            rows.append((slug, "", "MISS", "", ""))
            continue
        sim, doi, cand, yr, cont = b
        yr_ok = (yr is None) or (abs((yr or 0) - year) <= 1)
        flag = "OK " if (sim >= 0.90 and yr_ok) else "?? "
        print("%s %-32s sim=%.2f y=%s/%s  %s" % (flag, slug, sim, yr, year, doi))
        if flag != "OK ":
            print("      want: %s" % title)
            print("      got : %s (%s)" % (cand, cont))
        rows.append((slug, doi, flag.strip(), "%.2f" % sim, "%s/%s" % (yr, year)))
        time.sleep(0.3)

    with open(OUT, "w", encoding="utf-8") as f:
        for r in rows:
            f.write("\t".join(r) + "\n")
    n_ok = sum(1 for r in rows if r[2] == "OK")
    print("\n%d entries queried, %d high-confidence, results -> %s"
          % (len(rows), n_ok, os.path.normpath(OUT)))


if __name__ == "__main__":
    main()
