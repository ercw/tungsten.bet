# Contributing

tungsten.bet is a record of bets and, for each open bet, a page of evidence against the other side's own test. The point of the pages is that a sceptic can trust them. Every change is judged against that.

## The rules

1. **Primary sources only.** A change to a number, a date, a label or a caveat cites the document itself: the paper, the journal's correction notice, the repository, the post, the thread. A press article, a summary or an audit by a model is a lead, not a source. Say what passage you relied on.
2. **Caveats are append-only.** New facts are added to a caveat; nothing in it is removed or softened. If a caveat has become wrong, append the correction and say what changed and when. CI enforces this (`tests/check_revision.py`).
3. **Never make a claim stronger than its source.** If the paper says "estimated", the item says "estimated". A result that was challenged in print gets `contested: true` and the challenge in its caveat, with the challenge's citation.
4. **Labels have definitions.** `verification` is `peer-reviewed` (published in a reviewed venue), `preprint` (arXiv, ChemRxiv and the like, including a company's own preprint), or `company-reported` (a blog post, impact report or press release with no paper behind it). `llm` is true only when a language-model-class system did the proposing or coding. `physical` is true only when something ran on hardware, was synthesized, fabricated or deployed. `contested` is for a headline claim publicly challenged, not for ordinary disagreement.
5. **The ladder ratings are the author's.** `data/ladder.json` holds the four ratings per item (touched matter, AI necessary, huge leap, bears on qubits). A pull request may propose a change with its reasons; the maintainer decides, because the page says these are the author's reading.
6. **The verdict words on the James page are not computed.** They are the author's reading of where each of James's statements stands. Do not wire them to the data.

## Adding an item

Append to `data/items.json`. Ids are a letter and a number: `Q` quantum, `M` materials, `P` physics, `X` other. Fields:

| field | meaning |
|---|---|
| `date` | announcement or publication month, `YYYY-MM` |
| `title` | one line, the claim as the source states it |
| `domain` | `quantum`, `materials`, `plasma / fusion`, `atmospheric physics`, `fluids`, `theoretical physics`, `cryptography`, or a new one if needed |
| `tier` | 1 LLM-driven system produced a physical artifact; 2 non-LLM AI, physical and deployed; 3 LLM output, theory or simulation only |
| `llm`, `physical`, `quantum` | booleans as defined above; `quantum` means the result is about quantum computing or quantum physics |
| `verification` | see rule 4 |
| `contested` | `true` only when it applies; otherwise leave the field out |
| `who` | who did it and where it appeared |
| `what` | what was shown, with the numbers the source gives |
| `artifact` | what physical thing, if any, came out of it |
| `caveat` | what a sceptic should know; never empty |
| `P`, `H`, `W`, `C` | the score: physicality 0–10, horizon (`now`, `years`, `decades`, `someday`), weight 1–4, confidence 0–1; the scale is in the James page's footer |
| `url` | the primary source |

Then add the item's row to `data/ladder.json` (`matter`, `necessary` true/false/`"arguable"`, `leap` `none`/`early sign`/`leap`, `qubits`, and a one-line `why`), rebuild, and run the checks.

## Correcting the bet record

`data/bets.json` holds the front page's table. A row needs the posts where the bet was made and where it was settled. Rows marked `unrecorded` are known from a published profile only; the best pull request for them is the two links.

## Build and check

```bash
python3 -I build/assemble.py
```

```bash
python3 -I tests/check_static.py
```

Edit `data/` and `build/`, never `deploy/` by hand; `deploy/` is what the build writes and what Vercel serves. CI runs the same checks on every pull request, plus the revision rules against the base branch.
