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
