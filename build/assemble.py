"""Build tungsten.bet from data/ and build/.

    python3 -I build/assemble.py          # writes deploy/index.html and deploy/jamesob.html
    python3 -I build/assemble.py --check  # exit 1 if the deployed pages differ from what the data builds

The data is the source of truth:
    data/items.json   the 23 AI results on the James page (edit these, then rebuild)
    data/ladder.json  the author's four ladder ratings per item
    data/bets.json    the record of tungsten bets on the front page
The templates hold everything else:
    build/template.html   the James page; /*ITEMS*/ and /*LADDER*/ are replaced by the data blocks
    build/root.html       the front page; /*STYLE*/ takes the James page's stylesheet so the two stay
                          in one visual system, /*BETS*/ the record table, /*RECORD*/ the tally
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


STATUS = {"won": ("WON", "won"), "lost": ("LOST", "lost"), "open": ("OPEN", "open"), "unrecorded": ("SETTLED, LINK WANTED", "unrecorded")}


def who(b):
    c = b["counterparty"]
    name, handle = c.get("name", ""), c.get("handle", "")
    if handle:
        link = f'<a href="https://x.com/{H.escape(handle)}" target="_blank" rel="noopener">@{H.escape(handle)}</a>'
        return f"{H.escape(name)} ({link})" if name else link
    return H.escape(name)


def bet_row(b):
    label, cls = STATUS[b["status"]]
    when = H.escape(b.get("opened", ""))
    if b.get("settles"):
        when += f' <span class="dim">→ {H.escape(b["settles"])}</span>'
    elif b.get("settled"):
        when += f' <span class="dim">→ {H.escape(b["settled"])}</span>'
    srcs = " ".join(f'<a href="{H.escape(s["url"])}" target="_blank" rel="noopener" title="{H.escape(s["label"])}">[{i}]</a>'
                    for i, s in enumerate(b.get("sources", []), 1))
    claim = H.escape(b["claim"])
    if b.get("page"):
        claim += f' <a href="{H.escape(b["page"])}">[ the page ]</a>'
    note = f'<br><span class="dim">{H.escape(b["note"])}</span>' if b.get("note") else ""
    wanted = f'<br><span class="dim">Wanted: {H.escape(b["wanted"])}.</span>' if b.get("wanted") else ""
    return (f'<tr id="bet-{H.escape(b["id"])}"><td class="when">{when}</td><td>{who(b)}</td>'
            f'<td class="claim">{claim}{note}{wanted}</td><td>{H.escape(b["stake"])}</td>'
            f'<td class="st {cls}">{label}</td><td class="src">{srcs}</td></tr>')


def record(bets):
    n = {k: sum(1 for b in bets if b["status"] == k) for k in STATUS}
    return n


def build_root(bets):
    tpl = (BUILD / "root.html").read_text(encoding="utf-8")
    style = re.search(r"<style>\n(.*?)\n</style>", (BUILD / "template.html").read_text(encoding="utf-8"), re.S).group(1)
    for ph in ("/*STYLE*/", "/*BETS*/", "/*RECORD*/", "/*SOURCES*/"):
        assert tpl.count(ph) == 1, f"root placeholder {ph} missing"
    n = record(bets)
    tally = (f'<b>{len(bets)}</b> bets &nbsp;·&nbsp; <b>{n["won"]}</b> won &nbsp;·&nbsp; <b class="{"hot" if n["lost"] else ""}">{n["lost"]}</b> lost'
             f' &nbsp;·&nbsp; <b>{n["open"]}</b> open' + (f' &nbsp;·&nbsp; <b>{n["unrecorded"]}</b> settled, link wanted' if n["unrecorded"] else ""))
    rows = "\n".join(bet_row(b) for b in bets)
    seen, sources = {}, []
    for b in bets:
        for s in b.get("sources", []):
            if s["url"] not in seen:
                seen[s["url"]] = len(sources) + 1
                sources.append(f'<li><a href="{H.escape(s["url"])}" target="_blank" rel="noopener">{H.escape(s["label"])}</a> <span class="dim">{H.escape(s["url"])}</span></li>')
    return (tpl.replace("/*STYLE*/", style, 1).replace("/*BETS*/", rows, 1)
            .replace("/*RECORD*/", tally, 1).replace("/*SOURCES*/", "\n".join(sources), 1))


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
