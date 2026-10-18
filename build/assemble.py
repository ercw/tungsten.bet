"""Build tungsten.bet from data/ and build/.

    python3 -I build/assemble.py          # writes deploy/index.html and deploy/jamesob.html
    python3 -I build/assemble.py --check  # exit 1 if the deployed pages differ from what the data builds

The data is the source of truth:
    data/items.json   the 23 AI results on the James page (edit these, then rebuild)
    data/ladder.json  the author's four ladder ratings per item
    data/bets.json    Eric's tungsten bets: the cubes he has announced winning, and the open ones
    data/cubes.json   one page per won cube: the terms, the thread and what was not checked
    data/posts.json   the text of every post those pages quote, as fetched from x.com
The templates hold everything else:
    build/template.html   the James page; /*ITEMS*/ and /*LADDER*/ are replaced by the data blocks
    build/root.html       the front page; /*STYLE*/ takes the James page's stylesheet so the two stay
                          in one visual system, /*SHELF*/ the pyramid of cubes, /*TROPHIES*/ the cubes won,
                          /*OPEN*/ the open bets, /*RECORD*/ the tally
    build/cube.html       one cube page (tungsten.bet/adam and the others), filled from cubes.json and posts.json
    build/cube.js         the ASCII cube renderer, pasted into every page where /*CUBE*/ stands
"""
import html as H
import json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA, BUILD, DEPLOY = ROOT / "data", ROOT / "build", ROOT / "deploy"


def load():
    items = json.loads((DATA / "items.json").read_text(encoding="utf-8"))
    ladder = json.loads((DATA / "ladder.json").read_text(encoding="utf-8"))
    bets = json.loads((DATA / "bets.json").read_text(encoding="utf-8"))
    return items, ladder, bets


def load_cubes():
    cubes = json.loads((DATA / "cubes.json").read_text(encoding="utf-8"))
    posts = json.loads((DATA / "posts.json").read_text(encoding="utf-8"))
    return cubes, posts


def items_block(items):
    return "[\n" + ",\n".join(json.dumps(e, ensure_ascii=False, separators=(",", ":")) for e in items) + "\n]"


def ladder_block(ladder):
    return "{\n" + ",\n".join(f"  {json.dumps(k)}: {json.dumps(v, ensure_ascii=False)}" for k, v in ladder.items()) + "\n}"


def cube_js():
    return (BUILD / "cube.js").read_text(encoding="utf-8").rstrip("\n")


def build_exhibit(items, ladder):
    tpl = (BUILD / "template.html").read_text(encoding="utf-8")
    for ph in ("/*ITEMS*/", "/*LADDER*/", "/*CUBE*/"):
        assert tpl.count(ph) == 1, f"template placeholder {ph} missing"
    return (tpl.replace("/*ITEMS*/", items_block(items), 1).replace("/*LADDER*/", ladder_block(ladder), 1)
            .replace("/*CUBE*/", cube_js(), 1))


STATUS = {"won": ("WON", "won"), "lost": ("LOST", "lost"), "open": ("OPEN", "open")}
MON = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def day(d):
    """2024-01-15 -> 15 Jan 2024"""
    y, m, dd = d.split("-")
    return f"{int(dd)} {MON[int(m) - 1]} {y}"


def who(b):
    c = b["counterparty"]
    name, handle = c.get("name", ""), c.get("handle", "")
    if handle:
        link = f'<a href="https://x.com/{H.escape(handle)}" target="_blank" rel="noopener">@{H.escape(handle)}</a>'
        return f"{H.escape(name)} ({link})" if name else link
    return H.escape(name)


def sources(b):
    return " ".join(f'<a href="{H.escape(s["url"])}" target="_blank" rel="noopener" title="{H.escape(s["label"])}">[{i}]</a>'
                    for i, s in enumerate(b.get("sources", []), 1))


def quote(b):
    q = f'<q>{H.escape(b["claim"])}</q>'
    if b.get("claim_url"):
        q += f' <a class="dim" href="{H.escape(b["claim_url"])}" target="_blank" rel="noopener">[x.com]</a>'
    return q


def trophy_row(b):
    note = f'<br><span class="dim">{H.escape(b["note"])}</span>' if b.get("note") else ""
    page = f' <a href="{H.escape(b["page"])}">[the whole bet]</a>' if b.get("page") else ""
    return (f'<tr id="bet-{H.escape(b["id"])}"><td class="n">#{b["n"]}</td><td class="when">{day(b["announced"])}</td>'
            f'<td>{who(b)}</td><td class="bet">{quote(b)}{note}{page}</td><td class="src">{sources(b)}</td></tr>')


def open_row(b):
    note = f'<br><span class="dim">{H.escape(b["note"])}</span>' if b.get("note") else ""
    return (f'<li id="bet-{H.escape(b["id"])}"><span class="when">{day(b["opened"])} <span class="dim">→ {day(b["settles"])}</span></span>'
            f'<span>{who(b)}: {quote(b)}{note} <span class="src">{sources(b)}</span></span></li>')


def slot(n, b):
    """One cube in the pyramid. Each links to its own page."""
    handle = H.escape(b["counterparty"]["handle"])
    if b["status"] == "open":
        href, cls, when = H.escape(b["page"]), "slot wip", "in progress"
    else:
        href, cls, when = H.escape(b["page"]), "slot", day(b["announced"]).split(" ", 1)[1]
    return (f'<a class="{cls}" href="{href}"><canvas class="cubelet" aria-hidden="true"></canvas>'
            f'<span class="cap"><b>#{n}</b> @{handle}<br><span class="dim">{when}</span></span></a>')


def shelf(bets):
    """The won cubes, oldest at the base, stacked as a pyramid; the open bets sit on top, still in progress.
    Tiers are emitted bottom first (CSS reverses them), so the reading order runs #1, #2, #3 ..."""
    won = sorted((b for b in bets if b["status"] == "won"), key=lambda b: b["n"])
    cubes = won + [b for b in bets if b["status"] == "open"]
    base = 1
    while base * (base + 1) // 2 < len(cubes):
        base += 1
    tiers, i = [], 0
    for width in range(base, 0, -1):
        row = cubes[i:i + width]
        if row:
            tiers.append('<div class="tier">' + "".join(slot(i + j + 1, b) for j, b in enumerate(row)) + "</div>")
        i += width
    return f'<div class="tiers" style="--base:{base}">' + "\n".join(tiers) + "</div>"


def record(bets):
    return {k: sum(1 for b in bets if b["status"] == k) for k in STATUS}


def build_root(bets):
    tpl = (BUILD / "root.html").read_text(encoding="utf-8")
    style = stylesheet()
    for ph in ("/*STYLE*/", "/*SHELF*/", "/*TROPHIES*/", "/*OPEN*/", "/*RECORD*/", "/*SOURCES*/", "/*CUBE*/"):
        assert tpl.count(ph) == 1, f"root placeholder {ph} missing"
    n = record(bets)
    tally = (f'<b>{n["won"]}</b> cubes won &nbsp;·&nbsp; <b class="{"hot" if n["lost"] else ""}">{n["lost"]}</b> lost'
             f' &nbsp;·&nbsp; <b>{n["open"]}</b> open')
    won = sorted((b for b in bets if b["status"] == "won"), key=lambda b: b["n"])
    lost = [b for b in bets if b["status"] == "lost"]
    trophies = "\n".join(trophy_row(b) for b in won + lost)
    opened = "\n".join(open_row(b) for b in bets if b["status"] == "open")
    seen, srcs = set(), []
    for b in bets:
        for s in b.get("sources", []):
            if s["url"] not in seen:
                seen.add(s["url"])
                srcs.append(f'<li><a href="{H.escape(s["url"])}" target="_blank" rel="noopener">{H.escape(s["label"])}</a> <span class="dim">{H.escape(s["url"])}</span></li>')
    return (tpl.replace("/*STYLE*/", style, 1).replace("/*TROPHIES*/", trophies, 1).replace("/*OPEN*/", opened, 1)
            .replace("/*RECORD*/", tally, 1).replace("/*SOURCES*/", "\n".join(srcs), 1)
            .replace("/*SHELF*/", shelf(bets), 1).replace("/*CUBE*/", cube_js(), 1))


def stylesheet():
    return re.search(r"<style>\n(.*?)\n</style>", (BUILD / "template.html").read_text(encoding="utf-8"), re.S).group(1)


def x_link(url):
    return f'<a class="x" href="{H.escape(url)}" target="_blank" rel="noopener">[x.com]</a>'


def term_row(t, posts):
    body = H.escape(t.get("pre", ""))
    if t.get("quote"):
        body += f'<q>{H.escape(t["quote"])}</q>'
    body += H.escape(t.get("after", ""))
    if t.get("post"):
        body += " " + x_link(posts[t["post"]]["url"])
    return f'        <dt>{H.escape(t["k"])}</dt><dd>{body}</dd>'


def log_row(e, posts):
    if "sys" in e:
        detail = f', {H.escape(e["detail"])}' if e.get("detail") else ""
        return f'        <li class="sys"><span class="ts"></span><span class="msg">-!- <b>{H.escape(e["sys"])}</b>{detail}</span></li>'
    p = posts[e["post"]]
    msg = H.escape(e.get("excerpt", p["text"])).replace("[…]", '<span class="gap">[…]</span>')
    if e.get("note"):
        msg += f' <span class="gap">[{H.escape(e["note"])}]</span>'
    nick = "nick" if p["user"] == "ercwl" else "nick j"
    return (f'        <li><a class="ts" href="{H.escape(p["url"])}" target="_blank" rel="noopener">{p["at"]}</a>'
            f'<span class="{nick}">&lt;{H.escape(p["user"])}&gt;</span><span class="msg">{msg}</span></li>')


def caveat_row(c):
    link = f' <a href="{H.escape(c["href"])}"{" target=\"_blank\" rel=\"noopener\"" if c["href"].startswith("http") else ""}>{H.escape(c["label"])}</a>' if c.get("href") else ""
    return f'      <li>{H.escape(c["text"])}{link}</li>'


def build_cube_pages(bets, cubes, posts):
    """One page per won cube, at tungsten.bet/<route>."""
    tpl = (BUILD / "cube.html").read_text(encoding="utf-8")
    by_bet = {b["id"]: b for b in bets}
    won = sorted((b for b in bets if b["status"] == "won"), key=lambda b: b["n"])
    total = len(won)
    pages = {}
    for c in cubes:
        b = by_bet[c["bet"]]
        name = b["counterparty"].get("name") or "@" + b["counterparty"]["handle"]
        nav = []
        for w in won:
            cw = next(x for x in cubes if x["bet"] == w["id"])
            label = H.escape(w["counterparty"].get("name") or "@" + w["counterparty"]["handle"]) + f' <span class="dim">· {H.escape(cw["title"])}</span>'
            if w["id"] == c["bet"]:
                nav.append(f'        <li><span class="n">#{w["n"]}</span><span aria-current="page">{label} <span class="here">(this page)</span></span></li>')
            else:
                nav.append(f'        <li><span class="n">#{w["n"]}</span><a href="{H.escape(w["page"])}">{label}</a></li>')
        for o in (b for b in bets if b["status"] == "open"):
            nav.append(f'        <li><span class="n">open</span><a href="{H.escape(o["page"])}">{H.escape(o["counterparty"]["name"])} <span class="dim">· still open, not a cube yet</span></a></li>')
        fill = {
            "/*TITLE*/": H.escape(f'Cube #{b["n"]}: {c["title"]} · tungsten.bet'),
            "/*DESC*/": H.escape(c["lede"]),
            "/*ROUTE*/": H.escape(c["route"]),
            "/*CAP*/": f'cube #{b["n"]} of {total}',
            "/*KICKER*/": f'Eric Wall\'s tungsten cube #{b["n"]}',
            "/*H1*/": H.escape(c["title"]),
            "/*LEDE*/": H.escape(c["lede"]),
            "/*META*/": f'Won from {who(b)}. Announced {day(b["announced"])}.',
            "/*TERMS*/": "\n".join(term_row(t, posts) for t in c["terms"]),
            "/*LOG*/": "\n".join(log_row(e, posts) for e in c["log"]),
            "/*CAVEATS*/": "\n".join(caveat_row(x) for x in c["caveats"]),
            "/*NAV*/": "\n".join(nav),
            "/*TURN*/": f'{0.4 + b["n"] * 1.37:.2f}',
            "/*STYLE*/": stylesheet(),
        }
        html = tpl
        for ph, v in fill.items():
            assert html.count(ph) == 1, f"cube placeholder {ph} missing"
            html = html.replace(ph, v, 1)
        assert html.count("/*CUBE*/") == 1, "cube placeholder /*CUBE*/ missing"
        pages[DEPLOY / f'{c["route"]}.html'] = html.replace("/*CUBE*/", cube_js(), 1)
    return pages


def main(argv):
    items, ladder, bets = load()
    cubes, posts = load_cubes()
    out = {DEPLOY / "jamesob.html": build_exhibit(items, ladder), DEPLOY / "index.html": build_root(bets)}
    out.update(build_cube_pages(bets, cubes, posts))
    if "--check" in argv:
        stale = [p.name for p, s in out.items() if not p.exists() or p.read_text(encoding="utf-8") != s]
        if stale:
            sys.exit(f"stale: {', '.join(stale)} — run python3 -I build/assemble.py")
        print("deploy/ is up to date with data/")
        return
    for p, s in out.items():
        p.write_text(s, encoding="utf-8")
        print(f"wrote {p.relative_to(ROOT)} ({len(s):,} bytes)")
    print(f"{len(items)} items, {len(ladder)} ladder rows, {len(bets)} bets, {len(cubes)} cube pages, {len(posts)} archived posts")


if __name__ == "__main__":
    main(sys.argv[1:])
