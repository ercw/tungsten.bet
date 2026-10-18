"""Build tungsten.bet from data/ and build/.

    python3 -I build/assemble.py          # writes deploy/index.html and deploy/jamesob.html
    python3 -I build/assemble.py --check  # exit 1 if the deployed pages differ from what the data builds

The data is the source of truth:
    data/items.json   the 23 AI results on the James page (edit these, then rebuild)
    data/ladder.json  the author's four ladder ratings per item
    data/bets.json    Eric's tungsten bets: the cubes he has announced winning, and the open ones
The templates hold everything else:
    build/template.html   the James page; /*ITEMS*/ and /*LADDER*/ are replaced by the data blocks
    build/root.html       the front page; /*STYLE*/ takes the James page's stylesheet so the two stay
                          in one visual system, /*TROPHIES*/ the cubes won, /*OPEN*/ the open bets, /*RECORD*/ the tally
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


def items_block(items):
    return "[\n" + ",\n".join(json.dumps(e, ensure_ascii=False, separators=(",", ":")) for e in items) + "\n]"


def ladder_block(ladder):
    return "{\n" + ",\n".join(f"  {json.dumps(k)}: {json.dumps(v, ensure_ascii=False)}" for k, v in ladder.items()) + "\n}"


def build_exhibit(items, ladder):
    tpl = (BUILD / "template.html").read_text(encoding="utf-8")
    assert tpl.count("/*ITEMS*/") == 1 and tpl.count("/*LADDER*/") == 1, "template placeholders missing"
    return tpl.replace("/*ITEMS*/", items_block(items), 1).replace("/*LADDER*/", ladder_block(ladder), 1)


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
    return (f'<tr id="bet-{H.escape(b["id"])}"><td class="n">#{b["n"]}</td><td class="when">{day(b["announced"])}</td>'
            f'<td>{who(b)}</td><td class="bet">{quote(b)}{note}</td><td class="src">{sources(b)}</td></tr>')


def open_row(b):
    note = f'<br><span class="dim">{H.escape(b["note"])}</span>' if b.get("note") else ""
    return (f'<li id="bet-{H.escape(b["id"])}"><span class="when">{day(b["opened"])} <span class="dim">→ {day(b["settles"])}</span></span>'
            f'<span>{who(b)}: {quote(b)}{note} <span class="src">{sources(b)}</span></span></li>')


def record(bets):
    return {k: sum(1 for b in bets if b["status"] == k) for k in STATUS}


def build_root(bets):
    tpl = (BUILD / "root.html").read_text(encoding="utf-8")
    style = re.search(r"<style>\n(.*?)\n</style>", (BUILD / "template.html").read_text(encoding="utf-8"), re.S).group(1)
    for ph in ("/*STYLE*/", "/*TROPHIES*/", "/*OPEN*/", "/*RECORD*/", "/*SOURCES*/"):
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
            .replace("/*RECORD*/", tally, 1).replace("/*SOURCES*/", "\n".join(srcs), 1))


def main(argv):
    items, ladder, bets = load()
    out = {DEPLOY / "jamesob.html": build_exhibit(items, ladder), DEPLOY / "index.html": build_root(bets)}
    if "--check" in argv:
        stale = [p.name for p, s in out.items() if not p.exists() or p.read_text(encoding="utf-8") != s]
        if stale:
            sys.exit(f"stale: {', '.join(stale)} — run python3 -I build/assemble.py")
        print("deploy/ is up to date with data/")
        return
    for p, s in out.items():
        p.write_text(s, encoding="utf-8")
        print(f"wrote {p.relative_to(ROOT)} ({len(s):,} bytes)")
    print(f"{len(items)} items, {len(ladder)} ladder rows, {len(bets)} bets")


if __name__ == "__main__":
    main(sys.argv[1:])
