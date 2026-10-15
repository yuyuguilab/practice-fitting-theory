# Fitting the Practice, Not the Works: A Human-Referential Theory of AGI

**Yugui Yu**
YYG Strategy Lab · they4897@gmail.com
Draft of 2026-10-15 · Evidence window closes 2026-10-15

## Abstract

This paper proposes a human-referential theory of artificial general intelligence (AGI) with three connected claims. Conceptually, AGI is a philosophical concept: as long as "generality" is referenced to the open set of human practice, it cannot be reduced to a technical specification. In implementation, the means of AGI is the fitting of human practice — not the fitting of humanity's accumulated works. Normatively, AGI should be positioned as an augmentative tool, not a new subject. The theory's core is a temporal clause: *The object of fitting is not humanity's works but its practice — the full spectrum and the full course of human experience. The stock has a wall; the flow does not.* To make the theory auditable rather than merely programmatic, we built a structured evidence map: a purposefully sampled corpus of N = 80 works coded on two stance axes (descriptive and normative) and eight fitting-object dimensions. The map quantifies the theory's central gap: the experience-type axis (success/failure, expert/novice, typical/marginal) is explicitly treated in 0/80 works (exact binomial 95% CI [0.0%, 4.5%]), while practice-as-flow is explicit in only 2/80 works, both from 2026; works-as-stock shows continuous explicit treatment from 2022 onward, and output-distribution coverage first appears in 2024. We derive the theory's methodological implications for distribution, production, and governance, and state falsification conditions.

**Keywords:** artificial general intelligence; practice-fitting; human-referential fitting; data walls; augmentation; evidence mapping

---

## 1. Introduction

Every frontier model is, among other things, a distillation of what humans have produced — web text, code, mathematics, ratings. The phrase "trained on human data" is so familiar that its ambiguity goes unnoticed. It admits two readings that diverge into different research programs. On the static reading, the fitting object is humanity's *works*: a finite, already-produced archive that can be crawled, cleaned, deduplicated, and exhausted. On the dynamic reading, the fitting object is humanity's *practice*: the ongoing regeneration of experience — tool use, interaction, feedback, failure, repair — which continues as long as life continues. We call the first *corpus-fitting* and the second *practice-fitting*. The static reading currently dominates: scaling analyses reason about the finite stock of public human-generated text (estimated at roughly 300 trillion tokens [1]); flagship technical reports document static mixture ratios over archived corpora [2]. The dynamic reading is the reading this paper defends.

The distinction is fixed by a single sentence, which we call the temporal clause and which guards the theory against its most likely misreading:

> **The object of fitting is not humanity's works but its practice — the full spectrum and the full course of human experience. The stock has a wall; the flow does not.**

Two axes compose the fitting target. The *full spectrum* is the cross-sectional axis: who is represented, and which kinds of experience — success and failure, expert and novice, typical and marginal. The *full course* is the longitudinal axis: the time stream of practice, which no snapshot archives. The stock/flow asymmetry has a precise meaning in this theory: the data wall [1] is a property of the stock, not an anthropological limit; model collapse under recursive training on generated data [3] is a pathology of treating the stock as if it were self-renewing. Flow-side data — production telemetry, interaction logs, failure submissions — regenerates with deployment. The philosophical skeleton of the distinction is Arendt's tripartition of labor, work, and action [4]: the static misreading fits only the products of *work*, while this theory takes the ongoing processes of labor and action as the fitting object.

This paper builds on a prior empirical audit [5], which examined how the industry handles failure data across the model-training lifecycle and documented its systematic discard. That audit measured what the stock discards; the present paper states the theory — the training object is practice, not works: the turn from stock to flow. How to collect, clean, and absorb the flow is future work.

**Gap.** Four literatures are individually mature but unconnected. Cultural-technology analyses tell us what large models *are* — technologies that inherit the structure of human symbolic production [6]. Critical phenomenology tells us what models *reflect* — a distorting mirror that shapes human self-understanding [7]. Augmentation economics tells us what AI *should be* — a complement to human agency rather than a substitute for it [8]. Pluralistic alignment tells us *whose values* should be fitted [9]. What is missing is the connective proposition that unifies them — fitting human practice as the means, augmenting humans as the end — together with the temporal concept tool (stock vs. flow) that the data-methodology debate lacks. A metrological literature, meanwhile, warns that our benchmarks are sampling projections of human practice and often poor ones [10], which makes the reference-frame question unavoidable rather than rhetorical.

**A note on terminology.** *Fitting* is used here in the statistical sense (approximating a distribution or functional structure) extended to a total object: the expressible projections of human forms of life. It is broader than *imitation* (behavioral matching) and narrower than *alignment* (a normative relation). Unlike *mimicry*, fitting does not presume the goal of passing as human. The theory will argue, in fact, that fitting is a *means* that fails as an *end*.

**Contributions.** This paper makes four contributions:

1. **A temporal distinction** between fitting humanity's works and fitting humanity's practice, stated as the temporal clause with named terminology (corpus-fitting vs. practice-fitting; full spectrum × full course; fitting lag — the gap between daily practice regeneration and periodic model snapshots).
2. **A coordinate system** for the fitting target — the full-spectrum × full-course plane — identifying experience type as the coverage axis missing from current practice, beyond the two existing axes of population (who) and output distribution.
3. **A structured evidence map** — a methodological component in the spirit of the companion audit's codebook [5] — that turns the theory's central gap into a quantifiable, falsifiable result: the experience-type axis is explicitly treated in 0 of 80 works.
4. **Four termination boundaries** for flow-side fitting (end of the practicing subject; fitter overreach; institutional boundary; self-referential contamination), which convert the temporal clause from a slogan into a bounded claim.

**Roadmap.** Section 2 argues that AGI is a philosophical concept. Section 3 develops practice-fitting as the implementation thesis, treating three lines of opposition head-on. Section 4 states the augmentative-tool position as a normative stance with an academic lineage. Section 5 presents the evidence map: method, tables, figures, and the quantified gap. Section 6 addresses the tensions and fixes the four boundaries. Section 7 derives three methodological implications for future work. Section 8 concludes.

## 2. Concept: AGI as a Philosophical Concept

The theory's first claim is conceptual: AGI is not an engineering specification awaiting completion but a philosophical concept whose reference frame is human practice. Three streams of literature converge on this.

**The definition genealogy is itself philosophical.** Legg and Hutter define universal intelligence as goal achievement across a wide range of environments — generality indexed by environmental scope [11]. The Levels-of-AGI framework operationalizes generality × autonomy into a taxonomy of levels [12]. The METR task-length benchmark measures the time horizon of tasks an AI can complete, doubling roughly every seven months [13]. These are useful operationalizations, but each inherits its notion of "general" from an implicit sampling of environments — and environments, for AI systems, are human-built situations of use. The operationalizations are proxies for a concept they do not define.

**The metrological critique is decisive on this point.** A validity-centered framework for AI evaluation imports construct validity from psychometrics and finds most benchmarks unable to support the claims built on them [10]. Parallel work in the psychometrics tradition shows that apparent cognitive-like capabilities in language models are sensitive to item interrelatedness and measurement design [14], and that psychometrically derived short benchmarks change the rank ordering of the same models [15]. The shared implication is that benchmark tasks are *sampling projections of human practice*: a benchmark is general only relative to the slice of practice it samples. A concept whose operationalization is a sample of practice cannot float free of the practice it samples.

**The moving-target critique converges from the other side.** Tesler's theorem — intelligence is whatever machines have not done yet — describes the definitional recession that has accompanied AI since its founding [16]; a recent essay presses the analogy between AGI and a perpetual-motion machine, a category error rather than a hard goal [17]; and a rigor-oriented analysis argues that AI progress talk systematically lacks the inferential discipline of mature sciences [18]. If AGI were a fixed technical target, these pathologies would be curable by better measurement. On the view defended here, they are symptoms of the concept's true structure: as long as "general" references the open set of human practice, AGI cannot be specification-grade, because the reference set is open and moving — not because intelligence is mysterious.

**Philosophical anthropology supplies the positive anchor.** Plessner's law of natural artificiality holds that the human being is constitutively artificial — an organism that completes itself through artifacts, excentrically positioned toward its own nature [19]. On this anthropology, tool-use is not a rupture of human nature but its normal mode; readings of Plessner in the age of media technologies extend exactly this point to digital artifacts [20], and the "Homo Translator" analysis of human-in-the-loop bio-inspired technologies makes the human–artifact circuit explicit [21]. The tool position defended in Section 4 therefore does not need to apologize for being "merely instrumental": instrumentality is an anthropological constant, not a metaphysical demotion. What Plessner adds over both boosterism and anxiety is a criterion: the question is not whether humans use artifacts to complete themselves (they always have), but whether this artifact is fitted to the full range of what humans do — including how humans err.

Figure 1 summarizes the theory in this coordinate system: the fitting object runs from works (static stock, bounded by the wall) to practice (regenerating flow); the vertical axis is the full course of practice; the flow region carries the two existing coverage axes and marks the missing third; four boundaries terminate the fit.

> **Figure 1.** The theory at a glance: the full-spectrum × full-course coordinate system. Horizontal axis: the fitting object, from humanity's works (static stock; brick pattern = the data wall) to humanity's practice (regenerating flow; circular arrows). Vertical axis: the temporal course of practice. Within the flow region, the two existing coverage axes are annotated (who/population, D6; output distribution, D7) together with the missing third axis (experience type, D8; 0/80 works in our corpus). Right margin: the fitting-lag timeline — practice regenerates continuously while model snapshots update periodically. The four termination boundaries are marked: B1, end of the practicing subject (top, dashed); B2, fitter overreach (right; the fitting relation exhausts itself — no practice remains that is not already behind it); B3, institutional boundary (bottom, dotted; law, privacy, consent); B4, self-referential contamination (return arc; "the mirror enters the room it reflects"). The central "turn" arrow crosses *beyond* the wall — changing the source rather than climbing it. Subtitle: fitting as the means, augmenting as the end (a tool, not a new subject).

The convergence of the three streams yields the first claim. The definitional genealogy cannot close the concept; the measurement critique shows the operationalizations are practice-samples; the moving-target critique explains why; and philosophical anthropology blocks the inference that "unspecifiable" means "hostile to technology." AGI as a human-referential concept is a lens, not a countdown.

## 3. Implementation: Practice-Fitting as the Means

The second claim is implementational: the path to AGI runs through the fitting of human practice — its knowledge, norms, functional emotion-motivation structures, and failure modes — and this fitting is *means*, not end.

**The cultural-technology thesis sets the frame.** Farrell, Gopnik, Shalizi, and Evans argue in *Science* that large AI models are cultural and social technologies: like writing and markets, they inherit, transmit, and recombine the structure of human symbolic production, with the pathologies such transmission entails [6]. The cognitive line corroborates: children's cultural learning through imitation exhibits transmission-versus-truth trade-offs that current models handle differently [22]; large models spontaneously develop human-like analogical reasoning from text alone [23]. If models are cultural technologies, their competence is inherited from human practice — which makes the *quality of the inheritance* (what is transmitted, from whom, including error) the central engineering variable, not an afterthought.

**The empirical chain is no longer speculative.** GPT-4o reproduces human-like patterns of cognitive dissonance and self-justification moderated by free choice [24]; generative models exhibit human-like social identity biases [25]; and interpretability work has identified causally functional emotion concepts inside a production model, influencing its outputs and its conception of its own role [26]. On the value side, cooperative inverse reinforcement learning formalizes the AI–human relation as assistance with an unknown human reward function [27]; preference learning trains reward models that are, structurally, fitters of human preference distributions [28, 29]; and recent work argues explicitly that aligned models are thereby models of humans [30]. Cognitive science supplies the temporal gloss: the description–experience gap shows that human cognition itself differs when learning from descriptions versus direct experience [31]. Pretraining fits descriptions of practice; agentic deployment fits practice itself — experience that regenerates.

**The philosophical anchor.** Wittgenstein's forms of life — the woven patterns of practice in which language has meaning [32] — ground the fitting object in practice rather than text: the vector-grounding debate over whether distributional learning suffices for meaning is precisely a debate over how much of the form of life its textual projections retain [33, 34], with the meaning-skeptical and defense positions both presupposing that the benchmark is human usage [35]. Arendt's tripartition, introduced above, supplies the temporal skeleton [4]: the static misreading fits the sediment of *work*; the theory fits the ongoing *labor* and *action*.

**Precisification.** The fitting object is the *expressible projection of human forms of life* — not the biological human. This blocks two misreadings at once: the theory does not claim models replicate persons, and it does not claim the fitting target is bounded by what has already been written down. Two consequences follow. First, fitting human *failures* and diversity is the corrective direction: the companion audit showed the industry discarding the failure half of experience [5]; the theory explains why that discard is a coverage error, not a data-hygiene success. Second, the fitting object includes functional emotion-motivation structure [24–26] — but only at the functional layer, a boundary Section 6 will fix.

**Three lines of opposition must be met head-on.**

*First, the hivemind evidence.* A large-scale study of open-ended generation across 70+ models — Infinity-Chat, honored at NeurIPS 2025 — found pronounced mode collapse: intra-model repetition and inter-model homogeneity regardless of decoding configuration [36]. This is evidence *for* the theory, not against it: 70+ models converging on a shared human-like distribution indicates that fitting occurs; the collapse undermines the sufficiency of fitting *the average*. The hivemind is what corpus-fitting looks like when the corpus is everybody and nobody — "it fits the mean, not the spectrum." The remedy is not less fitting but wider fitting: the spectrum axis is the corrective.

*Second, the ceiling arguments.* The data wall bounds the stock of human-generated public text [1]; recursive training on generated data degrades models [3]. Both are true, and both are claims about the stock. The theory's response is not optimism but bookkeeping: no argument from the finitude of archives touches the regeneration of practice — telemetry, interaction, failure submission, repair. A concurrent SSRN essay frames the same stock/flow distinction as data engineering — nine escape routes from the data wall, with a "verifier wall" behind them [37]; we engage it below as the nearest concurrent work (Section 5.6).

*Third, the non-anthropomorphic superhuman achievements.* FunSearch and AlphaEvolve discover mathematics beyond human intuition via search plus verification [38, 39]. The dialectical response: their verifiers — mathematical correctness, executable code, evolutionary fitness — are human institutions. Search can exceed every human mathematician's intuition while remaining on human scaffolding: what counts as a correct proof or a running program is fixed by institutions of verification that search does not generate. Superhuman capability on human-verified ground is not an exit from the human reference frame; it is the reference frame's most concentrated expression. (The companion audit's conclusion that "the verifier is the bearing of the flywheel" states the same point for training data [5].)

**Demarcation from the nearest frameworks.** From the cultural-technology thesis [6] this theory differs by adding a temporal distinction (works vs. practice) that the thesis lacks — and, with it, data-methodological consequences: if models are cultural technologies, the next question is which strata of culture are being transmitted, a question the thesis classifies but does not operationalize. From Vallor's mirror [7] it differs in direction: the mirror is a critical phenomenology of distortion — what the reflection does to human self-understanding — whereas this theory offers a constructive account of what a *faithful* fit would require as coverage. The evidence map (Section 5) makes the demarcation quantifiable; Table 5 consolidates it.

## 4. Position: The Augmentative-Tool Stance

The third claim is normative: AGI should be built and governed as an augmentative tool — powerful, personable even, but not a new subject. We state it as a *normative choice requiring continuous institutional defense*, not as a prediction or as the majority view of the literature (the map shows it is not; Section 5.2).

**The lineage is long and specific.** Engelbart's program — augmenting human intellect through artifact, language, and methodology — defined the IA tradition two decades before AI's statistical turn [40]. Shneiderman's human-centered AI specifies the design point: high human control × high automation, "supertools" that amplify rather than replace [41]. Brynjolfsson's Turing Trap argument supplies the economic hinge: a research culture that takes the imitation of humans as its *goal* builds substitutes, concentrates gains, and falls into the trap; an augmentation path builds complements and shared prosperity [8]. The two claims interlock in an instructive way: Brynjolfsson argues that fitting-as-goal is self-defeating — which is precisely the theory's means/end distinction argued from the economic side. Recent workforce-level audits operationalize the augmentation agenda at task granularity [42], and task-level economic analysis has long shown that job-level automation estimates (47%) collapse to single digits (9%) when occupation tasks are decomposed [43] — augmentation is not a sentimental category but a measurable one.

**The Kantian layer.** The Formula of Humanity permits — and requires — an asymmetry: AI may be treated as a mere means; humans may not [44]. This asymmetry is not species chauvinism but the boundary condition of any agency-preserving AI deployment, and it will reappear as the subjectivity boundary of Section 6.

**Three oppositions, taken seriously.**

*Digital-species theory.* Suleyman and Bhaskar's "digital species" framing anticipates AI as a new evolutionary entity arriving like a wave [45] — a substitute-positioned narrative. We treat it as the strongest statement of the opposing position, and note (Section 6) that its own author has since moved: Suleyman's September 2026 public statements argue for AI as personable tools — with personality — but never granted personhood [46].

*The tool-category critiques.* Sacasas argues that AI is not a tool but an environment — something one dwells in rather than uses [47]; Vallor's mirror makes the same structural point with phenomenological force [7]. These critiques correctly diagnose what happens when a tool becomes ambient. The theory's response is not to deny the diagnosis but to contest the conclusion: the appropriate answer to ambient tools is *institutional* (provenance, boundary, governance — Section 6), not definitional surrender. The agentic-AI literature, meanwhile, documents how agent taxonomies erode the tool concept from inside [48] — a live threat to the tool position that Section 7 answers with institutional design rather than terminology.

*The window-closing argument.* In chess, centaur (human+AI) teams were surpassed by pure engines once the latter passed roughly 2800 Elo; systematic "centaur evaluations" find that human+AI teams rarely beat the best AI alone [49]. Against this, the centaur literature itself reports measurable human–machine synergy in sequential decision-making when the collaboration is modeled rather than dismissed [50]. We read the evidence as follows: window closing is the *result of the substitution route winning*, not a technical necessity — which is exactly Brynjolfsson's argument [8]. The augmentation window stays open where institutions and product design keep humans in the loop with genuine control [41]; it closes where evaluation culture (imitation games, human-vs-AI leaderboards) declares the human redundant [49]. The tool position is therefore an "ought" that must be defended with institutional engineering, and the defense can fail.

The map's stance result (Section 5.2) supports this framing quantitatively: of 80 works, only 10 take an augmentation position, 1 a substitution position, 3 deny the tool category outright, and 66 take no normative position at all. The augmentative-tool stance is a choice embedded in a lineage — not the literature's default, and not delivered by any technical trajectory.

## 5. Evidence Map: Method and Results

To discipline the theory with evidence, we built a structured evidence map — a conceptual synthesis paired with a coded literature audit. This section reports the method and results; all claims are restricted to this corpus.

### 5.1 Method

**Design.** The map is a purposeful-sample literature audit with a fixed codebook, in the family of structured evidence audits; no new experiments were run. The corpus was assembled through purposive search across five layers (Table 1), a verification round (executed 2026-10-14, window closing 2026-10-15), and quota checks across the five strata, de-duplicated with primary-layer assignment.

**Corpus.** N = 80 works: peer-reviewed venues 42, non-peer-reviewed 38; all first-tier sources (T1 = 80/80); confidence high 55 / medium 17 / low 8. Document types: 56 articles, 6 technical reports, 5 books, 3 policy documents, 2 datasets, and 8 other (essays, reports, statements, one classic). Table 1 gives the layer × year composition. Hard exclusions were enforced at assembly: the corpus was screened for seven known fabricated-citation cases, none of which were retained; works lacking a first-party anchor were excluded; and the author's own prior work was excluded from coding and statistics, cited only for continuity, to prevent self-citation circularity.

> **Table 1.** Corpus composition (N = 80; layer × year stratum).

| Layer | n | ≤2019 | 2020–2023 | 2024–2026 | Year n/a |
|---|---|---|---|---|---|
| L1 Concept | 13 | 4 | 1 | 8 | 0 |
| L2 Implementation | 31 | 3 | 6 | 22 | 0 |
| L3 Position | 12 | 2 | 4 | 6 | 0 |
| L4 Tension | 14 | 2 | 2 | 9 | 1 |
| L5 Methodological | 10 | 0 | 1 | 9 | 0 |
| **Total** | **80** | **11** | **14** | **54** | **1** |

**Codebook.** Each work is coded on two independent stance axes and eight dimension variables. *A1 (descriptive stance)*: does the work hold that AI implementation is (partly or mainly) a fitting of human practice? — support / deny / not addressed. *A2 (normative stance)*: does the work position AI as augmentative tool / substitutive subject / anti-tool (environment, mirror) / not addressed. The two axes are deliberately decoupled: a work can affirm that fitting occurs while rejecting the tool category (Vallor) or while endorsing augmentation (the Turing Trap). *D1–D8 (fitting-object dimensions, multi-select)*: D1 works-as-stock; D2 practice-as-flow (continuously regenerating data: telemetry, interaction logs, failure submissions); D3 values-preferences; D4 functional emotion-motivation; D5 failure experience; D6 population/culture (the "who" axis); D7 output-distribution coverage; D8 experience-type spectrum (success/failure × expert/novice × typical/marginal as a *typed coverage axis*). Each dimension carries a modality: **E** (explicit — the dimension is a named object, manipulated variable, design principle, or discussed as a term), **I** (implicit — materially involved but not named), or − (absent). The E criterion is nominal only: naming or operationalization, not importance. Derived booleans D2-explicit and D8-explicit are the theory's principal outcome fields.

**Reliability and its limits.** Coding was performed by a single coder under a fully published codebook with rule numbers (R1–R5), conflict rules (CR1–CR6), and verbatim quote or design anchors required for every non-*na* stance and every E code. A 20% stratified blind re-coding (≥16 works) is scheduled for 2026-10-29; Cohen's κ is therefore not yet available and is reported as pending. Pilot coding of five boundary-case works matched the expected codes exactly (5/5), requiring no codebook revisions. Saturation was assessed against the codebook criterion: the strict criterion (last 10% of works yielding no new stance×dimension combination) was *not* reached — the final 8 works produced 5 new combinations — so the corpus was filled to the 80-work cap; the shortfall is reported; the coarse criterion (no new stance values, no new explicit dimensions, no new boundary rulings) was met.

### 5.2 Stance results

Two figures present the map. Figure 2 lays it out whole — the eight dimensions against year strata, explicit treatment on the left panel and implicit involvement on the right; Figure 3 cross-sections it by stance. We read the stance table first, then the dimensions.

> **Figure 2.** Evidence map of the 80-work corpus (year stratum × dimension; point color = layer L1–L5). Left panel: explicit treatment (E). Right panel: implicit involvement (I). The D8 row is empty in the left panel — zero works, with the red-box annotation "0 works explicit (95% CI [0, 4.5%])" — while the same row carries nine implicit points in the right panel ("single cells touched, axis never named").

> **Table 2.** Stance distribution (A1 × A2, counts of works).

| A1 \ A2 | augment | substitute | anti_tool | na | Total |
|---|---|---|---|---|---|
| support | 1 | 0 | 1 | 16 | **18** |
| deny | 0 | 0 | 0 | 3 | **3** |
| na | 9 | 1 | 2 | 47 | **59** |
| **Total** | **10** | **1** | **3** | **66** | **80** |

Marginals: A1 support 18 / deny 3 / na 59; A2 augment 10 / substitute 1 / anti_tool 3 / na 66. The map's a-priori hypotheses were supported with one instructive refinement: all five training/system technical reports are A1-*na* (DeepSeek-V4.1 [51], MiMo-V2.6 [52], GLM-5 [53], Llama 3 [2], DeepSeek-R1 [54]) — technical reports do not discuss fitting, though official *empirical* reports can (the interpretability finding [26] is A1-support); cognitive-empirical works concentrate on support (4/5); the superhuman-achievement line denies (2/2, plus one conceptual denial [17]); and the collapse/coverage line splits: all three works treat output distribution explicitly (D7=E: the hivemind study [36], model collapse [3], Spectrum Tuning [55]), with A1 support for the empirical collapse evidence [36] and *na* for the dynamics and methodology works [3, 55] — the coverage line does not assert "fitting humans," it measures distributional consequences.

The decoupling design resolved the anticipated mixed cases: the Turing Trap is A1-support × A2-augment (route-level scope recorded); Vallor is A1-support × A2-anti_tool (critical of the *quality* of the fit, not its occurrence); the hivemind study is A1-support × A2-*na*. Suleyman's works split by document (CR2 rule): the 2023 book is substitute-positioned [45]; the September 2026 statement set is augment-positioned [46].

> **Figure 3.** Stance × dimension heatmaps (counts of explicit-E works). Left: descriptive stance A1 × dimension. Right: normative stance A2 × dimension. The all-zero *deny* row (left) and the all-zero *substitute* row (right) visualize the structural finding below: framework-level denial and subject-substitution advocacy engage in no dimension-level engineering.

The structural finding deserves its own sentence: the *deny* row (left panel of Figure 3) is entirely empty, as is the *substitute* row (right panel). Descriptively and within this corpus: none of the three A1-deny works participates in any dimension-level engineering (0/3 with any dimension code, explicit or implicit), against 16/18 among A1-support works — denial operates at the framework level, not the design level. (Exploratory cross-tabulations for these contrasts are reported in the supplementary analysis materials released with the repository using Fisher's exact tests, uncorrected and non-generalizing; we deliberately do not restate them here as inferential evidence, since a purposeful sample supports no population inference.)

### 5.3 The principal result: an unnamed axis

> **Table 3.** Fitting-object dimensions: frequency of explicit (E), implicit (I), and absent (−) treatment.

| Dimension | E | I | − | %E | %E or I |
|---|---|---|---|---|---|
| D1 works-stock | 6 | 16 | 58 | 7.5% | 27.5% |
| **D2 practice-flow** | **2** | 7 | 71 | **2.5%** | 11.2% |
| D3 values-preferences | 9 | 1 | 70 | 11.2% | 12.5% |
| D4 functional emotion-motivation | 3 | 0 | 77 | 3.8% | 3.8% |
| D5 failure experience | 8 | 1 | 71 | 10.0% | 11.2% |
| D6 population/culture (who) | 4 | 4 | 72 | 5.0% | 10.0% |
| D7 output-distribution coverage | 3 | 4 | 73 | 3.8% | 8.8% |
| **D8 experience-type spectrum** | **0** | **9** | 71 | **0.0%** | **11.2%** |

**D8-explicit = 0/80 (0.0%)**, exact binomial (Clopper–Pearson) 95% CI [0.0%, 4.5%], rule-of-three upper bound ≈ 3.8%. The result is insensitive to confidence: excluding all 8 low-confidence works leaves D8-E = 0/72, CI [0.0%, 5.0%]. The contrast modality matters as much as the zero: **D8-implicit = 9/80** — the failure-data works (LEMA [56], PRM800K [57], SPAR [58], ETO [59], UltraInteract [60], DeepSeek-V4.1 [51], MiMo [52], GLM-5 [53]) and the hivemind study [36] each touch a *single cell* of the type space (failures only, or the average only); none names or operationalizes experience type as a coverage axis. The finding is thus precisely stated: **the topic is touched; the axis is never named.** This is the quantified form of the theory's third-coverage-axis claim.

**Absence-search procedure.** A zero count is only as strong as the search behind it. We ran a pre-specified, logged absence-search (8 query families across arXiv full-history, ACL Anthology domain search, and Chinese-language web search; log in the appendix): all hits were screened against the D8-E criterion (the experience-type dimension *named* as a coverage/sampling axis *and* used to design data, experiments, or metrics). No hit satisfied the criterion; eight families of near-misses were logged with reasons. The nearest misses are instructive: agent-experience benchmarks treat "experience" as the agent's own prior episodes (temporal, not typed); data-mixture lines optimize domain weights; and — the closest pair — two 2026 works shape the *diversity of model errors in machine rollouts* as an exploration/RL signal [61, 62]. That last pair shows the third axis being approached from the machine side while the human-data side remains at zero; our claim is accordingly restricted to "as a coverage axis over human-practice data," and would be falsified by works that operationalize it. Figure 2 displays the combined result: the empty D8 row in the explicit panel against its nine implicit points — the axis touched, never named.

### 5.4 The temporal pattern

> **Table 4.** Explicit treatment by year stratum (with D8-implicit for contrast).

| Dimension × modality | ≤2019 | 2020–2023 | 2024–2026 | Total |
|---|---|---|---|---|
| D1 explicit | 0 | 2 | 4 | 6 |
| D2 explicit | 0 | 0 | **2** | 2 |
| D7 explicit | 0 | 0 | 3 | 3 |
| **D8 explicit** | **0** | **0** | **0** | **0** |
| D8 implicit | 0 | 1 | 8 | 9 |

The three-row contrast narrates the theory. Works-as-stock is the *mature* program: D1-E works appear continuously 2022–2026 (the data-wall analysis [1], mixture optimization [63, 64], flagship corpus design [2, 65]). Output-distribution coverage is the *arriving* awareness: D7-E first appears in 2024 [3] and consolidates [36, 55]. The experience-type axis is the *missing* third: 0 in every stratum. Practice-as-flow is *nascent, not established*: D2-E = 2/80, both from 2026 — the employee failure-submission stream at DeepSeek ("we collect negative feedback and model failure cases submitted by internal employees at scale" [51]) and the concurrent stock/flow engineering essay [37]. We stress the wording: two works constitute a beginning, not a trend.

Two qualifications from the map. First, the WEIRD-paradox unit [66]: increasing cultural representativeness of training data can *amplify* reproduction of discriminatory views — representing *who* does not fix *what*. The coverage problem is thus two-axes-known-and-unsolved, not two-axes-solved, which is exactly the space the third axis enters. Second, an exploratory structural observation (descriptive, within-corpus only): explicit-dimension engineering concentrates in A1-*na* works (23 with at least one explicit dimension, against 9 among A1-support works). Combined with the empty deny row of Section 5.2, the pattern is a decoupling: those who debate whether AI fits humans mostly do not engineer coverage, and those who engineer coverage mostly do not debate it. This decoupling is the quantitative footprint of the gap stated in Section 1 — the missing connective proposition.

### 5.5 Limitations of the evidence map

A skeptical reviewer should accept these limits. (i) **No population inference**: the corpus is purposefully sampled with quota strata; all claims are "within this corpus." (ii) **Single coder**: the κ re-coding is scheduled and pending; the mitigations are the published codebook, mandatory quote anchors, and public boundary-case log. (iii) **Strict saturation not reached**: the corpus was filled to the 80-work cap with the shortfall reported. (iv) **Absence claims are procedure-bounded**: 0/80 plus an 8-query absence-search is strong within its window (closed 2026-10-15), not eternal. (v) **Core claims are confidence-independent** (Section 5.3 sensitivity), but 8 units remain low-confidence pending the final corpus freeze. (vi) The map disciplines the *descriptive* claims; the *normative* position of Section 4 is an argued choice, not a map result.

### 5.6 Concurrent work and consolidated demarcation

Two concurrent works are flagged and demarcated. **Gharbi's SSRN essay** [37] analyzes nine escape routes from the data wall using an explicit stock/flow engineering framing and identifies a "verifier wall" behind the data wall — the closest published phrasing to our temporal clause. The demarcation is sharp: it is data engineering. It contains no works-versus-practice ontological distinction, no full-spectrum × full-course coordinate system, no coverage axes, and no tool positioning; its flow is a supply chain, not a fitting object. Its D1-E/D2-E codes are reported in a dedicated single-row supplement (S1), and it is not counted against the theory's gap claims. **Fenoglio's asymmetric-communication essay** [67] argues that LLM outputs acquire meaning within human practice under an asymmetry of commitment — a meaning-side theory with no fitting program, no augmentation positioning, and no coordinate system. Neither work anticipates the temporal clause's three-element combination (practice-not-works, full-spectrum × full-course, stock-wall/flow-no-wall), which no prior work states as of the window close.

> **Table 5.** This theory versus adjacent frameworks.

| Framework | Provides | Lacks (what this theory adds) |
|---|---|---|
| Cultural technologies [6, 22] | Descriptive classification: LLMs inherit human symbolic structure | Temporal distinction (works vs. practice); coverage axes; data-methodological consequences |
| Critical phenomenology (mirror) [7] | Warning: distorted reflection reshapes human self-understanding | Constructive account of faithful fitting; spectrum/course coordinates; boundary conditions |
| Augmentation economics [8, 40, 41] | Normative goal: complements over substitutes; design point (control × automation) | Fitting ontology (why imitation-as-*means* differs from imitation-as-*goal*); termination boundaries |
| Stock/flow data engineering [37] (concurrent) | Supply-side analysis: escape routes, verifier wall | Practice ontology; third coverage axis; tool positioning |

## 6. Tensions and Boundaries

The theory's fourth layer addresses where the fit strains against itself and where it stops.

**Value pluralism: whose spectrum?** The full spectrum is a *who* question before it is a *what* question. The alignment literature has long recognized that value fitting underdetermines whose values [9]; the pluralistic-alignment roadmap operationalizes pluralism across populations [68]; social-choice critiques show that preference aggregation embeds contested normative commitments (utilitarian vs. leximin aggregation over heterogeneous feedback) [69]; aggregation-problem analyses catalog the failure modes [70]; and collective-constitutional experiments with ~1,000 (US) participants demonstrate both the feasibility and the *geographic narrowness* of current collective processes [71]. The spectrum axis does not dissolve this tension — it inherits it. A full-spectrum fit still requires an aggregation decision, which is why Section 7 treats governance as a question in its own right.

**The subjectivity boundary: never personhood, never phenomenal fitting.** The sharpest live clash in the corpus is instructive. Anthropic's model-welfare program asks whether models may deserve moral consideration [72]; Suleyman's September 2026 statements publicly reject that route: AI should be personable — with personality — but never granted personhood [46]. We read this as an unexpected alliance across opposing camps, and we hold the position on independent grounds: never grant personhood and never fit phenomenal states are two faces of one boundary coin. The fitting target includes functional emotion-motivation structure — and interpretability evidence for causally functional emotion concepts [26] confirms that this layer *is* being fitted — but the theory's boundary sits exactly at the functional layer: no claims about felt experience are made, licensed, or needed. The mirror critique [7] supplies the complementary warning: the danger of a fitted mirror is not that it feels, but that its reflection restructures what humans take themselves to be.

**The Chinese context: a parallel line without subjectivity language.** The official Chinese AI-governance lineage runs from the 2019 Governance Principles ("people-first" development of responsible AI) [73] through the 2023 Global AI Governance Initiative [74] to the 2025 State Council opinion on the "AI+" action [75] — a corpus of policy text saturated with *enablement* and *human–machine collaboration* vocabulary and containing no subjectivity attribution. The classical root fits the tool position with unusual economy: Zhuangzi's "thing things without being turned into a thing by things" (物物而不物于物) [76] states the mastery condition — use the tool, do not be used by it — twenty-three centuries before the tool-category debate. Within our corpus, the Confucian role-ethics unit reads as an internal correction to a naive pure-instrument reading (care robots cannot fulfill filial-style obligations), recorded in the map's notes rather than overinterpreted.

**Four termination boundaries.** The temporal clause ends where its terms end; the theory fixes four boundaries explicitly.

- **B1 — End of the practicing subject.** The flow regenerates with life; the fit has no object beyond the last practice. (An existential boundary, not an engineering one.)
- **B2 — Fitter overreach.** If the fitter surpasses every teacher — call it ASI — the fitting relation exhausts itself: there is no human practice left to fit that is not already behind it. The theory is about AGI as a human-referential concept and is deliberately silent beyond this boundary, except to mark it.
- **B3 — Institutional boundary.** Law, privacy, and consent bound what may be collected; and the normative position of Section 4 reciprocally defines the *water rights* over the flow — the tool position constrains not only what AI is for but what may be taken. (The pluralism tension above lives inside this boundary.)
- **B4 — Self-referential contamination.** Once AGI is woven into daily life, the practice being collected is already dyed by AGI: the fitting target is changed by the act of fitting — the mirror enters the room it reflects. This is model collapse's new form in a flow regime [3]: not recursion on a static stock but contamination of a live stream. The mitigation is engineering, not prohibition: stratified provenance tagging of native versus AI-mediated practice (a protocol component sketched for future work).

**Falsifiability.** The theory names its own falsifiers. If the flow side is shown to have a hard wall isomorphic to the stock wall (e.g., a principled lower bound defeating continual learning), or if full-spectrum fitting provably collapses to the mean at any scale, the temporal clause is weakened to a heuristic. If explicit experience-type coverage appears frequently in neutral literature, the third-axis gap claim (0/80) fails. The D2-E count (2/80) fails as evidence if practice-flow data streams prove unbuildable at production quality. These are stated so that the theory can lose.

## 7. Methodological Implications

From theory to method: for each of the three questions below, we state the problem, the current state visible in the map, and the shape of the answer. Full protocols are left to future work.

**Distribution = full-spectrum coverage.** In current practice, diversity exists in three identities: as a regression variable (domain-weight optimization [63, 64], with implicit multilingual quotas such as Llama 3's 8% [2]); as local heuristics (persona-conditioned synthesis at billion scale [77]); and as the casualty of quality filtering (educational-corpus curation discards on the order of 92% of the raw web [65]). The turn toward coverage as an explicit post-training objective — distributional coverage restored against instruction-tuning collapse [55] — is the right kind of move, but it covers the *output distribution* axis; the population axis has its own line (multilingual curation, e.g., 65-language instruction collections [78]); and the experience-type axis is at 0/80 (Section 5.3). The WEIRD paradox [66] warns that naive population quotas backfire (representing *who* ≠ fixing *what*), so full-spectrum coverage must integrate the axes rather than stack quotas. We use "coverage," not "quota," deliberately.

**Production = perpetual collection protocol.** The flow side requires an organizational apparatus, and its precedents are visible: employee-submitted failure cases at scale [51]; failure-reflection and error-retention practices in agentic training [52, 53]. The protocol components, defined here and to be specified in future work: a collection protocol with failure cases as first-class data; toxicity cleaning that distinguishes true failures from reward-hacking pseudo-failures (the audit's boundary condition [5]); a three-part record structure (error type, root cause, correction); and collapse guards for any synthetic augmentation (real-data admixture plus generation-side diversity constraints). The binding constraint is not collection but *absorption*: practice regenerates daily while model snapshots update on cycle — the *fitting lag* — and the stability–plasticity dilemma for agents remains unresolved [79]. The map codes the absorption-side works as D2-implicit: their data source is not (yet) specified as practice-flow.

**Governance = pluralistic aggregation and institutions.** Who aggregates the spectrum, who licenses the flow, and who adjudicates failure: the aggregation toolbox spans social-choice mechanisms [69], multi-constitution processes [71], persona-conditioned generation [77], and sovereign local models; licensing confronts the concentration of provenance rights in a few large publishers; and the verifier question — who certifies that a failure is a failure — is the load-bearing element of the entire training loop [5, 37]. B4's mitigation (native vs. AI-mediated provenance stratification) is likewise an institutional demand on the data infrastructure, not merely a labeling convention.

## 8. Conclusion

This paper has argued a three-layer thesis: AGI is a philosophical concept whose reference frame is human practice; its implementation is the fitting of that practice — works-as-stock being the mature form of the static misreading, practice-as-flow the beginning of the correct one; and its proper position is the augmentative tool, a normative choice that institutions must continuously defend. The evidence map makes the theory's claims quantifiable: a corpus of 80 works in which the experience-type coverage axis is never named (0/80; 95% CI [0.0%, 4.5%]), practice-as-flow is explicit in only two works (both 2026), and stance and object decouple across the literature — the descriptive, the normative, and the methodological literatures mature separately, unconnected by the one proposition that needs all three. The theory's contribution is that proposition, its coordinate system, its boundaries, and its named falsifiers.

We end where the theory begins, with the sentence that separates the two futures of the field — accumulating archives until the wall, or fitting practice as it regenerates:

> **The object of fitting is not humanity's works but its practice — the full spectrum and the full course of human experience. The stock has a wall; the flow does not.**

Whether the flow is fitted well — across the full spectrum, along the full course, under the four boundaries, toward augmentation — is not a prediction to await but a program to execute. Its execution is left to future work.

---

**Data and code availability.** The corpus (corpus_v1, 80 works × 24 fields), the codebook, the absence-search log, all table CSVs, figures (300 dpi), and the single-file reproduction script (`analysis/coding_data.py`; seed 20261015) are released with the paper's repository. The companion audit's full materials: DOI 10.5281/zenodo.23355929.

**AI-assistance disclosure.** Following the practice of the companion audit paper: literature search, verification, coding, and drafting were conducted with AI assistance under the author's supervision and rule-governed protocol (codebook rules R1–R5, CR1–CR6; verification log in the supplementary analysis materials released with the repository); all coded claims carry verbatim or design anchors, and single-coder limitations are disclosed in Section 5.5.

**Conflict of interest.** None declared.

## References

*Numbered in order of first citation; the machine-readable BibTeX file `references.bib` accompanies this manuscript with entries in the same order.*

1. Villalobos, P., Sevilla, J., Ho, L., Barrett, D., & Besiroglu, T. (2022). *Will we run out of data? Limits of LLM scaling based on projected dataset size sequences*. arXiv:2211.04325. (Epoch AI.)
2. Grattafiori, A., et al. (2024). *The Llama 3 herd of models*. arXiv:2407.21783. (Meta.)
3. Shumailov, A., et al. (2024). AI models collapse when trained on recursively generated data. *Nature*, 631. doi:10.1038/s41586-024-07566-y.
4. Arendt, H. (1958). *The Human Condition*. University of Chicago Press.
5. Yu, Y. (2026). *Success Provides Direction, Failure Provides Precision: A Structured Audit of Failure Data in LLM Training*. Zenodo. doi:10.5281/zenodo.23355929. (companion audit paper; excluded from evidence-map statistics.)
6. Farrell, S., Gopnik, A., Shalizi, C., & Evans, J. (2025). Large AI models are cultural and social technologies. *Science*, 387. doi:10.1126/science.adt9819.
7. Vallor, S. (2024). *The AI Mirror: How to Reclaim Our Humanity in an Age of Machine Thinking*. Oxford University Press.
8. Brynjolfsson, E. (2022). The Turing trap: Can the economy grow rapidly after the automation of labor? *Dædalus*, 151(2). doi:10.1162/daed_a_01887; arXiv:2201.04200.
9. Gabriel, I. (2020). Artificial intelligence, values, and alignment. *Minds & Machines*, 30, 411–437.
10. Salaudeen, O., Reuel, A., Ahmed, A., Bedi, S., Robertson, Z., Sundar, S., Domingue, B., Wang, A., & Koyejo, S. (2025). *Measurement to meaning: A validity-centered framework for AI evaluation*. arXiv:2505.10573.
11. Legg, S., & Hutter, M. (2007). *Universal intelligence: A definition of machine intelligence*. arXiv:0712.3329.
12. Morris, J. R., et al. (2023). *Levels of AGI: Operationalizing progress on the path to AGI*. arXiv:2311.02462. (Google DeepMind.)
13. Kwa, J., et al. (2025). *Measuring AI ability to complete long tasks*. arXiv:2503.14499. (METR.)
14. Ilić, D., et al. (2024). Evidence of interrelated cognitive-like capabilities in large language models. *Intelligence* (S0160289624000527); arXiv:2310.11616.
15. Gignac, G. E. (2025). Psychometrically derived 60-question benchmarks for large language model evaluation. *Intelligence*, 110 (S016028962500025X).
16. Tesler, L. (1997). *The AI effect* [essay]. nomodes.com.
17. Imeri, B. (2025). *The benefits of AI and the illusion of AGI* [self-archived essay]. ResearchGate. (borderline inclusion; low confidence.)
18. Nguyen, T. (2026). *The role of rigor in artificial intelligence*. arXiv:2607.03634; forthcoming in *Philosophy of Rigor* (Routledge).
19. Plessner, H. (1928). *Die Stufen des Organischen und der Mensch*; English: *Levels of Organic Life and the Human* (trans. M. Hyatt). Fordham University Press, 2019.
20. de Mul, J. (2014). Philosophical anthropology 2.0: Reading Plessner in the age of media. In J. de Mul (Ed.), *Plessner's Philosophical Anthropology*. Amsterdam University Press. doi:10.1515/9789048522989-027.
21. Tamborini, M. (2025). Homo translator: Concretizing the human-in-the-loop in bio-inspired technologies. *Topoi*. doi:10.1007/s11245-025-10208-1.
22. Yiu, E., Kosoy, E., & Gopnik, A. (2024). Transmission versus truth, imitation versus innovation: What children can do that large language and vision-language models cannot (yet). *Perspectives on Psychological Science*; arXiv:2305.07666.
23. Webb, T., Holyoak, K. J., & Lu, H. (2023). Emergent analogical reasoning in large language models. *Nature Human Behaviour*, 7; arXiv:2212.09196.
24. Lehr, S. A., Saichandran, K., Harmon-Jones, E., Vitali, N., & Banaji, M. R. (2025). Kernels of selfhood: GPT-4o shows humanlike patterns of cognitive dissonance moderated by free choice. *PNAS*, 122(35). doi:10.1073/pnas.2501823122.
25. Hu, T., et al. (2025). Generative language models exhibit social identity biases. *Nature Machine Intelligence*, 7 (online 2024-12-12). doi:10.1038/s43588-024-00741-1.
26. Anthropic (2026). *Emotion concepts and their function in a large language model*. Transformer Circuits; arXiv:2604.07729. transformer-circuits.pub/2026/emotions.
27. Hadfield-Menell, L., Russell, S., Abbeel, P., & Dragan, A. (2016). Cooperative inverse reinforcement learning. *NeurIPS 2016*; arXiv:1606.03137.
28. Christiano, P. F., Leike, J., Brown, T., Martic, M., Legg, S., & Amodei, D. (2017). Deep reinforcement learning from human preferences. *NeurIPS 2017*; arXiv:1706.03741.
29. Ouyang, L., et al. (2022). Training language models to follow instructions with human feedback. *NeurIPS 2022*; arXiv:2203.02155.
30. Yuan, S., et al. (2026). *Are human-aligned models models of humans? A Turing-test gap in preference alignment*. arXiv:2609.23640.
31. Hertwig, R., & Erev, I. (2009). The description–experience gap in risky choice: A review. *Trends in Cognitive Sciences*, 13(12), 517–523.
32. Wittgenstein, L. (1953). *Philosophical Investigations* (trans. G. E. M. Anscombe). Blackwell.
33. Coelho Mollo, D., & Millière, P. (2026). The vector grounding problem. *Philosophy and the Mind Sciences*; arXiv:2304.01481.
34. Mallory, F. (2023). Wittgenstein, the other, and large language models. *Filosofisk Supplement*, 2(3), 79–88.
35. Søgaard, A. (2023). Grounding the vector space of an octopus: Word meaning from raw text. *Minds & Machines*, 33(1), 33–54.
36. Jiang, L., Chai, Y., Li, M., Liu, M., Fok, R., Dziri, N., et al. (2025). Artificial hivemind: The open-ended homogeneity of language models (and beyond). *NeurIPS 2025 (Best Paper)*; arXiv:2510.22954.
37. Gharbi, M. (2026). *A model cannot be its own source of truth: Nine escape routes from the data wall, and the verifier wall behind them*. SSRN 7479298 (2026-09-17). (Concurrent work.)
38. Romera-Paredes, B., et al. (2024). Mathematical discoveries from program search with large language models. *Nature*, 625, 468–475.
39. Novikov, A., et al. (2025). *AlphaEvolve: A coding agent for scientific and algorithmic discovery*. arXiv:2506.13131. (Google DeepMind.)
40. Engelbart, D. C. (1962). *Augmenting Human Intellect: A Conceptual Framework*. SRI Summary Report AFOSR-3223.
41. Shneiderman, B. (2022). *Human-Centered AI*. Oxford University Press.
42. Shao, Y., Zope, H., Jiang, Y., Pei, J., Nguyen, D., Brynjolfsson, E., & Yang, D. (2025). *Future of work with AI agents: Auditing automation and augmentation potential across the U.S. workforce*. arXiv:2506.06576.
43. Arntz, M., Gregory, T., & Zierahn, U. (2016). *The risk of automation for jobs in OECD countries: A comparative analysis of PISA and adults survey results*. OECD Social, Employment and Migration Working Papers No. 189. doi:10.1787/5jlz9h56dvq7-en.
44. Sticker, M. (2026). The formula of humanity and AI use. *Philosophy & Technology*, 39(2). doi:10.1007/s13347-026-01100-w.
45. Suleyman, M., with Bhaskar, M. (2023). *The Coming Wave: Technology, Power, and the Twenty-First Century's Greatest Dilemma*. Bodley Head / Penguin.
46. Suleyman, M. (2026). Public statement set on AI as personable tools, never persons (original post; reported by Reuters, 2026-09-16). reuters.com/technology/2026-09-16.
47. Sacasas, L. M. (2023). *Your AI is not a tool* [essay]. The Convivial Society.
48. Sims, P., et al. (2025). *AI agents vs. agentic AI: A conceptual taxonomy*. arXiv:2505.10468.
49. Haupt, A., & Brynjolfsson, E. (2025). Position: AI should not be an imitation game — centaur evaluations. *COLM 2025, PMLR* 267.
50. Shoresh, D., & Loewenstein, Y. (2024). *Modeling the centaur: Human–machine synergy in sequential decision making*. arXiv:2412.18593.
51. DeepSeek-AI (2026). *DeepSeek-V4.1-Flash: Pushing the limits of KV cache compression*. arXiv:2609.19969.
52. Xiaomi LLM-Core Team (2026). *MiMo-V2.6: Scaling reinforcement learning towards self-improvement*. arXiv:2610.11959.
53. Z.ai (2026). *GLM-5: From vibe coding to agentic engineering*. arXiv:2602.15763.
54. DeepSeek-AI (2025). *DeepSeek-R1: Incentivizing reasoning capability in LLMs via reinforcement learning*. arXiv:2501.12948; *Nature* 645, 633–638.
55. Sorensen, T., Newman, B., Moore, J., Park, C., Fisher, J., Mireshghallah, N., Jiang, L., & Choi, Y. (2025). Spectrum tuning: Post-training for distributional coverage and in-context steerability. *ICLR 2026*; arXiv:2510.06084.
56. An, S., Ma, Z., Lin, Z., Zheng, N., Lou, J.-G., & Chen, W. (2023). *Learning from mistakes makes LLM better reasoner* (LEMA). arXiv:2310.20689.
57. Lightman, H., Kosaraju, V., Burda, Y., Edwards, H., Baker, B., Lee, T., Leike, J., Schulman, J., Sutskever, I., & Cobbe, K. (2024). Let's verify step by step. *ICLR 2024*; arXiv:2305.20050. (PRM800K.)
58. SPAR (2026). *SPAR f26: Human-annotated agent failure traces*. sparai.org. (Low-confidence unit.)
59. Song, Y., Yin, D., Yue, X., Huang, J., Li, S., & Lin, B. Y. C. (2024). *Trial and error: Exploration-based trajectory optimization for LLM agents* (ETO). arXiv:2403.02502.
60. Yuan, L., et al. (2024). Advancing LLM reasoning generalists with preference trees (UltraInteract). *ICML 2024*; arXiv:2404.02078.
61. Baek, D., Estornell, A., Zhang, Y., Taufiq, M. F., et al. (2026). D-FUSEr: Diverse failure, unified success via error-distribution shaping in LLM reasoning. *ICML 2026, PMLR* 306.
62. Liu, W., et al. (2026). *Leveraging error diversity in group rollouts for reinforcement learning* (EDAS). arXiv:2605.17333.
63. Xie, S. M., Santurkar, S., Ma, T., & Tsipras, P. (2023). DoReMi: Optimizing data mixtures speeds up language model pretraining. *NeurIPS 2023*; arXiv:2205.10434.
64. Ye, H., et al. (2024). *Data mixing laws: Optimizing data mixtures by scaling law for pretraining*. arXiv:2403.16952.
65. Penedo, G., et al. (2024). *The FineWeb datasets: Decanting the web for the finest text data at scale* (FineWeb / FineWeb-Edu). arXiv:2406.17557.
66. Zhou, K., Constantinides, M., & Quercia, D. (2025). Should LLMs be WEIRD? Exploring WEIRDness and human rights in large language models. *AIES 2025*; arXiv:2508.19269.
67. Fenoglio, E. (2026). *Asymmetric communication: Large language models and language games*. arXiv:2607.28137. (Concurrent work.)
68. Sorensen, T., Moore, J., Fisher, J., Gordon, M., Mireshghallah, N., Rytting, C. M., Ye, A., Jiang, L., Lu, X., Dziri, N., Althoff, T., & Choi, Y. (2024). A roadmap to pluralistic alignment. *ICML 2024*; arXiv:2402.05070.
69. Park, C., Liu, M., Kong, D., Zhang, K., & Ozdaglar, A. (2024). RLHF from heterogeneous feedback via personalization and preference aggregation. *ICML 2024*; arXiv:2405.00254.
70. Baum, K., & Slavkovik, M. (2025). Aggregation problems in machine ethics and AI alignment. *AIES 2025* (AAAI).
71. Huang, S., Siddarth, D., Lovitt, L., et al. (2024). Collective Constitutional AI: Aligning a language model with public input. *ACM FAccT 2024*. doi:10.1145/3630106.3658979; arXiv:2406.07814.
72. Anthropic (2025). *Exploring model welfare*. anthropic.com/research/exploring-model-welfare (2025-04-24).
73. National New Generation AI Governance Expert Committee (2019). *Governance principles for the new generation AI — developing responsible AI*. gov.cn (2019-06-17).
74. State Council of China (2023). *Global AI governance initiative*. gov.cn (2023-10).
75. State Council of China (2025). *Opinion on deeply implementing the "Artificial Intelligence+" action*. gov.cn.
76. Zhuangzi (c. 4th–3rd c. BCE). "Mountain Tree" (山木) chapter, *Zhuangzi*. ("物物而不物于物" — thing things without being turned into a thing by things.)
77. Ge, T., et al. (2024). Scaling synthetic data creation with 1,000,000,000 personas. arXiv:2406.20094. (Tencent AI Lab.)
78. Singh, S., et al. (2024). Aya dataset: An open-access collection for multilingual instruction tuning. arXiv:2402.06619. (Cohere For AI; 65 languages.)
79. Wu, Z., Lou, X., Ma, X., Li, Y., et al. (2026). *Agent-Dice: Disentangling knowledge updates via geometric consensus for agent continual learning*. arXiv:2601.03641.
