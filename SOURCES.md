# Source checks for tungsten.bet/jamesob

Twelve facts about the AI results on the James page were checked against primary sources on 18 October 2026. Each passage below is copied from the source; the item ids (M1, Q3, P9 …) are the ids in `data/items.json`.

**Method.** Each source was opened and the passage copied verbatim. Where a publisher page could not be opened, bibliographic facts come from publisher-deposited metadata (Crossref) and from OpenAlex, Semantic Scholar and the arXiv API. Figures in images were not read; only text.

**Could not open.** `pubs.rsc.org` (Materials Horizons, check 3) and `pubs.acs.org` (JACS, check 2) refused automated access. For those two the bibliographic facts come from Crossref and OpenAlex, the abstracts from ChemRxiv (the paper's own preprint) and from the arXiv API's DOI field; what each record did and did not show is stated under the check. The GNoME paper's DOI is `10.1038/s41586-023-06735-9`; the `-z` form does not resolve.

Verdicts: **VERIFIED**, **PARTLY VERIFIED** (which part, and why the rest is not), **NOT VERIFIED**, **COULD NOT OPEN**.

---

## 1. M1 (GNoME / A-Lab). Author correction 36 of 57; "novel" meant new to the platform; 736 are retrospective matches

**VERIFIED** (all three parts).

- Author Correction, Nature 650, E1, published 19 January 2026: https://www.nature.com/articles/s41586-025-09992-y (Crossref: `update-to` 10.1038/s41586-023-06734-w, type "correction"). Text: "We acknowledge that the original claims of material novelty were subject to misinterpretation—their intention was to indicate that the materials were new to the prediction platform, not necessarily new to science." and "we have manually re-analyzed the diffraction patterns and have confirmed that the prediction platform came to the correct conclusion in 36 of its 40 reported successes, with 4 compounds being inconclusive. This re-analysis was peer-reviewed post-publication. The total number of compounds successfully made by the platform has now been updated to exclude four target materials whose presence is inconclusive from XRD alone. We have also removed one compound from the discussion (Zn2Cr3FeO8) that was mistakenly included in the training data."
- The corrected A-Lab article, https://www.nature.com/articles/s41586-023-06734-w (banner "An Author Correction to this article was published on 19 January 2026. This article has been updated"): abstract now reads "Over 17 days of continuous operation, the A-Lab realized 36 compounds from a set of 57 targets"; body: "the A-Lab synthesized 36 of the 57 target compounds over 17 days of continuous experimentation, representing a 63% success rate."
- GNoME paper, https://www.nature.com/articles/s41586-023-06735-9 (Methods, "Validation through experimental matching and r2SCAN"): "All candidates for GNoME are derived from snapshots of databases made in March 2021 … Concurrent to our discovery efforts, researchers have continued to experimentally create new crystals, providing a way to validate GNoME findings. Of the experimental structures aggregated in the ICSD, 736 match structures that were independently obtained through GNoME." and "Overall, we found 736 matches, providing experimental confirmation for the GNoME structures. 184 of these structures correspond to novel discoveries since the start of the project." The 736 are database matches made by the authors, not syntheses of GNoME predictions by others. (The DeepMind blog the item linked says "External researchers in labs around the world have independently created 736 of these new structures experimentally", which is the stronger reading.)

**On the page:** title and `what` numbers (36 of 57, with the original 41 of 58 kept in brackets; 736 described as matches), caveat appended with the correction, URL swapped from the DeepMind blog to the GNoME paper. `contested` already true.

## 2. M2 (Microsoft/PNNL electrolyte). Published in JACS 146(29):20009, 9 July 2024

**VERIFIED** (bibliographically; the ACS page itself COULD NOT OPEN, HTTP 403).

- Crossref record for 10.1021/jacs.4c03849: title "Accelerating Computational Materials Discovery with Machine Learning and Cloud High-Performance Computing: from Large-Scale Screening to Experimental Validation", *Journal of the American Chemical Society* 146(29), 20009–20018, published online 9 July 2024, print 24 July 2024; authors Chen, Nguyen, Lee, Baker, Karakoti, Lauw, Owen, Mueller, Bilodeau, Murugesan, Troyer.
- arXiv API for the preprint 2401.04070 (submitted 8 Jan 2024): DOI field `10.1021/jacs.4c03849`; abstract: "navigate through more than 32 million candidates and predict around half a million potentially stable materials … our discovery pipeline further identified 18 promising candidates with new compositions … We then synthesized and experimentally characterized the s[tructures]". This is the work the item describes (32 million to 18, synthesized).
- PNNL publication record (search result): same citation, dated August 2024.

**On the page:** `verification` company-reported → peer-reviewed; `who` and caveat note the JACS citation; URL swapped to the ACS DOI. Date left at 2024-01 (dates on the page are the month of announcement).

## 3. M3 (MatterGen). 169 GPa inferred from Young's modulus and a computed Poisson ratio, maximum of four (158 ± 11); Materials Horizons 2026 says the product is a known 1970s Ta–Cr oxide

**VERIFIED** for the measurement; **VERIFIED** that the Materials Horizons paper exists and makes the claim; the year is 1971 in the journal abstract and 1972 in the preprint abstract; the RSC page **COULD NOT OPEN**.

- Nature 639, 624 (2025), https://www.nature.com/articles/s41586-025-08628-5: "This structure was generated by targeting a bulk modulus value of 200 GPa; we predict a value of 222 GPa using DFT for the ordered TaCr2O6 structure generated by MatterGen and similar bulk modulus values (219 GPa) for two other ordered approximations corresponding to the same disordered structure (Fig. 6c). We also experimentally measure the Young's modulus of the sample by nanoindentation and estimate its bulk modulus using the DFT-computed Poisson ratio of 0.30. The estimated bulk modulus is up to 169 GPa after four measurements (158 ± 11 GPa), in which the maximum of the four measurements is our best estimate given that the experimental powder sample is likely non-compact." Fig. 6c caption: "Two views of the disordered TaCr2O6 structure we experimentally synthesize."
- Materials Horizons paper: Crossref 10.1039/d6mh00268d, "Continued challenges in high-throughput materials predictions: MatterGen predicts compounds from the training dataset", Mikkel Juelsholt, *Materials Horizons* 13(11), 5672–5679 (2026), record created 20 April 2026, with `has-preprint` ChemRxiv 10.26434/chemrxiv-2025-mkls8 (v1 19 June 2025, v3 23 Jan 2026). ChemRxiv v3 abstract: "MatterGen was used to predict the novel compound TaCr2O6, which was subsequently synthesised in a disordered form as Ta1/3Cr2/3O2. However, detailed crystallographic analysis, presented in this paper, reveals that this is not a novel compound but is identical to the already known compound Ta1/2Cr1/2O2 reported in 1972 and actually included in MatterGen's training dataset." Semantic Scholar's copy of the journal abstract reads "identical to the previously reported Ta1/2Cr1/2O2, first described in 1971 and included in MatterGen's training dataset." The journal page (https://pubs.rsc.org/en/content/articlelanding/2026/mh/d6mh00268d) could not be opened to settle the year.

**On the page:** `contested: true`; `what` now says how 169 GPa was obtained; caveat appended with the inference and the Juelsholt challenge (both years given).

## 4. Q3 (AlphaEvolve on Willow). The report links arXiv 2510.19550; "10× lower error" is approximation error under a gate budget, 10.4% → 0.82%; first submitted Oct 2025

**VERIFIED.**

- https://deepmind.google/blog/alphaevolve-impact/ (dated May 7, 2026): "suggesting quantum circuits with 10x lower error" with that phrase hyperlinked to https://arxiv.org/abs/2510.19550, the only arXiv link in the passage.
- arXiv 2510.19550, "Quantum computation of molecular geometry via many-body nuclear spin echoes", 323 authors, v1 22 Oct 2025, no later version. Abstract: "we simulate the molecular OTOCs on a Willow superconducting quantum processor, using AlphaEvolve-optimized quantum circuits and arbitrary-angle fermionic simulation gates." Methods: "AlphaEvolve is used to generate a set of Python functions that produce quantum circuits approximating Hamiltonian evolution … [starting from] a human-written program (a first-order Trotter formula) … AlphaEvolve ultimately generated a population of programs that produce simulation circuits with significantly lower approximation error against the reference (improving from a 10.4% mean error to 0.82%), while remaining below the gate budget enforced by the device". Outlook: "our AlphaEvolve optimization loop relies on evaluating candidate circuits against a complete, classically pre-computed dataset of OTOCs, which is not immediately scalable to beyond-classical system sizes."

**On the page:** `verification` company-reported → preprint (the figure now has a primary source); `what` states the 10.4% → 0.82% approximation error; `who` and caveat name the preprint and its date; URL swapped to the arXiv abstract. Date left at 2026-05 (the impact report is still the item's announcement); the preprint's October 2025 date is in the caveat.

## 5. Q1 (AlphaQubit). Distance 5: 2.748% vs 2.915% (tensor network) vs 3.597% (correlated matching), so ~6% and ~24%, not 30%

**PARTLY VERIFIED.** The 2.748% and 2.915% figures and the ~6% are in the paper's text. The 3.597% correlated-matching figure is **NOT VERIFIED**: it does not appear in the paper's text, the Fig. 3 caption, or the text layer of the Supplementary Information PDF; it would be a value read off Fig. 3b. The 30% is Google's blog figure, which the paper's text never states.

- Nature 635, 834 (2024), https://www.nature.com/articles/s41586-024-08148-8: "AlphaQubit achieves an LER of (2.901 ± 0.023) × 10−2 at distance 3 and (2.748 ± 0.015) × 10−2 at distance 5 (Fig. 3a,b) … This LER is even lower than that of the tensor-network decoder—(3.028 ± 0.023) × 10−2 at distance 3, (2.915 ± 0.016) × 10−2 at distance 5 … State-of-the-art MWPM-based decoders, such as correlated matching (MWPM-Corr), matching with belief propagation (MWPM-BP) and PyMatching … lead to higher LERs than the tensor network and AlphaQubit (Fig. 3a,b)." (2.915 − 2.748)/2.915 = 5.7%.
- Google blog, 20 Nov 2024, https://blog.google/innovation-and-ai/models-and-research/google-deepmind/alphaqubit-quantum-error-correction/: "In the largest Sycamore experiments, AlphaQubit makes 6% fewer errors than tensor network methods" and "AlphaQubit also makes 30% fewer errors than correlated matching, an accurate decoder that is fast enough to scale." No distance is named for the 30%.
- Supplementary Information PDF (41586_2024_8148_MOESM1_ESM.pdf): text layer contains no "3.597", "MWPM-Corr" or "Sycamore".

**On the page:** caveat appended (the 6% is the paper's distance-5 result; the 30% is the blog's figure, not in the paper's text); URL swapped to the Nature paper. The 30% is left in `what` because no primary text gives a replacement number.

## 6. Q2 (AlphaQubit 2). Sub-1 µs is per-cycle throughput, latency < 500 µs; distance-27 colour code does not match the extrapolated trend

**VERIFIED.**

- arXiv 2512.07737 (v1 8 Dec 2025, v2 11 Mar 2026), https://arxiv.org/html/2512.07737v1 and v2. Section 4: "Both AQ2 and AQ2-RT are streaming decoders … whose throughputs can be maintained for longer experiments without any increase in latency, which remains below 500 μs"; "AQ2-RT achieves this stringent real-time throughput for the surface code up to distance 11"; "We have not yet addressed reducing the latency between the final measurement and the decoding result". Fig. 4a: "Logical error per cycle vs. throughput (average time per cycle)". Section 3.3: "AQ2 achieves near-optimal accuracy on the surface code up to code distance 23" and, for the colour code, "At distance 27, an ensemble of 3 models reaches a logical error per cycle of 8.0×10−11 … but does not match the idealized trend in this regime where training AQ2 is more difficult and expensive"; Section 6: "we observed a deviation from ideal scaling at the highest distances, particularly for the colour code at distance 27". The "idealized trend" is Tesseract extrapolated linearly from distances 5 and 7.

**On the page:** `what` corrected (near-optimal to 23; colour code to 27 below the idealized trend; per-cycle figure labelled throughput with latency below 500 µs); caveat appended.

## 7. Q5 (meta-design). 133M-parameter task-trained transformer; journal date 19 Feb 2026, not April

**VERIFIED.**

- Nature Machine Intelligence 8, 148–157 (2026), https://www.nature.com/articles/s42256-025-01153-0: "Received 10 December 2024, Accepted 05 November 2025, Published 19 February 2026, Version of record 19 February 2026, Issue date February 2026" (Crossref agrees: published 2026-02-19). Methods: "The model has approximately 133 million parameters and is trained from random initialization for 750,000 steps with a batch size of 256 (approximately 2.5 epochs on a dataset of 56 million samples)." Same sentence in the arXiv version 2406.02470 (v1 4 Jun 2024).

**On the page:** `date` 2026-04 → 2026-02; caveat appended (133M parameters, trained from scratch, journal date); `who` notes the date; URL swapped from Physics World to the journal article.

## 8. M5 (Lila). The preprint is arXiv 2609.30133 and it gives benchmark numbers

**VERIFIED** that it is the paper and that it gives in-house benchmark numbers; the current caveat's "no benchmark numbers given" is wrong as written.

- arXiv 2609.30133, "AI-guided high-throughput discovery of iridium- and ruthenium-free palladium-oxide catalysts for durable acidic oxygen evolution", v1 24 Sep 2026, v2 25 Sep 2026; PDF front matter: all 22 authors "Lila Sciences, Inc., Cambridge, MA"; "This research was funded entirely by Lila Sciences, Inc." Abstract: "an artificial intelligence (AI)-guided, human-supervised closed-loop platform (>90% automation) … 2,942 catalysts across 53 material systems and 26 elements … PdOx at ~200 h and NiTaPdOx at ~470 h. InMnPdOx … below 0.5 V over 1,000 h". Section 3.3: "we benchmarked the two leads (InMnPdOx and NiTaPdOx) against RuOx and PdOx films made on the same platform … InMnPdOx held a stable overpotential of 0.45 V (not iR-corrected), within 40 mV of RuOx (0.41 V) and roughly 90 mV below the best non-PGM catalyst." Workflow: "human operators perform sample-fixture transfers and initiate instruments, while experimental runs, data ingestion, model training, ranking, candidate generation, and closed-loop feedback are automated." No comparison to literature RuO2/IrO2 values; "comparable to ruthenium" is the item's paraphrase of the in-house RuOx comparison.

**On the page:** caveat appended with the numbers and their in-house nature (the original wording kept); `who` carries the arXiv number; URL swapped from unite.ai to the arXiv abstract.

## 9. M6, a new item: Jeon et al., Advanced Materials, 10 Aug 2026, doi 10.1002/adma.74502

**VERIFIED.** Real, open access, peer-reviewed, LLM-generated recipes, three unreported compounds made, humans ran the experiments.

- https://advanced.onlinelibrary.wiley.com/doi/10.1002/adma.74502 (Crossref agrees): "Closed-Loop Solid-State Synthesis Planning for Materials Discovery With Large Language Models", Dong Won Jeon, Dong Hwi Kim, Taeyang Jeon, Joo Yeong Na, Heegyu Kim, Hyunsouk Cho, Dae Soo Jung, Ju Li, Jin-Sung Park, Sung Beom Cho; *Advanced Materials* 38(58), e74502; "First published: 10 August 2026"; "Open Access"; affiliations Sungkyunkwan University, Ajou University, KICET, MIT (Ju Li, corresponding).
- Abstract: "Using a retrieval-augmented generation (RAG) approach, the system first retrieves similar recipes from the corpus and then generates a new candidate recipe conditioned on those exemplars … the framework was applied to unreported solid-state electrolyte candidates identified through first-principles screening, and multiple oxy-selenide compounds were successfully synthesized through iterative feedback between the model and experiment."
- Results: "we generated 660 hypothetical structures … Structures absent from the MP database were regarded as unreported candidates. These hypothetical structures were then subjected to first-principles calculations"; "we performed the synthesis at 600°C for 3 h … secondary phases … the sample synthesized at 400°C exhibited a single-phase LiCr(SeO3)2 without any detectable secondary phases"; "Through this iterative verification workflow, we successfully synthesized LiCr(SeO3)2 … Following the same procedure, we confirmed suitable synthesis conditions for LiAl(SeO3)2 and CsLiSeO4 through three consecutive experiments guided by the recipe generator"; for the known LiGa(SeO3)2, "we successfully synthesized the target compound using an alternative SSR route after three iterative feedback cycles". Methods: "The mixture was thoroughly ground in an agate mortar for 15 min in ambient air … transferred into alumina crucibles and placed in a tube furnace." Introduction: "successfully synthesized them with fewer attempts by combining the recipe generator developed in this study with domain expert feedback." The recipe generator's base model is not named in the main text (GPT-4o is named only as the scoring model and GPT-4o-mini inside a third-party synthesizability checker).

**On the page:** added as item M6 (tier 1, llm true, physical true, quantum false, peer-reviewed, 2026-08, P 6, H years, W 1.5, C 0.9) with a caveat that humans chose the targets and ran the experiments; LADDER entry matter true, necessary "arguable", leap "early sign", qubits false. The C of 0.9 rather than the page's usual 1.0 for peer-reviewed work: one paper from one group, two months old, no independent replication.

## 10. P7 (nine loops). 107,053 coefficients are at symbol level; ~$100 CPU but $1,000–2,000 per approach with model use

**VERIFIED.**

- https://smsharma.io/cosmic-nine-loops/ ("Cosmically Normalized Six-Point Amplitudes at Nine Loops", 16 September 2026): "The nine-loop symbol in quintuple-coproduct form below was computed by Claude (Anthropic)"; "Its exact coefficients come from a separate direct bootstrap of the nine-loop symbol in the space of hexagon functions … The septuple file and the quintuple representation agree on every coefficient compared: all 107,053 nonzero coefficients that determine the septuple file, 3,401 of them modulo the two primes only." Of the function-level file: "The function was obtained separately; it has been computed once, and there is no second, independent computation of it." No costs on the page.
- https://www.anthropic.com/research/yes-claude-can-do-nine-loops ("Yes, Claude can do Nine Loops", Sep 25, 2026, guest post by Matt von Hippel with an addendum by Lance Dixon): "Claude ended up doing the calculation two different ways: the original bootstrap, and the indirect form-factor approach. Either approach would have cost an end-user around one or two thousand dollars, mostly due to the expense of running Claude for so long. The bootstrap calculation, done with the Python programming language with package SymPy, took around $100 of the budget, corresponding to running 96 CPUs for a week."

**On the page:** `what` now says the agreement is at symbol level, that the beyond-symbol completion was computed once, and gives both cost figures; URL swapped from unite.ai to the Anthropic post.

## 11. P8 (Navier–Stokes). Hales on Tao's blog (9 Oct 2026): formalisation confirmed by more than a dozen proof checkers; Bastounis–Circelli–Hansen do not claim the formal theorem is false

**VERIFIED.**

- https://terrytao.wordpress.com/2026/10/09/what-mathematicians-should-know-about-the-lean-theorem-proverquestions-of-reliability-and-ai/ : "This is a guest post by Thomas Hales." Dated 9 October 2026. "The Navier-Stokes formalization has already been confirmed by more than a dozen proof-checkers."
- arXiv 2610.08144 (v1 6 Oct 2026), "Navier-Stokes lost in translation: Why Lean verification of AI autoformalisation does not guarantee correct natural language proofs", Bastounis, Circelli, Hansen. Abstract: "we show that the formalised Lean proof does not correspond to the NL proof of blow-up of solutions to the Navier-Stokes equations." No sentence claims the Lean theorem or the paper's theorem is false; the item's existing caveat already said so.

**On the page:** caveat appended with the Hales sentence. `contested` stays true (the prose-vs-Lean mismatch is unresolved).

## 12. P9 (372 families). 372 families and 719 (or 722) manuscripts; "70 physics families" needs a selection list; "no human has read most of them" needs a source

**VERIFIED** on all three points: the counts, a selection list that gives exactly 70, and the absence of any repository statement behind "no human has read most of them".

- https://github.com/openai/math README: "The current catalogue contains 719 manuscripts organized into 372 families … Each family is classified by mathematical discipline." and "The repository has ~42% top-line results formalized." Commit history: initial commit 6 Oct 2026; the 8 Oct merge "Update manuscripts and Lean formalizations" changed README and CONTENTS from "722 manuscripts" to "719". `history.md` ("October 7, 2026"): "we have withdrawn the following three manuscripts … This brings the total percentage of top-line results formalized to 300 / 719 = ~42%."
- `overview.pdf` ("OpenAI Research Catalog, 372 result families in 719 manuscripts, October 6, 2026") groups the families into 17 subject sections. Counting entries per section: Mathematical physics 25 (families 260–284, which include the quantum-information results: Moore's parity conjecture for QAC0, QMA-hardness, entangled-game repetition, channel capacities), Partial differential equations 16 (362–377, including "Universal computation in forced Navier–Stokes flows" and "De Giorgi's conjecture in dimension eight"), Probability and statistical mechanics 29 (211–239). 25 + 16 + 29 = 70. That is the only combination of whole sections that gives 70, so it is the selection the item's title rests on.
- On human reading: the README says the results "were obtained with the same procedure using an unreleased internal OpenAI model", that "Some of the unformalized results could have issues", and that "the writeup for the Re(s) > 11/12 zero-free region for the Riemann zeta function was human edited for readability." Nothing in README, CONTENTS, history or the overview says who has or has not read the manuscripts.

**On the page:** `what` gives 300 of 719 and 722 → 719; caveat appended with the selection list and a note that "no human has yet read most of them" is the author's inference (the original wording kept).

---

## What changed in `data/items.json`

| Item | Fields changed | Source |
|---|---|---|
| M1 | title, what, caveat (appended), url | Nature 650 E1; Nature 624 86 (corrected); Nature 624 80 |
| M2 | verification → peer-reviewed, who, caveat (appended), url | Crossref 10.1021/jacs.4c03849; arXiv 2401.04070 |
| M3 | contested → true, what, caveat (appended) | Nature 639 624; Crossref 10.1039/d6mh00268d; ChemRxiv 2025-mkls8 v3 |
| Q1 | caveat (appended), url | Nature 635 834; Google blog 20 Nov 2024 |
| Q2 | what, caveat (appended) | arXiv 2512.07737 v1/v2 |
| Q3 | verification → preprint, who, what, caveat (appended), url | deepmind.google/blog/alphaevolve-impact; arXiv 2510.19550 |
| Q5 | date → 2026-02, who, caveat (appended), url | Nat. Mach. Intell. 8 148; arXiv 2406.02470 |
| M5 | who, caveat (appended), url | arXiv 2609.30133 |
| P7 | what, url | smsharma.io/cosmic-nine-loops; anthropic.com post of 25 Sep 2026 |
| P8 | caveat (appended) | Tao's blog 9 Oct 2026; arXiv 2610.08144 |
| P9 | what, caveat (appended) | github.com/openai/math README, history.md, overview.pdf |
| M6 | new item | Adv. Mater. 38 e74502 |

Not changed anywhere: `domain`, `tier`, `llm`, `physical`, `quantum`, `artifact`, `P`, `H`, `W`, `C` of the 22 original items; no caveat text removed (the test now enforces this). `data/ladder.json` gained an M6 row; no existing row changed.

---

# Checks of 27 October 2026

Three changes to the James page were checked on 27 October 2026, the same way as above. The session that wrote them could open `anthropic.com` and `github.com` (pages and raw files) but not `arxiv.org`, `openai.com`, `deepmind.google`, `quantinuum.com` or `claymath.org`; what each check could and could not see is stated under it.

## 13. Q8, a new item: Anthropic, "Designing more efficient quantum circuits with Claude", 16 October 2026

**VERIFIED** against the post; the paper it links (arXiv 2610.22367) **COULD NOT OPEN**, so the item's figures are the post's.

- https://www.anthropic.com/research/designing-efficient-quantum-circuits (Oct 16, 2026; Science): "Claude found designs that improve on the best published circuits, in some cases by an order of magnitude or more." "Across eight computational primitives", spanning chemistry, optimization, quantum simulation, number theory and numerical computing. "Claude Mythos 5 could successfully work in a closed loop" … "with no human input between rounds"; the score is "the number of qubits used, multiplied by the number of gates". Point addition: "Compared with the smallest previous design, one circuit in the family uses 12% more qubits but 17x fewer gates." and "After working for 53 hours with minimal human input". DQI decoder: "reduced the number of gates in the decoder by a factor of 12" and "ran 403 million sample decodings to measure how often these exceptions actually occurred". Storage: "would take 665 qubits" against "sets aside room for just one saved value, or 19 qubits" and "About one run in 10,000 needs more than that and fails". Lean: "it prompted Claude to write Lean proofs to verify its divsteps design". Limits: "Circuit design is only one part of building a useful quantum computer." and "useful quantum computing could arrive sooner". The post does not say any circuit ran on quantum hardware. Named: Andi Gu (lead, Anthropic STEM Fellows Program), Alek Kemeny (Anthropic), Susanne Yelin (Harvard), Mikhail Lukin (Harvard, QuEra). "Read the full paper on arXiv": https://arxiv.org/abs/2610.22367.
- The FeMoco figures on the page (about 50 trillion Toffoli gates in 2017 down to about 340 million) are the field's published estimates, cited for context, not Claude's result; they are left out of the item.

**On the page:** added as item Q8 (tier 3, llm true, physical false, quantum true, preprint, 2026-10, P 6, H years, W 1.5, C 0.8); LADDER row matter false, necessary true, leap none, qubits true.

## 14. P9 (372 families). The repository's 26 October update: 721 manuscripts in 373 families, two additions with Lean

**VERIFIED** (raw `README.md`, `history.md` and `CONTENTS.md` of github.com/openai/math, main branch, fetched 27 October 2026).

- README: "The current catalogue contains 721 manuscripts organized into 373 families." and "The repository has ~42% top-line results formalized."
- history.md, "October 26, 2026": "We have added two new manuscripts with accompanying Lean formalizations: *Local smoothing for the Euclidean wave equation.* The proof uses an auxiliary partial differential equation to establish Sogge's local smoothing for waves in every spatial dimension at least two. It also yields the Kakeya maximal and dimension conjectures and Stein's spherical restriction estimates throughout the interior of the conjectured range. We are releasing the model output directly, as we did in our October 6 release. *The Exponential Time Hypothesis is False.* The paper gives a deterministic algorithm that exactly counts satisfying assignments of fixed-width CNF formulas in subexponential time and polynomial space. The case of 3-SAT refutes the Exponential Time Hypothesis. An independent working group of computer scientists led by Russell Impagliazzo, Ramamohan Paturi, and Ryan Williams will examine and explain the proof. At the group's request, we are making the materials public immediately so others can examine them as well." The same entry adds a Lean formalization for "The rational Hodge conjecture for CM abelian varieties".
- CONTENTS.md: family 079 "Local smoothing for the Euclidean wave equation" (manuscript dated October 25, 2026, with Lean) and family 378 "Disproof of the Exponential Time Hypothesis" (with Lean).
- Neither file mentions the physics result announced the same day (check 15).

**On the page:** `what` and caveat appended; title, labels and ratings unchanged.

## 15. P10, a new item: OpenAI's physics claim of 26 October 2026

**COULD NOT OPEN.** `openai.com` was refused from the session that wrote this entry, so the post itself was not read. The item rests on the search engine's rendering of the post, which two separate queries returned in the same words, and on coverage; it is labelled company-reported and rated C 0.3. Before this entry is deployed, open https://openai.com/index/building-scientific-understanding-with-academic-communities/ and confirm the three points below, then record what the post says here.

- As returned by the search engine (its rendering of the post, not necessarily verbatim): the announcement gives a mathematically rigorous existence proof of certain interacting quantum field theories containing gauge fields and fermions in four dimensions, including Quantum Chromodynamics (QCD) and a unified completion of the Standard Model, and builds on Balaban's approach in constructive quantum field theory; a group led by David Gross, with Michael Douglas, Arthur Jaffe, Igor Klebanov and Nikita Nekrasov, will shepherd the effort and initially hold the AI artifacts while preparing its own writeup. To confirm against the post: (1) the exact wording of the claim; (2) the review group's members and that the artifacts are held; (3) whether the post names the model or gives dates.
- Coverage (leads, not sources): The Asia Business Daily, 27 Oct 2026, says the model produced the Yang–Mills proof on 9 September and a QCD-related proof on 18 September and that the Yang–Mills formalisation was completed on 16 October; OfficeChai says the pure Yang–Mills result does not address the mass gap. The dates and the mass-gap point are in the caveat as "coverage says".
- The repository's 26 October entry (check 14) does not mention the physics result; nothing about it is public.

**On the page:** added as item P10 (tier 3, llm true, physical false, quantum false, company-reported, 2026-10, P 2, H someday, W 2, C 0.3); LADDER row matter false, necessary true, leap none, qubits false.

---

## What changed in `data/items.json` on 27 October 2026

| Item | Fields changed | Source |
|---|---|---|
| Q8 | new item | anthropic.com post of 16 Oct 2026 (paper arXiv 2610.22367, not opened) |
| P9 | what, caveat (appended) | github.com/openai/math README, history.md, CONTENTS.md |
| P10 | new item | openai.com post of 26 Oct 2026 (not opened; see check 15) |

No caveat text removed; no label, flag or rating of an existing item changed. `data/ladder.json` gained Q8 and P10 rows; no existing row changed.

---

# Checks of 17 November 2026

Eight changes to the James page were checked on 17 November 2026, the same way as above. Open from the session that wrote them: `arxiv.org` (abstract records and full-text HTML), `api.crossref.org`, `github.com` raw files, `anthropic.com`, `nvidianews.nvidia.com`, `quantinuum.com`, `claymath.org`. Refused to automated clients (HTTP 403): `openai.com`, `journals.aps.org`, `pppl.gov`, `science.org`; for those, what was and was not seen is stated under each check. Quotations from arXiv are from the full-text HTML of the version named.

## 16. P10 (OpenAI, Yang–Mills). The Lean proof of the pure Yang–Mills part is public and assessed; the assessment's own limits

**VERIFIED** against the reviewing group's repository. OpenAI's post of 26 October still **COULD NOT OPEN** (403), so check 15's three points about that post stand unconfirmed; this check replaces the post as the item's source.

- https://github.com/yang-mills-group/YM, README: "The first package concerns **OpenAI's submission of 28 October 2026**. The assessment is dated **10 November 2026**. In our opinion, this submission proves that a relativistic quantum field theory satisfying the Wightman axioms can be constructed as a scaling limit of four-dimensional Wilson lattice gauge theory for any simple compact gauge group. It does not prove that the infinite-volume limit is unique or that there is a mass gap." Its table of submissions lists "OpenAI, 4 November 2026 | work in progress" and "Alpöge and Sussman, 15 November 2026 | work in progress". On other theories: "Proposals concerning QCD or chiral SU(5) should identify that category so they can be considered for the corresponding results repository."
- `docs/assessment-1.pdf` in that repository ("Validation of the OpenAI Yang–Mills construction. Based on Lean code submitted October 28, 2026 … Yang–Mills group Nov 10, 2026 release"): "OpenAI's construction does not certify the full Jaffe–Witten problem: no mass gap is claimed. Uniqueness across volume subsequences and agreement of the component theories are also unresolved." "Validation. A clean rebuild, axiom audit, and Comparator check passed. Our additional Lean checks establish that the submitted construction satisfies the independently formulated requirements described below, using the submission's proved results." "Sources and attribution. This assessment uses the Lean sources submitted by OpenAI on Oct 28, 2026 and available in the repository yang-mills-group/OpenAI-YM-20261028. It does not draw on the separate informal proof manuscript. We used OpenAI's Astra to assist with the digestion of the supplied Lean code. We do not claim to fully understand the proof yet." "Our group's only connection to OpenAI (besides accepting their submissions) is the use of their Astra model to help with analysis. Our group has no present connection to the Clay Mathematics Institute." Acknowledgements: "This document was prepared by Michael R. Douglas, Arthur Jaffe, Ron Nissim and Fred Rajasekaran, with contributions from other group members and consultants, and approved by the entire group."
- https://github.com/yang-mills-group/OpenAI-YM-20261028, README: "A positive mass gap, general exclusion of continuous-mass generalized free fields and all-orders MS-bar matching are outside its scope."
- Not in these documents: the name David Gross (the group's leadership is from OpenAI's announcement as returned by search, and from coverage), any statement about QCD's proof, and the length or release status of the written manuscript (coverage says 1,147 pages, unreleased).
- https://www.claymath.org/ (front page, 17 Nov 2026): the latest news item is still "11 September 2026 Navier-Stokes Announcement"; nothing on Yang–Mills.

**On the page:** title, `who`, `what` and `url` rewritten to the assessment; `verification` company-reported → preprint (public Lean sources in a repository, as Q7 and P9); C 0.3 → 0.8 (an outside group's assessment, with its stated limits); W 2 → 3 (the assessment judges that it constructs a four-dimensional Wightman theory, short of the Clay problem); caveat appended, the 27 October wording kept. LADDER `why` updated; ratings unchanged.

## 17. Q8 (Claude circuits). The paper behind the post

**VERIFIED.** The paper could not be opened on 27 October; it could on 17 November.

- arXiv 2610.22367 v1, "Discovering state-of-the-art quantum circuits with large language models", Andi Gu, Alek H. Kemeny, Susanne F. Yelin, Mikhail D. Lukin, submitted 15 Oct 2026, 46 pages. Abstract: "we introduce an evolutionary framework in which large language models (LLMs) propose circuit designs and an independent evaluator verifies and scores them … In seven of the eight tasks, the discovered circuits significantly reduce both Toffoli and qubit counts relative to the state of the art. In the eighth, the search discovers a new reversible architecture for prime-field modular inversion." Body: "We search over these circuit-generating programs with OpenEvolve [33], using Claude Mythos 5 [28] to propose architectures and program rewrites. Each of the eight searches uses a fixed, hand-written task specification"; "In the worst case, 35 stack entries (665 qubits) would be needed. Under the DQI input distribution, a second stack entry is required with probability 1.0×10−4, so the discovered circuit allocates only one stack entry (19 qubits instead of 665) and permits failure on these rare inputs."
- A text search of the paper did not find the post's "17x fewer gates" or "factor of 12" in those words; they remain the post's figures.

**On the page:** caveat appended; nothing else changed.

## 18. Q9, a new item: neural decoders on Quantinuum's Helios colour-code data

**VERIFIED.**

- arXiv 2610.24077 v1, "Quantum error correction well below the color code threshold", Ali Lavasani and 22 others, submitted 16 Oct 2026. Abstract: "we demonstrate below-threshold operation of triangular color codes with distances d=3,5, and 7 on Quantinuum's Helios trapped-ion quantum processor … we achieve logical error rates as low as 5(+4/−2)×10−6, and demonstrate error suppression by over an order of magnitude, Λ=12(+3/−2) … We compare logical performance for existing near-optimal algorithmic decoders, and both convolutional neural network and transformer-based neural network decoders capable of real-time decoding an order of magnitude faster than the syndrome extraction rate." Body: "we train two complementary neural-network decoders, a convolutional neural network (CNN) and a round-token transformer (RTT) on emulator data and apply them to the hardware data for memory experiments without further fine-tuning"; "The algorithmic decoders are technically indistinguishable within 1-σ error bars, and the two neural-network decoders achieve comparable logical performance to algorithmic decoders … suppression factors of Λ_Tesseract=12, Λ_Frontier=11, Λ_CNN=7 and Λ_RTT=8"; "While Tesseract achives near optimal performance, it is generally not fast enough to be used in real time"; "while all decoding in this work has been done offline, the syndromes have been fed to the streaming decoders one round at a time"; per-round GPU times "0.26, 0.36, 0.52 ms for the CNN and … 0.22, 0.25, 0.35 ms for the RTT"; "there could still be error channels on the device that are not captured by the emulation."
- https://www.quantinuum.com/blog/quantinuum-closes-in-on-one-million-error-free-operations (October 19, 2026): "we ran for 580,000 shots (29k shots, each one having 20 rounds, and observed 3 failures)".

**On the page:** added as item Q9 (tier 2, llm false, physical true, quantum true, preprint, 2026-10, P 8, H years, W 1.5, C 0.8); LADDER row matter false, necessary false, leap none, qubits true.

## 19. Q10, a new item: Google's formally verified quantum programs

**VERIFIED.**

- arXiv 2611.09822 v3, "Discovering formally verified quantum programs with AI", 25 authors (Shirobokov, Jaderberg, … Babbush, Chaudhuri, Kohli; affiliations Google DeepMind and Google Quantum AI), submitted 6 Nov 2026, v3 16 Nov 2026. Abstract: "we build a quantum program library in the Lean theorem prover in which Gemini 4 agents synthesize novel programs against formal problem specifications and verify their correctness and cost … Our results improve on prior baselines for parallel search (up to 2.57x), quantum arithmetic (290x), and simulations relevant to fusion, photochemistry and drug-metabolism by 12x, 8x and 2.5x respectively … lets researchers design algorithms that today's classical and quantum computers cannot test". Body: "a 290× spacetime reduction for fixed-point arcsin, and 11.8×, 8.22× and 2.49× reductions on simulations relevant to fusion, photochemistry and drug metabolism"; "369,800 (100 qubits, 3,698 T gates), 290× below the baseline"; "reducing resource costs by 290× for arcsin (combining classical and formal search)"; "Researchers and domain experts choose the problems and carefully prepare faithful formal specifications."

**On the page:** added as item Q10 (tier 3, llm true, physical false, quantum true, preprint, 2026-11, P 6, H years, W 1.5, C 0.8); LADDER row matter false, necessary true, leap none, qubits true.

## 20. M7, a new item: ElementsClaw, four superconductors

**VERIFIED** against the preprint. The search engine reports an ICML 2026 acceptance; the arXiv record carries no such note and `icml.cc` was not opened, so the label is preprint.

- arXiv 2604.23758, "Agentic Fusion of Large Atomic and Language Models to Accelerate Superconductor Discovery", Mingze Li, Yu Rong and 17 others (Gaoling School of Artificial Intelligence, Renmin University of China; DAMO Academy, Alibaba Group; Hupan Lab; others), v1 26 Apr 2026, v3 4 May 2026. Abstract: "ElementsClaw, an agentic framework for materials discovery that orchestrates a suite of Large Atomic Model (LAM) tools finetuned from our proposed 1-billion-parameter model Elements for numerical computation, while leveraging Large Language Models (LLMs) for semantic reasoning … rediscovers 66 experimentally verified superconductors that are absent from the standard SuperCon3D database. Scaling to 2.4 million equilibrium crystals, ElementsClaw identifies 68,000 high-confidence candidates in just 28 GPU hours … Guided by the agent's reasoning, we experimentally synthesize and verify four novel superconductors: the motif-guided Zr3ScRe8 (Tc = 6.5 K), the de novo generated HfZrRe4 (Tc = 5.9 K), the structurally reinterpreted Zr4VRe7 (Tc = 3.5 K), and the database-latent Hf21Re25 (Tc = 2.5 K)."
- Body: "Guided by human expertise, the agent first curates labeled superconducting instances via Elements-T screening and GPT-5-driven literature synthesis"; "After manual verification, the candidates are classified into 158 literature-verified superconductors, 385 verified non-superconductors and 981 unve[rified]"; "we execute the GPT-5.4 extraction pipeline over three independent times … we employ Opus-4.6 for a secondary review"; "we select Hf21Re25 as a representative database-latent validation case. Arc-melting synthesis followed by PXRD refinement confirms the target phase … Electrical transport measurements reveal a superconducting transition with Tc onset = 3.0 K and Tc zero = 2.0 K"; "ElementsClaw identifies Zr4VRe7, previously reported in the GNoME … dataset … with an orthorhombic structure, but predicted instead a lower-energy hexagonal configuration … Magnetic measurements reveal bulk superconductivity, with an onset Tc of 3.5 K"; "Zr3ScRe8 is selected as the primary experimental target … Transport measurements revealed Tc onset = 6.8 K and Tc zero = 6.0 K, while magnetic susceptibility showed a bulk superconducting transition near 6.5 K".

**On the page:** added as item M7 (tier 1, llm true, physical true, quantum false, preprint, 2026-04, P 6, H years, W 2, C 0.7); LADDER row matter true, necessary "arguable", leap "early sign", qubits false.

## 21. M8, a new item: kagome superconductors, Physical Review Research

**VERIFIED** bibliographically and against the preprint's text; the APS page **COULD NOT OPEN** (403).

- Crossref record for 10.1103/lpqj-7hyg: "Machine-learning-guided discovery of kagome superconductors YRu3B2 and LuRu3B2", *Physical Review Research* 8(2), 023308, published 17 June 2026, CC BY 4.0; authors Albu Mustaf, Sajilesh K. P., Mishra, Deng, Jiang, Hiorth, Lamponen, Gutierrez-Amigo, Törmä, Marques, Bernevig, Morosan; `has-preprint` arXiv 2512.16945. Deposited abstract: "We report the experimental discovery of bulk superconductivity in two kagome lattice compounds, YRu3B2 and LuRu3B2, which were predicted through machine-learning-accelerated high-throughput screening combined with first-principles calculations … Tc = 0.81 K for YRu3B2 and Tc = 0.95 K for LuRu3B2".
- arXiv 2512.16945 (full text): "we performed an ML-accelerated high-throughput screening of the entire 1:3:2 kagome family and identified several stable materials predicted to exhibit superconductivity. Here, we report the first successful experimental confirmation of bulk superconductivity in one of these predicted systems: YRu3B2. Furthermore, we report a second isostructural, new superconductor, LuRu3B2. The Lu compound was initially overlooked in our high-throughput predictions [14] because its calculated phonon spectrum exhibits weakly imaginary modes"; "The elements were arc-melted on a water-cooled copper hearth in an argon atmosphere"; "confirmed through magnetization, specific heat, and resistivity measurements with superconducting volume fractions close to 100%."

**On the page:** added as item M8 (tier 2, llm false, physical true, quantum false, peer-reviewed, 2026-06, P 6, H years, W 1.5, C 0.9, as M6); LADDER row matter true, necessary "arguable", leap "early sign", qubits false.

## 22. M9, a new item: Anthropic, "Testing Claude on real-world electronics design", 9 November 2026

**VERIFIED** against the post; each passage below was matched word for word in the page text.

- https://www.anthropic.com/research/claude-electronics-design (Published Nov 9, 2026; Science): "asking Claude Fable 5.2 to design three electronic devices: a speakerphone, a voice-assistant hub, and a handheld virtual pet"; "directed human engineers to build prototypes that worked without any fixes to their circuitry"; "Diode assembled the circuit boards and ran the firmware, under Claude's direction. The final result was a prototype of a speakerphone that still works after weeks of use."; "Claude ran these checks itself"; "Diode manufactured all three boards directly from Claude's design files, without any back-and-forth over adjustments."; "All three of these devices are still prototypes: they haven't been through electrical validation, antenna tuning, thermal testing, or certification, and they weren't designed for mass production. Since Claude wasn't connected to test equipment or to the machines that make and assemble circuit boards, engineers at Diode had to physically build and test the prototypes."; footnotes: "Anthropic has a commercial relationship with Diode." and "Overall, their prompting was minimal and limited to short directives (e.g., "clean up the schematic" and "continue")."
- The post links no paper or data release. It cites an OpenAI post on designing a handheld device (openai.com/index/accelerating-engineering-for-the-physical-world/), which could not be opened and is not on the page.

**On the page:** added as item M9 (domain electronics, tier 1, llm true, physical true, quantum false, company-reported, 2026-11, P 7, H now, W 1.5, C 0.6, as M4); LADDER row matter true, necessary false, leap "early sign", qubits false. The chart plots electronics with the materials and chips marker.

## 23. P11, a new item: machine-learning control on DIII-D, Nuclear Fusion

**VERIFIED** bibliographically and against the preprint's text. The quotations are from arXiv v1; the journal version was not compared line by line.

- Crossref record for 10.1088/1741-4326/ae7f9d: "Enabling integrated AI control on DIII-D: a control system design with state-of-the-art experiments", *Nuclear Fusion* 66(7), 076050, published online 2 July 2026, CC BY 4.0; authors Rothstein, Farre-Kaga, Butt, Shousha, Erickson, Wakatsuki, Steiner, Kim, Jalalvand, Kolemen (Princeton University, Princeton Plasma Physics Laboratory, National Institutes for Quantum and Radiological Science and Technology). Abstract: "We present the design and application of a general algorithm for Prediction And Control using MAchiNe learning (PACMAN) in DIII-D … We also describe several successful ML control experiments in DIII-D using this algorithm, including a reinforcement learning controller targeting advanced non-inductive plasmas, a wide-pedestal quiescent H-mode ELM predictor, an Alfvén Eigenmode controller, a Model Predictive Control plasma profile controller and a state-machine TM predictor-controller."
- arXiv 2511.08818 v1 (11 Nov 2025), section III.1: "an RL based βN and internal transport barrier (ITB) controller which demonstrates 'full ML control' where the outputs of an ML algorithm fully decide actuator commands, subject to hard coded machine safety actuator limits … a similar RL controller was trained offline using the RAPTOR code as a simulator environment … this RL controller needed PACMAN to run at 50 ms cycle time and this was achieved"; Figure 5: "DIII-D shot 204975 where the RL ITB controller was used to control βN and ITBs"; "The model block outputs request for P_NBI,on-axis, P_NBI,off-axis, and P_ECH."

**On the page:** added as item P11 (tier 2, llm false, physical true, quantum false, peer-reviewed, 2026-07, P 9, H now, W 1.5, C 0.9); LADDER row matter true, necessary "arguable", leap "early sign", qubits false.

---

## Looked at on 17 November 2026 and left off the page

- **NVIDIA, IBM and Fermilab, 16 November 2026.** https://nvidianews.nvidia.com/news/nvidia-announces-collaboration-with-ibm-and-fermi-national-accelerator-laboratory-to-launch-quantum-classical-codesign-platform-plus-error-correction-breakthrough-to-advance-practical-quantum-computing : "NVIDIA today announced plans for new collaborations with IBM and the U.S. Department of Energy's Fermi National Accelerator Laboratory"; Fermilab's Anna Grassellino: "This proposed platform would combine NVIDIA's computing capabilities with IBM's quantum technologies and Fermilab's scientific expertise"; on the decoder: "A classical algorithm called a decoder interprets measurement data to identify likely errors" and "NVIDIA's new TCBP-JOBS decoding algorithm accelerates the computationally intensive parts of quantum error-correction research by up to 13,000x". The paper, arXiv 2611.21321 (Howe, Maurya, Olle, Basov, Li, Lietz, Young, Svore, 16 Nov 2026): belief propagation with an ordered-statistics beam search on GPUs; its learned part is "A multilayer perceptron with two hidden layers of 16 units … the entire model has only 529 weights"; the 13,000× is "against unsparsified long-beam Tesseract … on the bivariate-bicycle codes", with "Serial speedups over Tesseract's sparsified presets range from 10× to 7,400×", and "rare-event splitting on the gross code shows that Tesseract is more accurate" at lower error rates; the tests are simulated circuits. Left out because the platform is a plan and the decoder is a conventional algorithm on GPUs that its authors do not present as an AI result.
- **In biology, which James set aside on 2 June 2025:** Anthropic's vault-particle structure (4 Nov) and DeepMind's AlphaGenome 2 (11 Nov, per coverage).
- **Simulation or theory only, preprints of the window:** an LLM agent that designs ion-implantation recipes against a simulator (arXiv 2611.03795); the Exponential Time Hypothesis refutations, which are computer science (OpenAI's is in the repository of item P9).
- **Company announcements with no paper found:** Quantum X Labs' decoder on IBM processors (9 Nov), SuperMatics, a University of Nottingham self-driving laboratory (14 Nov, per coverage).

## What changed in `data/items.json` on 17 November 2026

| Item | Fields changed | Source |
|---|---|---|
| P10 | title, who, what, verification → preprint, W 2 → 3, C 0.3 → 0.8, url, caveat (appended) | github.com/yang-mills-group/YM README and docs/assessment-1.pdf; OpenAI-YM-20261028 README |
| Q8 | caveat (appended) | arXiv 2610.22367 |
| Q9 | new item | arXiv 2610.24077; quantinuum.com post of 19 Oct 2026 |
| Q10 | new item | arXiv 2611.09822 |
| M7 | new item | arXiv 2604.23758 |
| M8 | new item | Crossref 10.1103/lpqj-7hyg; arXiv 2512.16945 |
| M9 | new item | anthropic.com post of 9 Nov 2026 |
| P11 | new item | Crossref 10.1088/1741-4326/ae7f9d; arXiv 2511.08818 |

No caveat text removed. No label, flag or rating of any item on `main` changed; the P10 changes are to an item added on 27 October. `data/ladder.json` gained rows for Q9, Q10, M7, M8, M9 and P11, and the `why` of P10 was reworded; no rating of an existing row changed. The ratings of the new rows are proposals in the author's voice, for the author to confirm.

---

# Check of 23 November 2026

One item was added on 23 November 2026, at the author's request, although it is mathematics and not physics or engineering.

## 24. X2, a new item: the Riemann Hypothesis, proved in Lean by Levent Alpöge working with Claude

**VERIFIED** against the author's note and the certifying statement, both opened. The file hash of the note (SHA-256 `3fc97784…cfeb8d`, 245,114 bytes) matches the hash recorded independently in github.com/tamnd/riemann-lean `SOURCE.md`.

- https://alpo.ge/remark.pdf (four pages, unsigned and undated; released 20 Nov 2026 per the statement below): "I believe I have, working with Claude, discovered a proof of the Riemann Hypothesis. In fact, the method easily extends much further, resolving the so-called Generalized Riemann Hypothesis, and I expect, with more time, the Extended Riemann Hypothesis too. Claude and I have also formalized the arguments without assumptions." "Claude and I have had a great time together with such breadth in recent months, but this time Claude far outpaced me near the finish line." "I guided us to the right situation analogous to that toy setting, and then Claude began to leave me in awe." "The argument is incredibly long at the moment, and while its formalization is finished and it is routine to produce a huge, unreadable document containing sufficient detail, in my view of my path I have just taken a step." "This puts us in the rather extraordinary situation this age has made possible, in which I am presenting the world with a complete argument before having mastered a massive neighbourhood around its mathematics. It being obviously inappropriate to attempt to post some massive unreadable travesty of "slop", I decided to only present Lean." Footnote: "I of course amused myself, and hit 250,000+ pages." On the timeline it gives: "a rough timeline Claude provided after a thorough search", running from "10/6/26: Stepanov determinant" to "11/16/26: GRH", with the note "The parts in which Claude is the expert and not me I am sort of paraphrasing a "slop" summary, which might make zero sense". The note names no Claude model and no employer; it refers to "Our leadership" and to having "messaged Dario".
- https://leanprover-community.github.io/blog/posts/riemann-hypothesis/ ("Lean verification of the Riemann Hypothesis", Lean and Mathlib communities, 2026-11-21 13:55): "Joint statement by the Lean and Mathlib communities, endorsed by the Lean FRO and the Mathlib Initiative. On November 20, 2026, Levent Alpöge released a proof of the Riemann Hypothesis as a Lean library comprising 17 million lines of code. We have full confidence that Alpöge's proof of the Riemann Hypothesis is correct, and we congratulate him on this achievement." "The codebase depends directly only on Mathlib … We hereby certify that both the statement and the proof of the Riemann Hypothesis are correct." "The statement of the Riemann Hypothesis is correct. This statement is part of Mathlib: RiemannHypothesis and has been carefully vetted by experts in Lean and number theory." "By now, dozens of people have reported correct compilation of the codebase, reproducing the same raw proof export file." "That statement was compared against the theorem proved by Alpöge using two independent tools (comparator and con-leche –compare), both confirming that the theorem proved in Alpöge's library is exactly Mathlib's statement of the Riemann Hypothesis." "The exported raw proof has been checked by several proof checkers, including Lean's official kernel, the con-leche and con-ron checkers, and several independent checkers contributed by third parties and implemented in different programming languages." "We look forward to all the activity in the mathematical community that will help explain the new ideas in this proof." The statement does not mention the Generalized Riemann Hypothesis or Dirichlet L-functions.
- github.com/tamnd/riemann-lean, a mirror of the release, `lean/src/Main.lean`: five theorems, `riemannHypothesis : RiemannHypothesis`, `riemannZeta_eq_zero_re`, `LFunction_ne_zero_of_half_lt_re`, `LFunction_eq_zero_re` and `LFunction_eq_zero_re_of_isPrimitive`; its README: "The release has 175,187 Lean files, about 17.4 million lines and about 1.06 million declarations."
- https://www.claymath.org/ (front page, 23 Nov 2026): the latest news item is still "11 September 2026 Navier-Stokes Announcement".
- From coverage only, not opened at a primary source: that the author works at Anthropic; an independent run report by Andrew Sutherland at math.mit.edu (linked from the statement); and a separate human-written proof announced the same day, which is not on arXiv under that title and is not assessed here.
- To re-check at the next update: a written proof and its refereeing, Clay's position, the Dirichlet part, and the human-written proof.

**On the page:** added as item X2 (domain mathematics, tier 3, llm true, physical false, quantum false, preprint, 2026-11, P 1, H someday, W 4, C 0.9); LADDER row matter false, necessary true, leap none, qubits false, proposed for the author to confirm. The chart plots mathematics with the cryptography marker, and the legend says so.

## Looked at since 17 November 2026 and left off the page

- **OpenAI, "Advancing chip design with our models".** https://openai.com/index/advancing-chip-design-with-our-models/ could not be opened (`openai.com` refuses automated clients). Coverage describes model-assisted design of arithmetic circuits in the Jalapeño inference chip built with Broadcom. It would sit beside M4 if the post confirms model-designed circuits in fabricated silicon; no primary source was read, so nothing was added.

---

# Checks of 26 November 2026

Research for 17 to 26 November 2026: three items added and four updated. Open from the session that wrote them: `anthropic.com`, `arxiv.org` (records and full-text HTML), `github.com` raw files, `alpo.ge`, `claymath.org`. Still refused to automated clients: `openai.com`. Not opened: `hexagonmath.org`.

## 25. P12, a new item: Anthropic, "Claude solves two open problems in the physics of black holes", 17 November 2026

**VERIFIED** against the post. The two preprints it links (hexagonmath.org/2611.00175v1 and /2611.00174v1) were not opened.

- https://www.anthropic.com/research/claude-black-hole-physics (Published Nov 17, 2026; Science): "In the first, it completed a calculation that physicists set up more than 20 years ago, but which had never been solved. Claude's result showed that a sudden transition associated with the formation of black holes persists even where spacetime no longer has a definite shape. In the second, Claude found the exact limit of the simplest version of a technique used to test candidate theories of quantum gravity." "In 2003, a group of physicists set out the calculation that would settle the question, but it was extremely complex and was never completed … It showed that the phase transition is abrupt." "Neither result describes our own universe directly, and neither has practical applications".
- On method: "an Anthropic researcher, Hongbin Chen, was testing Claude's capabilities as a side project … Claude came back hours later with 22 candidates, and Hongbin set up separate agents to work on each one … The agents ran in the background, with no special setup, for about six weeks." "Weeks after one of the agents reached a solution, a physicist, who had independently used Claude to tackle the same problem, shared his result … The two solutions used different methods, so they were a useful check on each other." On the bootstrap result: "One half of the final proof, showing that the ceiling can't be lowered, follows the strategy of the OpenAI proof. In September, the results were formally verified in Lean, a computerized proof checker. Claude then wrote the paper with minimal guidance, and a physicist checked every main result."
- Conclusion: "Neither result settles the question of quantum gravity, or even comes close to doing so".

**On the page:** added as item P12 (tier 3, llm true, physical false, quantum false, preprint, 2026-11, P 3, H someday, W 2, C 0.8); LADDER row matter false, necessary true, leap none, qubits false.

## 26. P13, a new item: blow-up for the unforced three-dimensional Euler equations

**VERIFIED.**

- arXiv 2611.26772 v1, "Finite-Time Singularity Formation for the Three-Dimensional Euler Equations", Levent Alpöge, Tristan Buckmaster, Matei P. Coiculescu, submitted 19 Nov 2026; comments: "55 pages, 3 figures, LLM-assisted and Lean formalized". Abstract: "We construct smooth periodic initial data for the three-dimensional incompressible Euler equations whose solution blows up in finite time. The velocity remains bounded, while the vorticity magnitude at the origin tends to infinity."
- Section 1.7: "AI statement. We used Claude and Codex throughout this work. The first proof without force was written by Anthropic models from the drafts on the Euler equations with forcing and on the hypodissipative Navier–Stokes equations described in Subsection 1.6 … We then rewrote it with Claude and Codex under our direction … In the course of this we replaced parts of the argument by ideas of our own, which the models implemented."
- Section 1.6: "Before OpenAI released its paper on the unforced Euler equations, the first and second authors had completed a second proof of blow-up for the Euler equations with smooth forcing … this unreleased proof uses the same Craik–Criminale amplification mechanism as OpenAI's paper".
- https://github.com/mcoiculescu/EulerBlowupPublic, README: "a Lean 4 formalization by the authors of the arXiv version of the manuscript, in one-to-one correspondence with its proof … These theorems depend only on the axioms `propext`, `Classical.choice` and `Quot.sound`, and the sources contain no `sorry`." Exceptions: "Corollary 8.3 cites the periodic Beale–Kato–Majda criterion, which is not formalized."
- Not opened: OpenAI's paper on the unforced Euler equations.

**On the page:** added as item P13 (domain fluids, tier 3, llm true, physical false, quantum false, preprint, 2026-11, P 7, H decades, W 3, C 0.8); LADDER row matter false, necessary true, leap none, qubits false.

## 27. P14, a new item, and P8: a claimed blow-up for the Navier–Stokes equations without force

**VERIFIED** that the claim is made and what is and is not released; the proof itself cannot be checked yet.

- https://github.com/tristanbuckmaster/navier-stokes, `paper/finite-time-blow-up-navier-stokes.pdf` ("Finite-time blow-up for the Navier–Stokes equations", Levent Alpöge and Tristan Buckmaster; README: "79 pages, version of 20 November 2026"). Abstract: "We prove that there exist smooth, compactly supported, divergence-free initial data on R3, and smooth divergence-free initial data on the torus T3, for which the solutions of the three-dimensional Navier–Stokes equations without force blow up in finite time. This disproves the statements (A) and (B) of the Millennium Prize problem as formulated by Fefferman, and hence proves the statements (C) and (D) … The discretely self-similar solution is obtained from a certificate: an approximate solution that satisfies explicit inequalities. The certificate will be released soon; its hash is 3f7a335b84b6c7631742cacc5343dfcd11cf72f5221ff79b2b9268790b4b22c5." Section 1.6: "AI statement. We used Anthropic models (Claude) throughout this work, and no others."
- The repository's README: "The formalization contains no data. The certificate whose hash the paper gives is not in this repository; the paper says that it will be released. That the certificate satisfies the conditions of Appendix B is verified by a rigorous computation, involving interval arithmetic (128 bits of precision, with the Arb library through FLINT), which is not part of the formalization and is not in this repository either." "The source of the paper is not in this repository." "The patched package was not rebuilt when this repository was assembled."
- An arXiv search by author for 17 to 26 November returned the Euler paper only; the Navier–Stokes paper is not on arXiv.
- https://www.claymath.org/ (front page, 26 Nov 2026): the latest news item is still "11 September 2026 Navier-Stokes Announcement".

**On the page:** added as item P14 (domain fluids, tier 3, llm true, physical false, quantum false, preprint, 2026-11, P 7, H decades, W 4, C 0.4); LADDER row matter false, necessary true, leap none, qubits false. P8's caveat appended: its first words, "Unforced case still open", are kept and corrected.

## 28. P10 (Yang–Mills). The group's summary of OpenAI's second submission

**VERIFIED.**

- https://github.com/yang-mills-group/YM, README ("Updated 25 November 2026"): the first package is now described as "OpenAI's submission of 27 October 2026", with "Submission dates record when the group received the materials; the October archive retains its original filename date." The table lists "OpenAI, 4 November 2026 | November summary, 25 November 2026 | Verification records and AI-generated initial draft reports" and "Alpöge and Sussman, 15 November 2026 | work in progress".
- https://github.com/yang-mills-group/submissions, `docs/assessments/november-4-assessment.pdf` ("OpenAI Yang–Mills: November assessment … 25 November 2026"): "This supplements our October assessment. OpenAI's November submission strengthens the checks that the construction has the intended Yang–Mills fields and short-distance behavior. Its principal addition is matching to a specified perturbative reference at every finite order. Agreement of that reference with conventional Yang–Mills perturbation theory remains under review; human review so far is limited." "Both combined targets passed Comparator with standard Lean axioms only. Neither release establishes a mass gap or a unique infinite-volume limit." "It does not assert convergence of the series." "Supporting initial draft reports (AI-generated)".

**On the page:** `what` and `who` updated (submission date, the second submission); caveat appended. No label or rating changed.

## 29. P9 (OpenAI's catalogue). The additions of 23 and 24 November

**VERIFIED** (raw `README.md` and `history.md` of github.com/openai/math, fetched 26 November 2026).

- README: "The current catalogue contains 730 manuscripts organized into 375 families."
- history.md, "November 23, 2026": "*VP and VNP are different*. This result was obtained on November 6, 2026." "November 24, 2026": "We have added nine manuscripts across two result families, with Lean formalizations of selected results from each manuscript." Family 379, "Euclidean tensor geometry and its applications to complexity and combinatorics", seven manuscripts, among them "The matrix multiplication exponent is nine fourths", "Circuit lower bounds for Hamiltonian cycle and the permanent" and "An exponential bound for sunflowers". Family 380: "*Strongly polynomial linear programming* gives a deterministic strongly polynomial algorithm for linear programming, answering Smale's ninth problem." and "*Superpolynomial graph diameter of simple polytopes* disproves the polynomial Hirsch conjecture for bounded simple rational polytopes."
- These are complexity theory and combinatorics. They are noted on P9 because that item is the catalogue; none is a physics result.

**On the page:** `what` and caveat appended. No label or rating changed.

## 30. X2 (Riemann Hypothesis). Status on 26 November, and the author's employer

**VERIFIED.**

- https://alpo.ge/remark.pdf fetched again on 26 Nov 2026: same SHA-256 as on 23 Nov (`3fc97784…`), so the note is unchanged. The index page lists no written proof.
- https://alpo.ge/ : the heading reads "Levent Alpöge (pt&rl, anthropic, pbc / junior fellow, harvard sof …)", with "anthropic, pbc" linked to anthropic.com. This replaces "according to coverage" for his employer.
- https://www.claymath.org/ : nothing newer than 11 September 2026.
- From coverage only: a human-written proof by another author, posted the same day, which Scientific American says has not been verified by anyone; not on the page.

**On the page:** `who` no longer says "per coverage"; caveat appended.

## Looked at for 17 to 26 November 2026 and left off the page

- **OpenAI, "Advancing chip design with OpenAI models" (18 Nov, per coverage).** Still could not be opened; coverage says it reports model-made improvements in the Jalapeño chip and in AMD designs. It would be the strongest candidate of the period for step 1 of James's test, and it stays off until the post or a paper behind it has been read.
- **OpenAI, "Searching for distant planets with Astra" (24 Nov).** Not opened; coverage says amateurs flagged planet candidates in NASA data and that none is confirmed.
- **OpenAI, protein design with GPT-6 (24 Nov).** Biology.
- **Architect Labs, the Frostbite CPU (18 Nov).** A company post, not opened; coverage says agents designed a processor down to layout and that nothing has been fabricated.
- **arXiv, 17 to 26 Nov, no item made or measured anything new:** a layout benchmark for two-dimensional quantum devices (2611.30043), an agent on a mass-spectrometry instrument in an organic-dye campaign (2611.25043), a neural decoder for transversal gates in simulation (2611.31607), agent-built bases for Feynman integrals (2611.26688).
- **Not results:** a US Department of Energy award to Harvard and QuEra for AI-designed error correction; the launches of GPT-6.2 Astra and Gemini 4 Neon; DeepMind's post on quantum algorithms, which is the work of item Q10.

## What changed in `data/items.json` on 26 November 2026

| Item | Fields changed | Source |
|---|---|---|
| P12 | new item | anthropic.com post of 17 Nov 2026 |
| P13 | new item | arXiv 2611.26772; github.com/mcoiculescu/EulerBlowupPublic README |
| P14 | new item | github.com/tristanbuckmaster/navier-stokes, paper of 20 Nov 2026 and README |
| P8 | caveat (appended) | as P14; claymath.org |
| P9 | what, caveat (appended) | github.com/openai/math README and history.md |
| P10 | what, who, caveat (appended) | github.com/yang-mills-group/YM README; november-4-assessment.pdf |
| X2 | who, caveat (appended) | alpo.ge; claymath.org |

No caveat text removed; no label, flag or rating of an existing item changed. `data/ladder.json` gained rows for P12, P13 and P14, proposed for the author to confirm. None of the three reaches step 1 of James's test.
