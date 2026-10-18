# tungsten.bet

Eric Wall bets a tungsten cube against people who are sure. The claim is public, the test for changing their mind is their own, the deadline is fixed, and the loser pays in metal.

- **tungsten.bet** — what this is, how it works, and the record.
- **tungsten.bet/adam, /keroles, /bitcoinerrrrr, /brad, /midas** — one page per cube won: the terms in both sides' words, the thread with times, and what was not checked.
- **tungsten.bet/jamesob** — the open bet with James O'Beirne (31 May 2025 → 31 May 2028): the AI results since the bet, rated step by step against the test James named, with the results from before the bet in a section of their own and a source and a caveat on every item.

Corrections are welcome as pull requests. Read [CONTRIBUTING.md](CONTRIBUTING.md) first: primary sources only, caveats are append-only, nothing gets stronger than its source.

## Layout

```
data/items.json      the items on the James page (the source of truth; edit here)
data/ladder.json     the author's four ladder ratings per item
data/bets.json       the cubes won and the open bets, on the front page
data/cubes.json      one page per cube won: terms, thread, what was not checked
data/posts.json      the text of every post the cube pages quote, as fetched from x.com
build/template.html  the James page template; build/root.html the front page template
build/cube.html      the cube page template; build/cube.js the ASCII cube every page draws
build/assemble.py    builds deploy/ from data/ and build/
deploy/              what Vercel serves: index.html, jamesob.html, the five cube pages, vercel.json
tests/               check_static.py (data, built pages, page rules); check_revision.py (PR rules)
SOURCES.md           the primary-source passages behind the corrections on the James page
```

## Build and check

```bash
python3 -I build/assemble.py && python3 -I tests/check_static.py
```

Every page is a single self-contained HTML file: inline CSS and JS, no framework, no build step beyond the splice above. The only external requests are Google Fonts.

## Deploy

`deploy/` is a Vercel project. From that folder, `vercel --prod` publishes it. Clean URLs are on, so `deploy/jamesob.html` is served at `/jamesob`.
