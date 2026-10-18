"""Static checks for tungsten.bet: the data files, the built pages, and the page constraints.

Run from anywhere:  python3 -I tests/check_static.py

The data in data/ is the source of truth. The James page (deploy/jamesob.html) and the front page
(deploy/index.html) are built from it by build/assemble.py; this script fails if they are stale.
Counts (how many items pass each filter) are printed, not pinned: they change whenever an item does.
"""
import json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "build"))
import assemble  # noqa: E402

results = []

def check(name, ok, detail=""):
    results.append((name, bool(ok), detail))

items, ladder, bets = assemble.load()
ids = [e["id"] for e in items]
by_id = {e["id"]: e for e in items}

# ---- items ----
check("items.json parses", True, f"{len(items)} items")
check("ids unique", len(set(ids)) == len(ids))
check("ids are letter+number (Q1, M6, P9, X1)", all(re.fullmatch(r"[QMPX]\d+", i) for i in ids), str([i for i in ids if not re.fullmatch(r"[QMPX]\d+", i)]))
REQ = {"id": str, "date": str, "title": str, "domain": str, "tier": int, "llm": bool, "physical": bool, "quantum": bool,
       "verification": str, "who": str, "what": str, "artifact": str, "caveat": str, "P": (int, float), "H": str, "W": (int, float), "C": (int, float), "url": str}
bad = [f"{e.get('id')}.{k}" for e in items for k, t in REQ.items() if not isinstance(e.get(k), t) or isinstance(e.get(k), bool) and t is not bool]
check("every item has every field with the right type", not bad, str(bad))
check("dates are YYYY-MM", all(re.fullmatch(r"20\d\d-(0[1-9]|1[0-2])", e["date"]) for e in items), str([e["id"] for e in items if not re.fullmatch(r"20\d\d-(0[1-9]|1[0-2])", e["date"])]))
check("tier in 1..3", all(e["tier"] in (1, 2, 3) for e in items))
check("verification values valid", all(e["verification"] in ("peer-reviewed", "preprint", "company-reported") for e in items))
check("H values valid", all(e["H"] in ("now", "years", "decades", "someday") for e in items))
check("P 0-10, W 1-4, C 0-1", all(0 <= e["P"] <= 10 and 1 <= e["W"] <= 4 and 0 <= e["C"] <= 1 for e in items))
check("contested is true or absent", all(e.get("contested", True) is True for e in items))
check("every item has http(s) url", all(re.match(r"https?://", e["url"]) for e in items))
check("every item has non-empty caveat", all(e["caveat"].strip() for e in items))
check("every item has non-empty what, who, title", all(e["what"].strip() and e["who"].strip() and e["title"].strip() for e in items))

# ---- ladder ----
check("LADDER rates every item exactly once", sorted(ladder) == sorted(ids), str(sorted(set(ids) ^ set(ladder))))
check("LADDER values valid", all(
    isinstance(v["matter"], bool) and v["necessary"] in (True, False, "arguable") and v["leap"] in ("none", "early sign", "leap")
    and isinstance(v["qubits"], bool) and v["why"].strip() for v in ladder.values()))
check("LADDER rows carry only the five fields", all(set(v) == {"matter", "necessary", "leap", "qubits", "why"} for v in ladder.values()))

# ---- bets ----
check("bets.json parses", True, f"{len(bets)} bets")
check("bet ids unique", len({b["id"] for b in bets}) == len(bets))
check("bet status valid", all(b["status"] in assemble.STATUS for b in bets), str([b["id"] for b in bets if b["status"] not in assemble.STATUS]))
check("every bet has a claim, a stake and at least one source url", all(b["claim"].strip() and b["stake"].strip() and b.get("sources") and all(re.match(r"https?://", s["url"]) for s in b["sources"]) for b in bets))
check("every open bet names a page", all(b.get("page") for b in bets if b["status"] == "open"))
check("no bet lost (the front page says so; change the box title if this ever fails)", not any(b["status"] == "lost" for b in bets))

# ---- built pages are what the data builds ----
jamesob = (ROOT / "deploy" / "jamesob.html").read_text(encoding="utf-8")
front = (ROOT / "deploy" / "index.html").read_text(encoding="utf-8")
check("deploy/jamesob.html is built from data/", jamesob == assemble.build_exhibit(items, ladder), "run python3 -I build/assemble.py")
check("deploy/index.html is built from data/", front == assemble.build_root(bets), "run python3 -I build/assemble.py")
check("no stray index.html at the repository root", not (ROOT / "index.html").exists(), "the site lives in deploy/")

# ---- page constraints (both pages) ----
for name, html in (("jamesob", jamesob), ("front", front)):
    check(f"{name}: no external <script src>", not re.search(r"<script[^>]+src=", html, re.I))
    check(f"{name}: only Google Fonts loaded externally", all("fonts.googleapis.com" in u for u in re.findall(r'<link[^>]+href="(https?://[^"]+)"', html)))
check("jamesob: one hard-coded verdict word per side, none computed", len(re.findall(r"verdict: '[^']+'", jamesob)) == 2)
check("jamesob: Eric's side is quoted from his own post", "ercwl/status/1928882831175876997" in jamesob and "AI cannot invent solutions/workarounds" in jamesob)
james_bet = next(b for b in bets if b["id"] == "jamesob")
check("jamesob: the before/after split is the month James posted his test", f"const BET = '{james_bet['opened'][:7]}';" in jamesob)
check("jamesob: no filter of Eric's own (the steps are James's test only)", "strict test" not in jamesob.lower())
check("jamesob: bet record links all four stages", all(u in jamesob for u in [
    "jamesob/status/1928911469342806444", "ercwl/status/1928915231344091358", "ercwl/status/1941525148722659776", "jamesob/status/2022527098670526479"]))
check("jamesob: address line points at /jamesob and links home", 'href="/"' in jamesob and "</a>/jamesob" in jamesob)
check("front: links to /jamesob", 'href="/jamesob"' in front)
check("front: every bet row rendered", all(f'id="bet-{b["id"]}"' in front for b in bets))
vercel = json.loads((ROOT / "deploy" / "vercel.json").read_text())
check("vercel.json: cleanUrls on, no trailing slash", vercel.get("cleanUrls") is True and vercel.get("trailingSlash") is False)

# ---- counts, printed for the record (not pinned) ----
def sel(*conds):
    return [e["id"] for e in items if all(c(e) for c in conds)]
llm = lambda e: e["llm"]; phys = lambda e: e["physical"]; peer = lambda e: e["verification"] == "peer-reviewed"
matter = [i for i in ids if ladder[i]["matter"]]
nec = [i for i in matter if ladder[i]["necessary"] is True]
leap = [i for i in ids if ladder[i]["leap"] == "leap"]
bridge = [i for i in matter if ladder[i]["qubits"]]
print(f"items {len(items)} · contested {[e['id'] for e in items if e.get('contested')]}")
after = lambda e: e["date"] > james_bet["opened"][:7]
print(f"since the bet {sel(after)} · before {[i for i in ids if i not in sel(after)]}")
print(f"LLM-driven and ran on hardware {sel(llm, phys)} · + peer-reviewed {sel(llm, phys, peer)}")
print(f"any AI, physical, peer-reviewed {sel(phys, peer)}")
print(f"step 1 touched matter {matter} · step 2 necessary {nec} · step 3 leap {leap} · matter and qubits {bridge}")
print(f"since the bet: step 1 {[i for i in matter if after(by_id[i])]} · step 2 {[i for i in nec if after(by_id[i])]} · step 3 {[i for i in leap if after(by_id[i])]}")
print(f"LLM-driven that touched matter {[i for i in matter if by_id[i]['llm']]}")
print()

w = max(len(n) for n, _, _ in results)
for n, ok, d in results:
    print(f"{'PASS' if ok else 'FAIL'}  {n.ljust(w)}  {d}")
sys.exit(0 if all(ok for _, ok, _ in results) else 1)
