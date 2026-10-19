"""Build tungsten.bet from data/ and build/.

    python3 -I build/assemble.py          # writes deploy/index.html and deploy/jamesob.html
    python3 -I build/assemble.py --check  # exit 1 if the deployed pages differ from what the data builds

The data is the source of truth:
    data/items.json   the 23 AI results on the James page (edit these, then rebuild)
    data/ladder.json  the author's four ladder ratings per item
    data/bets.json    Eric's tungsten bets: the cubes he has announced winning, and the open ones
    data/cubes.json   one page per won cube: the terms, the thread and what was not checked
    data/posts.json   the text of every post those pages quote, as fetched from x.com
    data/hexicans.json  the money bets with HEX and PulseChain holders (tungsten.bet/hexicans)
    data/pls_daily.json PLS daily prices from PulseX, launch to the last deadline
The templates hold everything else:
    build/template.html   the James page; /*ITEMS*/ and /*LADDER*/ are replaced by the data blocks
    build/root.html       the front page; /*STYLE*/ takes the James page's stylesheet so the two stay
                          in one visual system, /*SHELF*/ the pyramid of cubes, /*TROPHIES*/ the cubes won,
                          /*OPEN*/ the open bets, /*RECORD*/ the tally
    build/cube.html       one cube page (tungsten.bet/adam and the others), filled from cubes.json and posts.json
    build/cube.js         the ASCII cube renderer, pasted into every page where /*CUBE*/ stands
    build/hexicans.html   the money-bets page; build/assets/ holds the HEX and PulseChain logos it draws as ASCII
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


MON_LONG = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]


def load_hexicans():
    bets = json.loads((DATA / "hexicans.json").read_text(encoding="utf-8"))
    pls = json.loads((DATA / "pls_daily.json").read_text(encoding="utf-8"))
    return bets, pls


def data_uri(path):
    import base64
    return "data:image/png;base64," + base64.b64encode(path.read_bytes()).decode()


PLS_STOPS = [(0, 212, 255), (59, 91, 255), (138, 0, 255), (230, 0, 230), (255, 42, 85)]


def grad(stops, f):
    f = max(0.0, min(1.0, f)) * (len(stops) - 1)
    i = min(int(f), len(stops) - 2)
    a, b, t = stops[i], stops[i + 1], f - i
    return "#%02x%02x%02x" % tuple(round(a[k] + (b[k] - a[k]) * t) for k in range(3))


def pls_chart(prices, deadlines):
    """PLS daily price on a log scale against the $0.001 line, as coloured characters."""
    import math
    W, H = 60, 13
    lo, hi = math.log10(1e-5), math.log10(2e-3)
    step = (hi - lo) / (H - 1)
    rowof = lambda v: max(0, min(H - 1, round((math.log10(max(v, 1e-9)) - lo) / step)))
    per = len(prices) / W
    cols = []
    for c in range(W):
        chunk = prices[int(c * per):int((c + 1) * per)] or prices[-1:]
        cols.append((chunk[0][0], chunk[-1][0], max(v for _, v in chunk)))
    r_line, r_sac = rowof(1e-3), rowof(1e-4)
    sp = lambda cls, t: f'<span class="{cls}">{t}</span>'
    out = []
    for r in range(H - 1, -1, -1):
        label = {r_line: "$0.001 ", r_sac: "0.0001 ", 0: "0.00001"}.get(r, "       ")
        row = sp("ax", label + ("┤" if r in (r_line, r_sac, 0) else "│"))
        for c, (_, _, v) in enumerate(cols):
            h, col = rowof(v), grad(PLS_STOPS, c / (W - 1))
            if r == h:
                row += f'<span style="color:{col}">█</span>'
            elif r < h:
                row += f'<span style="color:{col};opacity:.4">▒</span>'
            elif r == r_line:
                row += sp("line", "━")
            elif r == r_sac:
                row += sp("sac", "┄")
            else:
                row += " "
        if r == r_line:
            row += sp("line", " 10×")
        out.append(row)
    out.append(sp("ax", "       └" + "─" * W))
    marks = [" "] * W
    for d in deadlines:
        for c, (a, b, _) in enumerate(cols):
            if a <= d <= b or (c == W - 1 and d > b):
                marks[c] = sp("dl", "▲"); break
    out.append("        " + "".join(marks))
    yrs = [" "] * W
    for c, (a, _, _) in enumerate(cols):
        if c == 0 or a[5:7] == "01" and cols[c - 1][0][:4] != a[:4]:
            lab = a[:7] if c == 0 else a[:4]
            for j, ch in enumerate(lab):
                if c + j < W: yrs[c + j] = ch
    out.append("        " + sp("ax", "".join(yrs)))
    top = max(prices, key=lambda x: x[1])
    return "\n".join(out), top


def hx_day(d):
    y, m, dd = d.split("-")
    return f"{int(dd)} {MON[int(m) - 1]} {y}"


def build_hexicans(posts):
    bets, pls = load_hexicans()
    tpl = (BUILD / "hexicans.html").read_text(encoding="utf-8")
    bets = sorted(bets, key=lambda b: (b["entered"], -b["stake"]))
    total = sum(b["stake"] for b in bets)
    paid_yes = [b for b in bets if b["paid"] is True]
    paid_no = [b for b in bets if b["paid"] is False]
    unknown = [b for b in bets if b["paid"] is None]
    partial = [b for b in bets if b["paid"] == "partial"]
    chips = "".join(f'<span class="{"h" if b["camp"] == "hex" else "p"}">■</span>' for b in bets)
    if unknown:
        got = sum(b.get("paid_amount") or 0 for b in bets)
        nothing = sum(1 for b in unknown if not b.get("paid_amount"))
        def who_paid(b):
            how = "paid in full" if b["paid"] is True else "paid ${:,} and stopped".format(b["paid_amount"])
            return H.escape(b["who"]["name"]) + " " + how
        answer = (f'<span class="answer">${got:,}</span> <span class="dim">of ${total:,} received so far. '
                  + "; ".join(who_paid(b) for b in bets if b.get("paid_amount"))
                  + f'. No payment found from the other {nothing}.</span>')
    else:
        answer = (f'<span class="answer">{len(paid_yes)} of {len(bets)}</span> '
                  f'<span class="dim">${sum(b["stake"] for b in paid_yes):,} of ${total:,} paid.</span>')
    score = f"""      <dl class="score">
        <dt>bets taken</dt><dd><span class="big">{len(bets)}</span> <span class="chips" aria-hidden="true">{chips}</span> <span class="dim">{sum(b["camp"] == "hex" for b in bets)} on HEX, {sum(b["camp"] == "pls" for b in bets)} on PulseChain</span></dd>
        <dt>staked against Eric</dt><dd><span class="big">${total:,}</span> <span class="dim">plus one pair of panties, delivered</span></dd>
        <dt>won by Eric, by the terms</dt><dd><span class="big">{len(bets)} of {len(bets)}</span></dd>
        <dt>paid</dt><dd>{answer}</dd>
        <dt>Eric, December 2024</dt><dd><q>{H.escape(posts["1872772808927002626"]["text"].split(chr(10))[2])}</q> <a class="x" href="{H.escape(posts["1872772808927002626"]["url"])}" target="_blank" rel="noopener">[x.com]</a></dd>
      </dl>"""
    deadlines = sorted({b["deadline"] for b in bets if b["camp"] == "pls"})
    chart, top = pls_chart(pls["prices"], deadlines)
    chart_alt = (f"PLS daily price from {hx_day(pls['prices'][0][0])} to {hx_day(pls['prices'][-1][0])} on a log scale. "
                 f"Its highest was ${top[1]:.6f} on {hx_day(top[0])}, its first week. It never reached the $0.001 line.")
    key = ("█ PLS, the highest daily price in each column of about twelve days. ━ $0.001, ten times the sacrifice price. "
           "┄ $0.0001, the sacrifice price. ▲ deadlines: " + ", ".join(hx_day(d) for d in deadlines) + ". "
           f"Highest daily price ever: ${top[1]:.6f}, on {hx_day(top[0])}.")
    def quote(t):
        p = posts[t["post"]]
        if t.get("image"):
            return (f'<q>{H.escape(t["quote"])}</q> <span class="dim">in a screenshot posted by @{H.escape(p["user"])}, {hx_day(p["at"][:10])}</span> '
                    f'<a class="x" href="{H.escape(p["url"])}" target="_blank" rel="noopener">[x.com]</a>')
        arch = f' <a class="x" href="{H.escape(p["archive"])}" target="_blank" rel="noopener">[archive]</a>' if p.get("archive") else ""
        return (f'<q>{H.escape(t["quote"])}</q> <span class="dim">@{H.escape(p["user"])}, {hx_day(p["at"][:10])}</span> '
                f'<a class="x" href="{H.escape(p["url"])}" target="_blank" rel="noopener">[x.com]</a>{arch}')
    def exhibit(e, cls=""):
        p = posts[e["post"]]
        return (f'<figure class="ex {cls}"><a href="{H.escape(p["url"])}" target="_blank" rel="noopener"><img src="/img/hexicans/{H.escape(e["file"])}" '
                f'alt="{H.escape(e["alt"])}" loading="lazy"></a><figcaption>{H.escape(e["cap"])} <a class="x" href="{H.escape(p["url"])}" target="_blank" rel="noopener">[x.com]</a></figcaption></figure>')
    arts = []
    for i, b in enumerate(bets, 1):
        who = f'{H.escape(b["who"]["name"])} <a href="https://x.com/{H.escape(b["who"]["handle"])}" target="_blank" rel="noopener">@{H.escape(b["who"]["handle"])}</a>'
        stake = f'${b["stake"]:,}' + (f' + <span class="extra">{H.escape(b["stake_extra"])}</span>' if b.get("stake_extra") else "") + (f' <span class="dim">vs Eric\'s ${b["eric_stake"]:,}</span>' if b.get("eric_stake") else "")
        sheet_out = f'<b>{H.escape(b["sheet_outcome"])}</b>' if b["sheet_outcome"] else '<span class="dim">no outcome entered</span>'
        paid = {True: '<span class="paid yes">PAID</span>', False: '<span class="paid no">NOT PAID</span>', "partial": '<span class="paid no">PARTLY</span>', None: '<span class="paid unknown">?</span>'}[b["paid"]]
        if b.get("paid_note"): paid += f' <span class="dim">{H.escape(b["paid_note"])}</span>'
        if b.get("paid_post"): paid += f' <a class="x" href="{H.escape(posts[b["paid_post"]]["url"])}" target="_blank" rel="noopener">[x.com]</a>'
        note = f'\n        <p class="note">{H.escape(b["note"])}</p>' if b.get("note") else ""
        if b.get("avatar"):
            av = f"/img/hexicans/{b['avatar']}"
            who_row = (f'<div class="who-row"><span class="av" tabindex="0" aria-label="{H.escape(b["who"]["name"])}\'s profile picture">'
                       f'<canvas class="avc" data-src="{av}" data-mode="photo" aria-hidden="true"></canvas><img src="{av}" alt="" loading="lazy"></span><h3>{who}</h3></div>')
        else:
            who_row = f'<h3>{who}</h3>'
        exs = "".join(exhibit(e) for e in b.get("exhibits", []))
        arts.append(f"""      <article class="box hbet {b["camp"]}" id="bet-{H.escape(b["id"])}">
        <span class="box-t">#{i} · <span class="tag">{"HEX" if b["camp"] == "hex" else "PulseChain"}</span></span><span class="box-t r">{stake}</span>
        {who_row}
        <dl class="kv">
          <dt>the bet</dt><dd>{H.escape(b["bet"])}</dd>
          <dt>their words</dt><dd>{"<br>".join(quote(t) for t in b["terms"])}</dd>
          <dt>window</dt><dd>{hx_day(b["entered"])} to {hx_day(b["deadline"])}</dd>
          <dt>what happened</dt><dd>{H.escape(b["check"])} <a class="x" href="{H.escape(b["check_url"])}" target="_blank" rel="noopener">[prices]</a></dd>
          <dt>Eric's sheet</dt><dd><q>{H.escape(b["sheet"])}</q> {sheet_out}</dd>
          <dt>paid</dt><dd>{paid}</dd>
        </dl>{exs}{note}
      </article>""")
    lede = (f"Between 2022 and 2024, seven HEX and PulseChain holders bet Eric ${total:,} that their coins would set new highs or go up "
            "tenfold. None came close, so by their own terms Eric won all seven. That leaves the question in the title.")
    fill = {
        "/*STYLE*/": stylesheet(), "/*DESC*/": H.escape(lede), "/*LEDE*/": H.escape(lede),
        "/*SCORE*/": score + "\n      " + exhibit({"file": "debt-square.jpg", "post": "1953841425419804978",
                                                  "alt": "A large purple square with a tiny yellow square in its corner",
                                                  "cap": "Eric, 8 August 2025, after Hviid's first $100: “The yellow square in the right diagram represents debt paid so far visually.”"}, "score-ex"),
        "/*CHART*/": chart, "/*CHARTALT*/": H.escape(chart_alt), "/*CHARTKEY*/": H.escape(key), "/*BETS*/": "\n".join(arts),
        "/*HEXLOGO*/": data_uri(BUILD / "assets" / "hex.png"), "/*PLSLOGO*/": data_uri(BUILD / "assets" / "pulsechain.png"),
    }
    html = tpl
    for ph, v in fill.items():
        assert html.count(ph) >= 1, f"hexicans placeholder {ph} missing"
        html = html.replace(ph, v)
    return html


def main(argv):
    items, ladder, bets = load()
    cubes, posts = load_cubes()
    out = {DEPLOY / "jamesob.html": build_exhibit(items, ladder), DEPLOY / "index.html": build_root(bets)}
    out.update(build_cube_pages(bets, cubes, posts))
    out[DEPLOY / "hexicans.html"] = build_hexicans(posts)
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
