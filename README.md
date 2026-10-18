# tungsten.bet

Eric Wall bets a tungsten cube against people who are sure. The claim is public, the test for changing their mind is their own, the deadline is fixed, and the loser pays in metal.

- **tungsten.bet** — what this is, how it works, and the record.
- **tungsten.bet/jamesob** — the open bet with James O'Beirne (31 May 2025 → 31 May 2028): the AI results of 2022–2026 laid on the ladder James named, rung by rung, with a source and a caveat on every item.

Corrections are welcome as pull requests. Read [CONTRIBUTING.md](CONTRIBUTING.md) first: primary sources only, caveats are append-only, nothing gets stronger than its source.

## Layout

```
data/items.json      the items on the James page (the source of truth; edit here)
data/ladder.json     the author's four ladder ratings per item
data/bets.json       the bet record on the front page
build/template.html  the James page template; build/root.html the front page template
build/assemble.py    builds deploy/ from data/ and build/
deploy/              what Vercel serves: index.html, jamesob.html, vercel.json
tests/               check_static.py (data, built pages, page rules); check_revision.py (PR rules)
AUDIT-2026-10-18.md  the source-by-source audit the current numbers rest on
ACCEPTANCE.md        the build log; HANDOFF-physics-exhibit.md the original brief
```

## Build and check

```bash
python3 -I build/assemble.py && python3 -I tests/check_static.py
```

Both pages are single self-contained HTML files: inline CSS and JS, no framework, no build step beyond the splice above. The only external requests are Google Fonts.

## Deploy

`deploy/` is a Vercel project (`tungsten-bet`). From that folder, `vercel --prod` publishes it. Clean URLs are on, so `deploy/jamesob.html` is served at `/jamesob`.
