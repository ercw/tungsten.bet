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
check("every bet names a page", all(b.get("page") for b in bets), str([b["id"] for b in bets if not b.get("page")]))
check("no bet lost (the front page says so; change the box title if this ever fails)", not any(b["status"] == "lost" for b in bets))

# ---- cube pages and the posts they quote ----
cubes, posts = assemble.load_cubes()
norm = lambda t: re.sub(r"\s+", " ", t.replace(" / ", " ").replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')).strip().lower()
won = [b for b in bets if b["status"] == "won"]
check("posts.json: every post has user, time, url and text", all({"user", "at", "url", "text"} <= set(v) <= {"user", "at", "url", "text", "archive", "image_text"} and v["text"].strip() and v["url"].endswith(k) for k, v in posts.items()))
check("cubes.json: one page per won cube, none for open bets", sorted(c["bet"] for c in cubes) == sorted(b["id"] for b in won), str(sorted(c["bet"] for c in cubes)))
check("cubes.json: each route matches the bet's page", all(next(b for b in bets if b["id"] == c["bet"])["page"] == "/" + c["route"] for c in cubes))
missing = [f'{c["route"]}:{x["post"]}' for c in cubes for x in c["terms"] + c["log"] if x.get("post") and x["post"] not in posts]
check("cube pages quote only archived posts", not missing, str(missing))
bad = []
for c in cubes:
    for x in c["terms"]:
        if x.get("quote") and x.get("post") in posts and norm(x["quote"]) not in norm(posts[x["post"]]["text"]):
            bad.append(f'{c["route"]} term {x["k"]}')
    for x in c["log"]:
        for frag in (x.get("excerpt") or "").split("[…]"):
            if frag.strip() and x.get("post") in posts and norm(frag) not in norm(posts[x["post"]]["text"]):
                bad.append(f'{c["route"]} log {x["post"]}')
check("every quote on a cube page is word for word in its post", not bad, str(bad))
check("no cube page says @bitcoinerrrrr lost the Merge cube", "bitcoinerrrrr" not in [c["bet"] for c in cubes if "Merge" in c["title"]])

# ---- hexicans: the money bets ----
hx, pls = assemble.load_hexicans()
check("hexicans.json: ids unique, camp hex or pls, paid true/false/null", len({b["id"] for b in hx}) == len(hx) and all(b["camp"] in ("hex", "pls") and b["paid"] in (True, False, None, "partial") for b in hx))
src = lambda t: norm(posts[t["post"]].get("image_text", "") if t.get("image") else posts[t["post"]]["text"])
check("hexicans: every quote is word for word in its post (or its screenshot)", all(t["post"] in posts and norm(t["quote"]) in src(t) for b in hx for t in b["terms"]),
      str([(b["id"], t["quote"][:30]) for b in hx for t in b["terms"] if t["post"] not in posts or norm(t["quote"]) not in src(t)]))
check("hexicans: money received adds up from the bets", sum(b.get("paid_amount") or 0 for b in hx) == 10399, str(sum(b.get("paid_amount") or 0 for b in hx)))
check("hexicans: stakes add up to the sheet's $152,000", sum(b["stake"] for b in hx) == 152000, str(sum(b["stake"] for b in hx)))
check("hexicans: the panties stay in", any(b.get("stake_extra") == "her panties" for b in hx))
check("hexicans: seven bets in all, Hviid's two in one box", sum(len(b["sheet"]) for b in hx) == 7 and len(next(b for b in hx if b["id"] == "hviid")["sheet"]) == 2)
check("hexicans: screenshot quotes say who said them", all(t.get("by") for b in hx for t in b["terms"] if t.get("image")))
hx_imgs = [b["avatar"] for b in hx if b.get("avatar")] + [e["file"] for b in hx for e in b.get("exhibits", [])] + ["debt-square.jpg"]
check("hexicans: every image it shows is in deploy/img/hexicans", all((ROOT / "deploy" / "img" / "hexicans" / f).is_file() for f in hx_imgs), str([f for f in hx_imgs if not (ROOT / "deploy" / "img" / "hexicans" / f).is_file()]))
check("hexicans: every exhibit points at an archived post", all(e["post"] in posts for b in hx for e in b.get("exhibits", [])))
check("pls_daily.json: no day at or above $0.001 (every PLS bet's line)", all(v < 0.001 for _, v in pls["prices"]), str(max(pls["prices"], key=lambda x: x[1])))

# ---- built pages are what the data builds ----
jamesob = (ROOT / "deploy" / "jamesob.html").read_text(encoding="utf-8")
front = (ROOT / "deploy" / "index.html").read_text(encoding="utf-8")
check("deploy/jamesob.html is built from data/", jamesob == assemble.build_exhibit(items, ladder), "run python3 -I build/assemble.py")
check("deploy/index.html is built from data/", front == assemble.build_root(bets), "run python3 -I build/assemble.py")
check("no stray index.html at the repository root", not (ROOT / "index.html").exists(), "the site lives in deploy/")
cube_pages = assemble.build_cube_pages(bets, cubes, posts)
stale = [p.name for p, html in cube_pages.items() if not p.exists() or p.read_text(encoding="utf-8") != html]
check("deploy/<cube>.html pages are built from data/", not stale, str(stale))
hexicans_html = assemble.build_hexicans(posts)
check("deploy/hexicans.html is built from data/", (ROOT / "deploy" / "hexicans.html").read_text(encoding="utf-8") == hexicans_html)

# ---- page constraints (both pages) ----
for name, html in [("jamesob", jamesob), ("front", front), ("hexicans", hexicans_html)] + [(p.stem, h) for p, h in cube_pages.items()]:
    check(f"{name}: no external <script src>", not re.search(r"<script[^>]+src=", html, re.I))
    check(f"{name}: only Google Fonts loaded externally", all("fonts.googleapis.com" in u for u in re.findall(r'<link[^>]+href="(https?://[^"]+)"', html)))
    check(f"{name}: one palette (no light theme, no theme toggle)", "theme-btn" not in html and "prefers-color-scheme" not in html and "data-theme" not in html)
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
check("front: links to every cube page", all(f'href="{b["page"]}"' in front for b in won))
check("front: [hexicans] in the top bar, before [github]", 0 <= front.find('href="/hexicans">[hexicans]') < front.find('[github]'))
check("cube pages: each links home and to the open bet", all('href="/"' in h and 'href="/jamesob"' in h for h in cube_pages.values()))
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
