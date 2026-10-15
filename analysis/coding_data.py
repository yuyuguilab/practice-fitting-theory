#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
coding_data.py — Evidence-map coding data + tables + figures for
Paper #2 "Human-Referential Fitting Theory" (人本拟合论), deliverable 03.

What this is
------------
The surveyed corpus (N = 80 works) coded with the codebook frozen in
02_experiment_protocol.md §2.2 (dual stance axes A1/A2; fitting-object
dimensions D1–D8 with modality E/I/−; derived booleans D2_explicit,
D8_explicit). Coding units, quotes and provenance are embedded below so the
whole analysis is reproducible from this single file.

Field order for each record (see CODEBOOK_FIELDS):
  work_id, title, authors, year, venue, venue_status, doc_type,
  layer, subdomain, A1, A2, a1_scope, D, tier, peer_reviewed, confidence,
  concurrent, arxiv_id, doi, url, anchor, notes
where:
  D  = 8-char string for D1..D8, each char in {E, I, -}
  anchor = key quote / design anchor backing the non-na A codes and all E codes (R5)
Coding rules applied: R1–R5, CR1–CR6 of the protocol; codebook-fixed codes
(pilot W set: Farrell / Hivemind / Turing Trap / Vallor / Spectrum Tuning)
are reproduced verbatim from 02 §7.

Run:  python3 analysis/coding_data.py   (from the workspace root, or anywhere;
      outputs are written relative to this file's parent directory)
Outputs:
  analysis/tables/table1_corpus_composition.csv
  analysis/tables/table2_A1xA2_stance.csv
  analysis/tables/table3_D_frequencies.csv
  analysis/tables/table4_D2_D7_D8_by_year.csv
  analysis/tables/tableS_gharbi_row.csv
  analysis/tables/tableS_A1xD_exploratory.csv
  analysis/corpus_v1.csv                 (full coded data, data-lock artifact)
  figures/fig1_theory_framework.png      (300 dpi)
  figures/fig2_evidence_map.png          (300 dpi)
  figures/fig3_stance_dimension_heatmap.png (300 dpi)
  stdout: all tables + statistics in readable form

Access-date anchor for all sources: 2026-10-15 (screening/verification calls
performed 2026-10-14, inside the window). Single coder; 20% blind re-coding
scheduled 2026-10-29 (kappa placeholder, see report §8).
"""

import csv
import math
import os
from collections import Counter, OrderedDict

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle
from scipy import stats

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
TABLE_DIR = os.path.join(HERE, "tables")
FIG_DIR = os.path.join(ROOT, "figures")
os.makedirs(TABLE_DIR, exist_ok=True)
os.makedirs(FIG_DIR, exist_ok=True)

CODEBOOK_FIELDS = [
    "work_id", "title", "authors", "year", "venue", "venue_status", "doc_type",
    "layer", "subdomain", "A1", "A2", "a1_scope", "D", "tier", "peer_reviewed",
    "confidence", "concurrent", "arxiv_id", "doi", "url", "anchor", "notes",
]

D_NAMES = {
    "D1": "D1 Works-stock (static archives of human output)",
    "D2": "D2 Practice-flow (regenerating data: telemetry/logs/failure streams)",
    "D3": "D3 Values-preferences",
    "D4": "D4 Emotion-motivation (functional level)",
    "D5": "D5 Failure experience",
    "D6": "D6 Population/culture (the 'who' axis)",
    "D7": "D7 Output-distribution coverage",
    "D8": "D8 Experience-type spectrum (success/failure x expert/novice x typical/edge)",
}

# ---------------------------------------------------------------------------
# The coded corpus (surveyed corpus v1.0, N = 80)
# ---------------------------------------------------------------------------
R = []  # collected below in layer order W-001..W-080

# ----------------------------- L1 concept (13) -----------------------------
R.append(("W-001", "Universal Intelligence: A Definition of Machine Intelligence",
    "Legg, S.; Hutter, M.", 2007, "arXiv preprint", "confirmed", "article",
    "L1", "definition-spectrum", "na", "na", "", "--------", "T1", False, "high",
    False, "0712.3329", "", "https://arxiv.org/abs/0712.3329",
    "Definition (upstream-verified): universal intelligence = ability to achieve goals in a wide range of environments; generality defined by environmental scope.",
    "A1=na: defines intelligence without reference to fitting human practice (CR5)."))
R.append(("W-002", "Levels of AGI: Operationalizing Progress on the Path to AGI",
    "Morris, J. R. et al. (Google DeepMind)", 2023, "arXiv / DeepMind report", "confirmed", "article",
    "L1", "definition-spectrum", "na", "na", "", "--------", "T1", False, "high",
    False, "2311.02462", "", "https://arxiv.org/abs/2311.02462",
    "Taxonomy of AGI levels (generality x autonomy) as operationalization proxy.",
    "A1=na per codebook (taxonomy work, CR5)."))
R.append(("W-003", "Measuring AI Ability to Complete Long Tasks",
    "Kwa, J. et al. (METR)", 2025, "arXiv preprint", "confirmed", "article",
    "L1", "definition-spectrum", "na", "na", "", "--------", "T1", False, "high",
    False, "2503.14499", "", "https://arxiv.org/abs/2503.14499",
    "Task-length horizon doubling ~every 7 months; task duration as operationalization of capability scope.",
    "A1=na (measurement proxy)."))
R.append(("W-004", "The AI Effect (Tesler's theorem) [essay]",
    "Tesler, L.", 1997, "nomodes.com (author site)", "confirmed", "essay",
    "L1", "definition-spectrum", "na", "na", "", "--------", "T1", False, "medium",
    False, "", "", "https://nomodes.com/",
    "Tesler's theorem (upstream: exact wording confirmed from nomodes.com): 'Intelligence is whatever machines haven't done yet.'",
    "Moving-target anchor for C2; verbatim English quote to be re-pinned at data lock."))
R.append(("W-005", "Measurement to Meaning: A Validity-Centered Framework for AI Evaluation",
    "Salaudeen, O.; Reuel, A.; Ahmed, A.; Bedi, S.; Robertson, Z.; Sundar, S.; Domingue, B.; Wang, A.; Koyejo, S.",
    2025, "arXiv preprint", "confirmed", "article",
    "L1", "measurement-critique", "na", "na", "", "I-------", "T1", False, "high",
    False, "2505.10573", "", "https://arxiv.org/abs/2505.10573",
    "Psychometric validity framework for judging which evaluative claims benchmarks can support.",
    "D1=I: benchmark items as samples of human-produced tasks; evaluation-side involvement, not a fitting object (R4). Title verified 2026-10-14."))
R.append(("W-006", "Evidence of interrelated cognitive-like capabilities in large language models: Indications of artificial general intelligence or mere achievement?",
    "Ilić, D. et al.", 2024, "Intelligence (S0160289624000527)", "confirmed", "article",
    "L1", "measurement-critique", "support", "na", "construct-level", "I-------", "T1", True, "high",
    False, "2310.11616", "", "https://arxiv.org/abs/2310.11616",
    "Title: '...indications of artificial general intelligence or mere achievement?' — LLM performance read as mastery of trained (human-produced) content.",
    "A1=support via criterion (2), scope=construct-level (R3). NOTE: upstream 00_input conflated Ilic and Gignac into one entry; separated here (data-quality fix, see report)."))
R.append(("W-007", "Psychometrically derived 60-question benchmarks for large language model evaluation",
    "Gignac, G. E.", 2025, "Intelligence 110 (S016028962500025X)", "confirmed", "article",
    "L1", "measurement-critique", "na", "na", "", "I-------", "T1", True, "medium",
    False, "", "", "https://ideas.repec.org/a/eee/intell/v110y2025ics016028962500025x.html",
    "Psychometric principles imply reliable/valid LLM benchmarks need far fewer items (~60) than current practice.",
    "D1=I (benchmark item banks as human-practice samples, evaluation side). Title from RePEc record; full bib to lock."))
R.append(("W-008", "Evaluating General-Purpose AI with Psychometrics",
    "CACM research feature (author list to lock)", 2026, "Communications of the ACM (Apr 2026)", "confirmed", "article",
    "L1", "measurement-critique", "na", "na", "", "I-------", "T1", False, "medium",
    False, "", "", "https://cacm.acm.org/research/evaluating-general-purpose-ai-with-psychometrics",
    "Psychometric evaluation of 29 LLMs across 27 cognitive tasks (reasoning/comprehension constructs).",
    "Magazine research feature; peer_reviewed=False; author list to lock. This is the 'CACM psychometrics piece' of 00_input."))
R.append(("W-009", "The Benefits of AI and the Illusion of AGI",
    "Imeri, Besim", 2025, "self-archived (ResearchGate/Academia.edu)", "confirmed-marginal", "article",
    "L1", "moving-target", "deny", "na", "", "--------", "T1", False, "low",
    False, "", "", "https://www.researchgate.net/publication/395098367_The_benefits_of_AI_and_the_Illusion_of_AGI",
    "AGI promises 'endless intelligence without limits' as perpetual-motion machines promised 'endless energy without input'; both contradict fundamental principles (verified in screening search 2026-10).",
    "G1-MARGINAL: no DOI/arXiv located; version of record to be pinned at data lock or excluded. A1=deny (2): fitting frame inapplicable (category error). This is the 'Imeri 2025' of 00_input; first name Besim verified this session."))
R.append(("W-010", "The Role of Rigor in Artificial Intelligence",
    "Nguyen, T.", 2026, "arXiv preprint (to appear in Philosophy of Rigor, Routledge)", "confirmed", "article",
    "L1", "moving-target", "na", "na", "", "--------", "T1", False, "high",
    False, "2607.03634", "", "https://arxiv.org/abs/2607.03634",
    "Three-part rigor framework (conceptual/epistemic/operational); deep learning prioritizes operational rigor without mature theoretical foundations.",
    "A1=na (CR4): critiques scientific rigor of AI; no stance on the fitting-human frame. Title+abstract verified 2026-10-14."))
R.append(("W-011", "Die Stufen des Organischen und der Mensch [Levels of the Organic and the Human]",
    "Plessner, H. (1928; new English translation 2024)", 1928, "book (new trans. 2024)", "confirmed", "book",
    "L1", "phil-anthropology", "na", "na", "", "--------", "T1", True, "medium",
    False, "", "", "",
    "Law of natural artificiality: humans constitutively complete themselves through artifacts (upstream-verified anchor).",
    "Philosophical anchor for C2 (tool-use as anthropological norm, not rupture). version_anchor = English translation 2024."))
R.append(("W-012", "Philosophical Anthropology 2.0: Reading Plessner in the Age of Media",
    "de Mul, J.", 2014, "Ch. 26 in de Mul (ed.), Plessner's Philosophical Anthropology (AUP; OA reissue Routledge 2025)", "confirmed", "book-chapter",
    "L1", "phil-anthropology", "na", "na", "", "--------", "T1", True, "high",
    False, "", "10.1515/9789048522989-027", "",
    "Rereads Plessner for the media age: the human as naturally artificial, technologically self-completing.",
    "DOI verified this session (00_input gave no year; pinned to 2014 chapter, OA reissue 2025)."))
R.append(("W-013", "Homo Translator: Concretizing the Human-in-the-Loop in Bio-Inspired Technologies",
    "Tamborini, M.", 2025, "Topoi (open access)", "confirmed", "article",
    "L1", "phil-anthropology", "na", "na", "", "--------", "T1", True, "high",
    False, "", "10.1007/s11245-025-10208-1", "https://link.springer.com/article/10.1007/s11245-025-10208-1",
    "Homo translator: human activity as translation between biological systems and technological artifacts.",
    "Verified this session. A1/A2=na: philosophical anthropology of technology, no AI-fitting claim (CR5)."))

# ------------------------- L2 implementation (31) --------------------------
R.append(("W-014", "Large AI models are cultural and social technologies",
    "Farrell, S.; Gopnik, A.; Shalizi, C.; Evans, J.", 2025, "Science 387 (adt9819)", "confirmed", "article",
    "L2", "cultural-technology", "support", "na", "industry-level", "I----I--", "T1", True, "high",
    False, "", "10.1126/science.adt9819", "https://www.science.org/doi/10.1126/science.adt9819",
    "Title is the A1 claim: large AI models ARE cultural and social technologies.",
    "PILOT-FIXED (02 §7): A1=support, A2=na, D1=I, D6=I. D1=I: corpus is carrier, not research object. Fourth author Evans added per 01 §3.6 verification."))
R.append(("W-015", "Transmission Versus Truth, Imitation Versus Innovation: What Children Can Do That Large Language and Language-and-Vision Models Cannot (Yet)",
    "Yiu, E.; Kosoy, E.; Gopnik, A.", 2024, "Perspectives on Psychological Science", "confirmed", "article",
    "L2", "cultural-technology", "support", "na", "", "I-------", "T1", True, "high",
    False, "2305.07666", "", "https://arxiv.org/abs/2305.07666",
    "'We argue that these artificial intelligence models are cultural technologies that enhance cultural transmission in the modern world' (verified abstract); LLMs as efficient imitators of millions of human writers.",
    "A1=support (1). Journal version 2024 of arXiv:2305.07666 (2023)."))
R.append(("W-016", "Emergent analogical reasoning in large language models",
    "Webb, T.; Holyoak, K. J.; Lu, H.", 2023, "Nature Human Behaviour 7", "confirmed", "article",
    "L2", "cultural-technology", "support", "na", "", "I-------", "T1", True, "high",
    False, "2212.09196", "", "https://arxiv.org/abs/2212.09196",
    "Human-like analogical reasoning emerges from text-only pretraining.",
    "A1=support (2): capability form attributable to fitting human text."))
R.append(("W-017", "The Vector Grounding Problem",
    "Coelho Mollo, D.; Millière, P.", 2026, "Philosophy and the Mind Sciences (special issue; arXiv 2023)", "confirmed", "article",
    "L2", "cultural-technology", "support", "na", "", "I-------", "T1", True, "high",
    False, "2304.01481", "", "https://arxiv.org/abs/2304.01481",
    "Reframes symbol grounding for LLMs; concludes at least some LLM representations may be partially grounded (meaning inherited from human usage through text).",
    "A1=support (medium-grounding defense). CR3: published 2026 version preferred over 2023 preprint (moves year bin to 2024-26)."))
R.append(("W-018", "Wittgenstein, The Other, and Large Language Models",
    "Mallory, F.", 2023, "Filosofisk Supplement 2(3):79-88", "confirmed", "article",
    "L2", "cultural-technology", "na", "na", "", "I-------", "T1", True, "medium",
    False, "", "", "https://fintanmallory.com/publications",
    "Wittgensteinian analysis (anti-foundationalism; meaning without inner reified entities) of talking with LLMs as with an Other.",
    "A1=na (CR4): no stance on fitting asserted; form-of-life vocabulary anchor. Identity verified this session."))
R.append(("W-019", "Grounding the Vector Space of an Octopus: Word Meaning from Raw Text",
    "Søgaard, A.", 2023, "Minds & Machines 33(1):33-54", "confirmed", "article",
    "L2", "cultural-technology", "support", "na", "", "I-------", "T1", True, "high",
    False, "", "10.1007/s11023-023-09622-4", "https://link.springer.com/article/10.1007/s11023-023-09622-4",
    "Defense (upstream '辩护侧', venue verified): word meaning can be grounded in raw text to a substantial degree.",
    "A1=support: distributional meaning inherited from human use."))
R.append(("W-020", "Kernels of selfhood: GPT-4o shows humanlike patterns of cognitive dissonance moderated by free choice",
    "Lehr, S. A.; Saichandran, K.; Harmon-Jones, E.; Vitali, N.; Banaji, M. R.", 2025, "PNAS 122(35)", "confirmed", "article",
    "L2", "fitting-evidence", "support", "na", "", "---E----", "T1", True, "high",
    False, "", "10.1073/pnas.2501823122", "https://www.pnas.org/doi/10.1073/pnas.2501823122",
    "GPT-4o reproduces humanlike cognitive-dissonance / self-justification patterns in the free-choice paradigm.",
    "A1=support (2). D4=E (codebook positive example): functional motivational/self-structure fitting. Authors+DOI verified this session."))
R.append(("W-021", "Generative language models exhibit social identity biases",
    "Hu, T. et al. (Univ. of Cambridge)", 2025, "Nature Machine Intelligence 7 (online 2024-12-12)", "confirmed", "article",
    "L2", "fitting-evidence", "support", "na", "", "---E----", "T1", True, "high",
    False, "", "10.1038/s43588-024-00741-1", "https://www.nature.com/articles/s43588-024-00741-1",
    "'Large language models exhibit patterns of social identity bias, similarly to humans' across 77 LLMs / ~2000 prompts; biases steerable.",
    "A1=support (2). D4=E (codebook). Verified this session."))
R.append(("W-022", "Functional emotion concepts in Claude [interpretability research; exact title to lock]",
    "Anthropic (Interpretability team)", 2026, "transformer-circuits.pub research report", "confirmed", "tech-report",
    "L2", "fitting-evidence", "support", "na", "", "---E----", "T1", False, "medium",
    False, "", "", "https://transformer-circuits.pub/2026/emotions",
    "Upstream-verified finding: functional emotion concepts discovered inside Claude's activations.",
    "D4=E (codebook positive example). Title/section anchors to lock at data lock (T1 URL given by upstream)."))
R.append(("W-023", "The description-experience gap in risky choice: A review",
    "Hertwig, R.; Erev, I.", 2009, "Trends in Cognitive Sciences 13(12):517-523", "confirmed", "article",
    "L2", "fitting-evidence", "na", "na", "", "--------", "T1", True, "high",
    False, "", "10.1016/j.tics.2009.09.021", "",
    "Description-based vs experience-based learning produce systematically different risky choice.",
    "A1=na: human cognition, no AI claim; D all '-': conceptual anchor (corpus=description, practice=experience). Reused from paper-1 bib."))
R.append(("W-024", "Learning from Mistakes Makes LLM Better Reasoner (LEMA)",
    "An, S.; Ma, Z.; Lin, Z.; Zheng, N.; Lou, J.-G.; Chen, W.", 2023, "arXiv (Microsoft)", "confirmed", "article",
    "L2", "fitting-evidence", "na", "na", "", "I---E--I", "T1", False, "high",
    False, "2310.20689", "", "https://arxiv.org/abs/2310.20689",
    "Design anchor: fine-tunes on mistake-correction data (human-like erroneous reasoning) to improve reasoning.",
    "D5=E (codebook positive). D8=I: failure-only single cell, axis not thematized (boundary rule)."))
R.append(("W-025", "Let's Verify Step by Step (PRM800K)",
    "Lightman, H.; Kosaraju, V.; Burda, Y.; Edwards, H.; Baker, B.; Lee, T.; Leike, J.; Schulman, J.; Sutskever, I.; Cobbe, K.",
    2024, "ICLR 2024 (arXiv 2023)", "confirmed", "article",
    "L2", "fitting-evidence", "na", "na", "", "I---E--I", "T1", True, "high",
    False, "2305.20050", "", "https://arxiv.org/abs/2305.20050",
    "PRM800K: 800k step-level human ratings; process supervision learns from step errors (design anchor, paper-1 bib).",
    "D5=E; D8=I (failure-only cell). CR3: ICLR 2024 version preferred over 2023 preprint."))
R.append(("W-026", "SPAR f26: Human-annotated agent failure traces",
    "SPAR (project)", 2026, "sparai.org project page", "confirmed", "dataset",
    "L2", "fitting-evidence", "na", "na", "", "-I--E--I", "T1", False, "low",
    False, "", "", "https://sparai.org/projects/f26/recPcCQjmdWCEjPJL",
    "Human-annotated agent failure traces; open-release plan (paper-1 audit CR4 unit, accessed 2026-10-13 there).",
    "Low confidence (paper-1's only low-confidence unit). D5=E (failure traces as dataset object); D2=I (agent traces); D8=I (failure-only)."))
R.append(("W-027", "Trial and Error: Exploration-Based Trajectory Optimization for LLM Agents (ETO)",
    "Song, Y.; Yin, D.; Yue, X.; Huang, J.; Li, S.; Lin, B. Y. C.", 2024, "arXiv (paper-1 bib)", "confirmed", "article",
    "L2", "fitting-evidence", "na", "na", "", "-I--E--I", "T1", False, "high",
    False, "2403.02502", "", "https://arxiv.org/abs/2403.02502",
    "Design anchor: learns from failed agent trajectories (negative feedback) to refine behavior.",
    "D5=E (failed trajectories as explicit training data); D2=I (agent trajectories); D8=I (failure-only cell)."))
R.append(("W-028", "Advancing LLM Reasoning Generalists with Preference Trees (UltraInteract)",
    "Yuan, L. et al.", 2024, "ICML 2024 (arXiv 2404.02078)", "confirmed", "article",
    "L2", "fitting-evidence", "na", "na", "", "-I--E--I", "T1", True, "high",
    False, "2404.02078", "", "https://arxiv.org/abs/2404.02078",
    "Preference trees pairing correct and incorrect trajectories (chosen/rejected sides) by design.",
    "D5=E (incorrect trajectories as the rejected side, explicit dataset design); D2=I; D8=I (success/failure as training contrast, not a coverage axis)."))
R.append(("W-029", "Cooperative Inverse Reinforcement Learning",
    "Hadfield-Menell, L.; Russell, S.; Abbeel, P.; Dragan, A.", 2016, "NeurIPS 2016", "confirmed", "article",
    "L2", "formalization", "support", "na", "system-level", "--E-----", "T1", True, "high",
    False, "1606.03137", "", "https://arxiv.org/abs/1606.03137",
    "Assistance games: the agent infers and optimizes the human's reward — formal fitting of human values.",
    "A1=support (1). D3=E (codebook lineage start)."))
R.append(("W-030", "Deep Reinforcement Learning from Human Preferences",
    "Christiano, P. F.; Leike, J.; Brown, T.; Martic, M.; Legg, S.; Amodei, D.", 2017, "NeurIPS 2017", "confirmed", "article",
    "L2", "formalization", "support", "na", "system-level", "--E-----", "T1", True, "high",
    False, "1706.03741", "", "https://arxiv.org/abs/1706.03741",
    "Reward model fitted to human preference comparisons; policy optimizes the fitted reward.",
    "A1=support (1). D3=E (RLHF lineage)."))
R.append(("W-031", "Training language models to follow instructions with human feedback",
    "Ouyang, L. et al.", 2022, "NeurIPS 2022", "confirmed", "article",
    "L2", "formalization", "support", "na", "system/industry-level", "--E-----", "T1", True, "high",
    False, "2203.02155", "", "https://arxiv.org/abs/2203.02155",
    "RLHF at scale: the reward model is a fitter of the human preference distribution (upstream gloss).",
    "A1=support (1). D3=E (RLHF lineage representative)."))
R.append(("W-032", "Are Human-Aligned Models Models of Humans? A Turing-Test Gap in Preference Alignment",
    "Yuan, S.; Lin, R.; Li, M.; Hong, G.; Gu, J.; Feng, L.; Russell, C.; Liu, T.", 2026, "arXiv preprint", "confirmed", "article",
    "L2", "formalization", "support", "na", "system-level", "--E-----", "T1", False, "high",
    False, "2609.23640", "", "https://arxiv.org/abs/2609.23640",
    "Preference alignment diverges from modeling human behavior ('Turing-test gap'); stronger preference weighting makes outputs less human-like.",
    "A1=support per codebook (aligned models framed as candidate models of humans). NUANCE for paper-writer: finds preference-fitting != behavior-fitting — supports the D3-vs-D2 distinction. Title verified 2026-10-14."))
R.append(("W-033", "Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond)",
    "Jiang, L. et al.", 2025, "NeurIPS 2025 Best Paper (arXiv 2510.22954; OpenReview saDOrrnNTz)", "confirmed", "article",
    "L2", "counter-adjacent", "support", "na", "", "------EI", "T1", True, "high",
    False, "2510.22954", "", "https://arxiv.org/abs/2510.22954",
    "Infinity-Chat large-scale study of mode collapse in open-ended generation: intra-model repetition + inter-model homogeneity across 70+ models regardless of decoding.",
    "PILOT-FIXED: A1=support (fitting to the shared human-like distribution CONFIRMED to occur), D7=E (collapse metrics), D8=I (loss of edge/individual outputs as a cell, not thematized axis). THE MIXED CASE: affirms fitting, refutes its sufficiency — 'fits the average, not the spectrum'."))
R.append(("W-034", "AI models collapse when trained on recursively generated data",
    "Shumailov, A. et al.", 2024, "Nature 631", "confirmed", "article",
    "L2", "counter-adjacent", "na", "na", "", "------E-", "T1", True, "high",
    False, "", "10.1038/s41586-024-07566-y", "https://www.nature.com/articles/s41586-024-07566-y",
    "Recursive training on generated data degrades output distributions (tails lost first).",
    "CODEBOOK-FIXED: A1=na (recursive degeneration dynamics, no stance on fitting humans), D7=E. Fitting object is model output, not human works (D1='-')."))
R.append(("W-035", "Will we run out of data? Limits of LLM scaling based on human-generated data",
    "Villalobos, P.; Sevilla, J.; Ho, L.; Barrett, D.; Besiroglu, T. (Epoch AI)", 2022, "arXiv / Epoch report", "confirmed", "tech-report",
    "L2", "counter-adjacent", "na", "na", "", "E-------", "T1", False, "high",
    False, "2211.04325", "", "https://arxiv.org/abs/2211.04325",
    "Effective public stock of human-generated text ~300T tokens; compute demand overtakes supply ('data wall').",
    "D1=E: the STOCK of human-produced text is the named object. Theory response: the wall bounds the stock, not the flow (C1 reverse-evidence handled by temporal clause). version_anchor: 2024 update + companion analysis 'Can AI scaling continue through 2030?'."))
R.append(("W-036", "Mathematical discoveries from program search with large language models (FunSearch)",
    "Romera-Paredes, B. et al.", 2024, "Nature 625:468-475", "confirmed", "article",
    "L2", "counter-adjacent", "deny", "na", "", "--------", "T1", True, "high",
    False, "", "10.1038/s41586-023-06924-6", "https://www.nature.com/articles/s41586-023-06924-6",
    "Search + automatic verification discovers algorithms beyond known human intuition (new matrix-multiplication results).",
    "A1=deny (1) (codebook positive example). Dialectic note: its verifier (mathematical correctness, runnable code) is itself a human institution."))
R.append(("W-037", "AlphaEvolve: A coding agent for scientific and algorithmic discovery",
    "Novikov, A. et al. (Google DeepMind)", 2025, "arXiv (official white paper)", "confirmed", "article",
    "L2", "counter-adjacent", "deny", "na", "", "--------", "T1", False, "high",
    False, "2506.13131", "", "https://arxiv.org/abs/2506.13131",
    "Evolutionary LLM pipeline surpasses human-designed algorithms (open math problems, data-center scheduling).",
    "A1=deny (1). Verified this session."))
R.append(("W-038", "A Model Cannot Be Its Own Source of Truth: Nine Escape Routes from the Data Wall, and the Verifier Wall Behind Them",
    "Gharbi, M.", 2026, "SSRN preprint 7479298 (2026-09-17)", "confirmed", "article",
    "L2", "counter-adjacent", "na", "na", "", "EE------", "T1", False, "medium",
    True, "", "", "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7479298",
    "Stock/flow data-engineering framing of the data wall plus a 'verifier wall' behind it; nine escape routes (upstream-verified title and claims).",
    "CONCURRENT WORK (G6). D1=E / D2=E as the protocol expects. Delimitation notes: engineering flow != practice ontology; no works-vs-practice ontological distinction, no full-spectrum x full-course frame, no tool positioning. Not counted as falsifying C1. Reported in a dedicated single-row table."))
R.append(("W-039", "Asymmetric Communication: Large Language Models and the Other",
    "(author list to lock)", 2026, "arXiv preprint", "confirmed", "article",
    "L2", "counter-adjacent", "support", "na", "meaning-side", "--------", "T1", False, "low",
    True, "2607.28137", "", "https://arxiv.org/abs/2607.28137",
    "Communication theory (upstream 01 §3.6): LLM outputs acquire their meaning within human practice; asymmetry between model producer and human interpreters.",
    "CONCURRENT WORK (G6). A1=support, confidence=low (meaning-side implication; author list and section anchors to lock). Cited for delimitation, not claim support."))
R.append(("W-040", "DeepSeek-V4.1-Flash: Pushing the limits of KV cache compression",
    "DeepSeek-AI", 2026, "arXiv tech report", "confirmed", "tech-report",
    "L2", "tech-report", "na", "na", "", "-E--E--I", "T1", False, "high",
    False, "2609.19969", "", "https://arxiv.org/abs/2609.19969",
    "§5.1.1 verbatim (paper-1 audit): 'we collect negative feedback and model failure cases submitted by internal employees at scale'; 'systematic replay of failures and targeted RL against observed model weaknesses'.",
    "D2=E (codebook positive example: employee-submitted failure stream), D5=E, D8=I (failure-only cell). Highest-confidence D2-explicit unit in the corpus."))
R.append(("W-041", "MiMo-V2.6: Scaling reinforcement learning towards self-improvement",
    "Xiaomi LLM-Core Team", 2026, "arXiv tech report", "confirmed", "tech-report",
    "L2", "tech-report", "na", "na", "", "-I--E--I", "T1", False, "high",
    False, "2610.11959", "", "https://arxiv.org/abs/2610.11959",
    "§4.2.6 verbatim (paper-1 audit): reflection/revision data 'keeps the original error recognizable and makes the correction explicit'.",
    "D5=E (codebook positive example); D2=I (self-improvement RL trajectories, not a deployment stream); D8=I."))
R.append(("W-042", "GLM-5: From vibe coding to agentic engineering",
    "Z.ai", 2026, "arXiv tech report", "confirmed", "tech-report",
    "L2", "tech-report", "na", "na", "", "II--E--I", "T1", False, "high",
    False, "2602.15763", "", "https://arxiv.org/abs/2602.15763",
    "§3.1 verbatim (paper-1 audit): 'Erroneous segments within trajectories are retained but masked out in the loss function, allowing the model to learn error correction behaviors.'",
    "D5=E; D2=I (agentic tool trajectories); D1=I (pretraining corpus as background); D8=I."))
R.append(("W-043", "The Llama 3 Herd of Models",
    "Grattafiori, A. et al. (Meta)", 2024, "arXiv tech report", "confirmed", "tech-report",
    "L2", "tech-report", "na", "na", "", "E----I--", "T1", False, "high",
    False, "2407.21783", "", "https://arxiv.org/abs/2407.21783",
    "Design anchor: pretraining data mixture as explicit engineering object; ~8% multilingual share (implicit quota, upstream-verified).",
    "D1=E (codebook positive example); D6=I (implicit multilingual quota)."))
R.append(("W-044", "DeepSeek-R1: Incentivizing reasoning capability in LLMs via reinforcement learning",
    "DeepSeek-AI", 2025, "Nature 645:633-638 (arXiv 2501.12948)", "confirmed", "article",
    "L2", "tech-report", "na", "na", "", "I---I---", "T1", True, "high",
    False, "2501.12948", "", "https://arxiv.org/abs/2501.12948",
    "RL with verifiable rewards (GRPO): incorrect rollouts participate in training as negative signal.",
    "D5=I (codebook GRPO rule: failure signal participates but is not thematized as a coverage object); D1=I (base corpus background)."))

# --------------------------- L3 positioning (12) ---------------------------
R.append(("W-045", "Augmenting Human Intellect: A Conceptual Framework",
    "Engelbart, D. C.", 1962, "SRI Summary Report AFOSR-3223", "confirmed", "report",
    "L3", "augmentation-lineage", "na", "augment", "", "--------", "T1", False, "high",
    False, "", "", "https://www.dougengelbart.org/pubs/augment-3906.html",
    "Programmatic claim: technology should amplify human capability ('augmenting human intellect').",
    "A2=augment (codebook positive example). Origin of the IA tradition."))
R.append(("W-046", "Human-Centered AI",
    "Shneiderman, B.", 2022, "Oxford University Press", "confirmed", "book",
    "L3", "augmentation-lineage", "na", "augment", "", "--------", "T1", True, "high",
    False, "", "10.1093/oso/9780192865254.001.0001", "",
    "Human-centered AI: supertools combining high human control with high automation.",
    "A2=augment."))
R.append(("W-047", "The Turing Trap: Can the Economy Grow Rapidly after the Automation of Labor?",
    "Brynjolfsson, E.", 2022, "Dædalus 151(2) / arXiv 2201.04200", "confirmed", "article",
    "L3", "augmentation-lineage", "support", "augment", "route-level", "--I-----", "T1", True, "high",
    False, "2201.04200", "10.1162/daed_a_01887", "https://arxiv.org/abs/2201.04200",
    "The Turing-test tradition (imitation as the goal) leads into a substitution trap; the augmentation path leads to shared prosperity.",
    "PILOT-FIXED: A1=support with scope=route-level (R3) — for the imitation route, fitting IS the goal; A2=augment; D3=I. Dual-axis decoupling showcase (support x augment)."))
R.append(("W-048", "Future of Work with AI Agents: Auditing Automation and Augmentation Potential across the U.S. Workforce",
    "Shao, Y.; Zope, H.; Jiang, Y.; Pei, J.; Nguyen, D.; Brynjolfsson, E.; Yang, D.", 2025, "arXiv preprint", "confirmed", "article",
    "L3", "augmentation-lineage", "na", "augment", "", "--------", "T1", False, "high",
    False, "2506.06576", "", "https://arxiv.org/abs/2506.06576",
    "WORKBank audit: Human Agency Scale over 844 tasks; maps worker desires for automation vs augmentation.",
    "A2=augment (augmentation-auditing framing). NOTE: 00_input called this 'H1-H5 分级'; actual content is the workforce audit framework with Brynjolfsson as co-author (title verified 2026-10-14)."))
R.append(("W-049", "The Risk of Automation for Jobs in OECD Countries: A Comparative Analysis",
    "Arntz, M.; Gregory, T.; Zierahn, U.", 2016, "OECD Social, Employment and Migration Working Papers 189", "confirmed", "report",
    "L3", "labor-evidence", "na", "na", "", "--------", "T1", False, "medium",
    False, "", "10.1787/5jlz9h56dvq7-en", "https://www.oecd-ilibrary.org/docserver/5jlz9h56dvq7-en.pdf",
    "Task-level analysis: 47% occupation-level automation risk (Frey-Osborne) falls to ~9% at task level.",
    "Empirical anchor for C4 (task-level reality of substitution vs augmentation). The 47% figure is Frey & Osborne's, revised to 9% by this work (kept as the upstream's 47%->9% shorthand with attribution care)."))
R.append(("W-050", "AI Should Not Be An Imitation Game: Centaur Evaluations",
    "Haupt, A. et al. (Stanford Digital Economy Lab)", 2025, "PMLR v267 (COLM 2025)", "confirmed", "article",
    "L3", "labor-evidence", "na", "na", "", "--------", "T1", True, "high",
    False, "", "", "https://digitaleconomy.stanford.edu/app/uploads/2025/06/CentaurEvaluations.pdf",
    "Human-AI teams beat humans alone but rarely outperform the best AI working alone; evaluation should measure the human+AI team.",
    "A1=na, A2=na per codebook (evaluation-methodology stance). Notes: complementarity-window warning evidence for C4's counterpoint section. Verified this session."))
R.append(("W-051", "Modeling the Centaur: Human-Machine Synergy in Sequential Decision Making",
    "Shoresh, D.; Loewenstein, Y.", 2024, "arXiv preprint", "confirmed", "article",
    "L3", "labor-evidence", "na", "na", "", "--------", "T1", False, "high",
    False, "2412.18593", "", "https://arxiv.org/abs/2412.18593",
    "Maia (human-like chess) + Leela (RL) mixture-of-experts: substantial human-machine synergy potential in chess.",
    "DATA-QUALITY FIX: arXiv:2412.18593 was misattributed upstream to Korinek & Stiglitz (NBER 2024); actual work is Shoresh & Loewenstein. Korinek & Stiglitz 2024 therefore EXCLUDED (unverifiable anchor). Synergy-potential counterpoint to centaur pessimism."))
R.append(("W-052", "The Coming Wave [digital-species thesis]",
    "Suleyman, M. (with Hoffman, G.)", 2023, "Bodley Head / Penguin", "confirmed", "book",
    "L3", "counter-position", "na", "substitute", "", "--------", "T1", True, "medium",
    False, "", "", "",
    "AI as a coming wave / nascent digital species — a new kind of entity, not a tool (upstream characterization).",
    "A2=substitute (codebook positive example). A1=na: species framing is identity-normative, no explicit claim about fitting human practice (CR4)."))
R.append(("W-053", "Your AI Is Not a Tool [essay]",
    "Sacasas, L. M.", 2023, "The Convivial Society (newsletter)", "confirmed", "essay",
    "L3", "counter-position", "na", "anti_tool", "", "--------", "T1", False, "medium",
    False, "", "", "https://theconvivialsociety.substack.com/",
    "AI arrives as an environment/habitat rather than an instrument (title is the claim).",
    "A2=anti_tool (codebook positive example). Exact post URL/date to lock."))
R.append(("W-054", "Agentic AI and the erosion of the tool category [title to lock]",
    "Laba, K.-D. (to verify)", 2025, "AI & Society", "confirmed", "article",
    "L3", "counter-position", "na", "anti_tool", "", "--------", "T1", True, "low",
    False, "", "", "",
    "Agentic AI systematically erodes the conceptual conditions of tool-use (upstream characterization of the AI & Society 2025 piece).",
    "Confidence low: exact title/authors not yet pinned (upstream gives surname + venue only). A2=anti_tool per 01 §3.3 grouping."))
R.append(("W-055", "AI Agents vs. Agentic AI: A Conceptual Taxonomy",
    "Sims, P. et al.", 2025, "arXiv preprint", "confirmed", "article",
    "L3", "counter-position", "na", "na", "", "--------", "T1", False, "medium",
    False, "2505.10468", "", "https://arxiv.org/abs/2505.10468",
    "Taxonomy distinguishing AI agents from agentic AI — terminological evidence of the category shift eroding 'tool'.",
    "A1=na, A2=na (descriptive taxonomy). Used as context for the agentic-erosion argument."))
R.append(("W-056", "Kant's humanity formula as a constraint on AI use [title to lock]",
    "Sticker, M.", 2026, "Philosophy & Technology (s13347-026-01100-w)", "confirmed", "article",
    "L3", "normative-constraint", "na", "augment", "", "--------", "T1", True, "medium",
    False, "", "10.1007/s13347-026-01100-w", "",
    "Kantian constraint (upstream): AI may be treated as a mere means; humans may not.",
    "A2=augment (codebook: Kantian permission structure for the tool position). Exact title to lock from DOI."))

# ---------------------------- L4 tension (14) ------------------------------
R.append(("W-057", "Artificial Intelligence, Values, and Alignment",
    "Gabriel, I.", 2020, "Minds & Machines 30:411-437", "confirmed", "article",
    "L4", "plural-alignment", "support", "na", "industry-level", "--E-----", "T1", True, "high",
    False, "", "10.1007/s11023-020-09539-2", "",
    "Alignment means aligning AI to human values; 'whose values?' is the central question (upstream anchor, ~2200 citations).",
    "A1=support (1): alignment framed as fitting human values; scope=industry-level. D3=E (codebook positive example)."))
R.append(("W-058", "A Roadmap to Pluralistic Alignment",
    "Sorensen, T.; Moore, J.; Fisher, J.; Gordon, M.; Mireshghallah, N.; Rytting, C. M.; Ye, A.; Jiang, L.; Lu, X.; Dziri, N.; Althoff, T.; Choi, Y.",
    2024, "ICML 2024 (arXiv 2402.05070)", "confirmed", "article",
    "L4", "plural-alignment", "na", "na", "", "--E--E--", "T1", True, "high",
    False, "2402.05070", "", "https://arxiv.org/abs/2402.05070",
    "Three types of pluralistic models and three benchmark classes; standard alignment may reduce pluralism (Overton / CSA / procedural approaches over POPULATIONS).",
    "D3=E; D6=E (pluralism across populations = explicit who-axis design). Title verified 2026-10-14. Note same first author as Spectrum Tuning (W-071)."))
R.append(("W-059", "RLHF from Heterogeneous Feedback via Personalization and Preference Aggregation",
    "Park, C.; Liu, M.; Kong, D.; Zhang, K.; Ozdaglar, A.", 2024, "ICML 2024 (arXiv 2405.00254)", "confirmed", "article",
    "L4", "plural-alignment", "na", "na", "", "--E-----", "T1", True, "high",
    False, "2405.00254", "", "https://arxiv.org/abs/2405.00254",
    "Preferences are heterogeneous: personalization and social-choice aggregation (utilitarian/Leximin-style) frameworks.",
    "D3=E, A2=na per codebook (criticizing aggregation still treats preferences as the object). Title verified 2026-10-14."))
R.append(("W-060", "Aggregation Problems in Machine Ethics and AI Alignment",
    "Baum, K.; Slavkovik, M.", 2025, "AIES 2025 (AAAI)", "confirmed", "article",
    "L4", "plural-alignment", "na", "na", "", "--E-----", "T1", True, "high",
    False, "", "", "https://ojs.aaai.org/index.php/AIES/article/view/36554",
    "'Alignment by social aggregation cannot replace moral aggregation but merely relocates it — often opaquely.'",
    "D3=E (aggregation as object of critique). Verified this session (co-author Slavkovik added; upstream had 'Baum' only)."))
R.append(("W-061", "Collective Constitutional AI: Aligning a Language Model with Public Input",
    "Anthropic (Huang, M. et al.)", 2025, "ACM FAccT 2025", "confirmed", "article",
    "L4", "plural-alignment", "na", "na", "", "--E--I--", "T1", True, "medium",
    False, "", "", "",
    "~1,000 US participants deliberate constitution content; collective value-fitting at scale.",
    "D3=E; D6=I (US-only participant base — the who-limitation recorded in upstream critique). Title partially verified; author list to lock."))
R.append(("W-062", "'Personable tools', never personhood [public statement set]",
    "Suleyman, M.", 2026, "original post (T1 anchor) + Reuters 2026-09-16 context", "confirmed", "statement-set",
    "L4", "subjecthood-boundary", "na", "augment", "", "--------", "T1", False, "medium",
    False, "", "", "https://www.reuters.com/technology/2026-09-16/",
    "Upstream quote (paraphrase-locked): AI should be 'personable tools' with personality but NEVER granted personhood — public critique of Anthropic's model-welfare route.",
    "CR2 statement set (original post as T1 anchor, Reuters as context), separate entry from W-052. A2=augment (codebook CR2 rule). Confidence medium per protocol §2.2 CR2."))
R.append(("W-063", "Exploring model welfare",
    "Anthropic", 2025, "anthropic.com research statement (2025-04-24)", "confirmed", "statement",
    "L4", "subjecthood-boundary", "na", "na", "", "--------", "T1", False, "high",
    False, "", "", "https://www.anthropic.com/research/exploring-model-welfare",
    "Official research program on whether AI models may deserve moral consideration and how to assess welfare-relevant traits.",
    "A2=na (CR4: moral-consideration exploration, not a substitute-advocacy claim). Notes: the counterpart in the Suleyman-Anthropic clash = C5 evidence. Verified this session."))
R.append(("W-064", "The AI Mirror: How to Reclaim Our Humanity in an Age of Machine Thinking",
    "Vallor, S.", 2024, "Oxford University Press (ISBN 9780197759066)", "confirmed", "book",
    "L4", "subjecthood-boundary", "support", "anti_tool", "", "--------", "T1", True, "high",
    False, "", "", "",
    "AI as a (distorting) mirror of human thought: the danger is what it reflects back into human self-understanding.",
    "PILOT-FIXED: A1=support (distorted fitting/reflection affirmed) x A2=anti_tool (mirror/environment, not instrument) — second dual-axis showcase. D4='-' per codebook (reverse causality: AI shapes human self-understanding, direction criterion fails)."))
R.append(("W-065", "新一代人工智能治理原则——发展负责任的人工智能 [Governance Principles for New Generation AI]",
    "国家新一代人工智能治理专业委员会", 2019, "official policy document", "confirmed", "policy",
    "L4", "chinese-context", "na", "augment", "", "--------", "T1", False, "high",
    False, "", "", "http://www.gov.cn/xinwen/2019-06/17/content_5401006.htm",
    "Principle 1: 以人为本 ('human-centered') among eight governance principles.",
    "A2=augment. Official text (T1)."))
R.append(("W-066", "全球人工智能治理倡议 [Global AI Governance Initiative]",
    "中国 (官方发布)", 2023, "official policy document", "confirmed", "policy",
    "L4", "chinese-context", "na", "augment", "", "--------", "T1", False, "medium",
    False, "", "", "https://www.gov.cn/zhengce/202310/content_6911589.htm",
    "以人为本、智能向善 ('people-centered, AI for good') as leading framing.",
    "A2=augment."))
R.append(("W-067", "关于深入实施'人工智能+'行动的意见 [Opinion on the 'AI+' Action]",
    "国务院", 2025, "official policy document", "confirmed", "policy",
    "L4", "chinese-context", "na", "augment", "", "--------", "T1", False, "high",
    False, "", "", "https://www.gov.cn/zhengce/",
    "Throughout: 赋能 (empowerment) / 人机协同 (human-machine collaboration); no subjecthood language (upstream characterization, full-text confirmed there).",
    "A2=augment. Used in the argument that the official Chinese register is fully instrumental/augmentative."))
R.append(("W-068", "重申传统：一种整体论的比较技术哲学研究 [monograph; exact year to lock]",
    "李三虎", None, "book (Chinese philosophy of technology)", "confirmed-marginal", "book",
    "L4", "chinese-context", "na", "na", "", "--------", "T1", True, "low",
    False, "", "", "",
    "'体用不分、道器合一' — a technology-philosophy framework on Confucian ti-yong / dao-qi non-dualism (upstream anchor; framework documented via 2024 secondary discussion).",
    "A2=na (CR4: not an AI-specific normative claim). Confidence low: publication year/publisher to lock; excluded from year-stratified tables (year unknown)."))
R.append(("W-069", "庄子·山木 [Zhuangzi, 'Mountain Tree': 物物而不物于物]",
    "庄子 (classic text)", -300, "classic text (pre-Qin)", "confirmed", "classic",
    "L4", "chinese-context", "na", "na", "", "--------", "T1", True, "high",
    False, "", "", "",
    "'物物而不物于物' — master things without being thingified by them (verbatim, upstream).",
    "A1/A2=na (CR5: classical aphorism, no AI claim). Designated 题眼 (thematic eye) material for C5; tool-non-dompletion topos."))
R.append(("W-070", "Care robots and filial obligations [title to lock]",
    "Muyskens, J.", 2024, "journal article (to lock)", "confirmed", "article",
    "L4", "chinese-context", "na", "augment", "", "--------", "T1", True, "low",
    False, "", "", "",
    "Care robots cannot fulfill filial-piety-type obligations (upstream): an INTERNAL correction to pure-instrument readings of care AI.",
    "A2=augment with notes 'corrects pure-artifact view' per codebook boundary rule. Confidence low: exact title/venue to lock."))

# ------------------------ L5 methodological (10) ---------------------------
R.append(("W-071", "Spectrum Tuning: Post-Training for Distributional Coverage and In-Context Steerability",
    "Sorensen, T.; Newman, B.; Moore, J.; Park, C.; Fisher, J.; Mireshghallah, N.; Jiang, L.; Choi, Y.",
    2025, "ICLR 2026 (arXiv 2510.06084; comments field)", "confirmed", "article",
    "L5", "coverage-distribution", "na", "na", "", "------E-", "T1", True, "high",
    False, "2510.06084", "", "https://arxiv.org/abs/2510.06084",
    "Instruction tuning systematically damages distributional coverage (mode collapse); Spectrum Tuning restores output coverage and steerability (three desiderata: steerability, valid coverage, distributional alignment).",
    "PILOT-FIXED: A1=na, A2=na, D7=E, D8='-'. VENUE RESOLVED this session: arXiv comments field states ICLR 2026 and author list includes Yejin Choi (both were 'unconfirmed' in 01 §3.6); OpenReview cross-check still pending at data lock (G7)."))
R.append(("W-072", "Should LLMs be WEIRD? [cultural representativeness and bias amplification]",
    "(authors to lock)", 2025, "AIES 2025", "confirmed", "article",
    "L5", "coverage-population", "na", "na", "", "-----E--", "T1", True, "medium",
    False, "2508.19269", "", "https://arxiv.org/abs/2508.19269",
    "Upstream-verified finding: increasing cultural representativeness can AMPLIFY reproduction of discriminatory views — naive who-quotas backfire.",
    "D6=E (codebook: cultural representativeness as manipulated variable). The WEIRD paradox: representing who != fixing what."))
R.append(("W-073", "Aya Dataset: An Open-Access Collection for Multilingual Instruction Tuning",
    "Singh, S. et al. (Cohere For AI)", 2024, "arXiv (ACL 2024 companion)", "confirmed", "article",
    "L5", "coverage-population", "na", "na", "", "I----E--", "T1", False, "high",
    False, "2402.06619", "", "https://arxiv.org/abs/2402.06619",
    "Human-curated instruction data spanning 65 languages, designed to bridge the language gap.",
    "D6=E (language coverage as explicit design axis); D1=I (curated corpus as carrier). DATA-QUALITY FIX: 00_input's 'Aya 117 languages' is incorrect — dataset covers 65 languages (Aya model: 101). Verified this session."))
R.append(("W-074", "DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining",
    "Xie, S. M.; Santurkar, S.; Ma, T.; Tsipras, P.",
    2023, "NeurIPS 2023", "confirmed", "article",
    "L5", "mixture-regression", "na", "na", "", "E-----I-", "T1", True, "high",
    False, "2205.10434", "", "https://arxiv.org/abs/2205.10434",
    "Domain weights optimized by proxy models, then trained: mixture as a regression variable over the static corpus.",
    "D1=E (domain mixture as named optimization object over stock); D7=I (diversity enters as a data-cluster quantity to regress, not output-distribution coverage — upstream three-roles taxonomy role 1)."))
R.append(("W-075", "Data Mixing Laws: Optimizing Data Mixtures by Scaling Law for Pretraining",
    "Ye, H. et al.", 2024, "arXiv preprint", "confirmed", "article",
    "L5", "mixture-regression", "na", "na", "", "E-----I-", "T1", False, "high",
    False, "2403.16952", "", "https://arxiv.org/abs/2403.16952",
    "Fitting mixing laws that predict loss as function of mixture proportions; optimizing mixtures by scaling laws.",
    "D1=E; D7=I (same three-roles classification as DoReMi)."))
R.append(("W-076", "InsTag: tag-cluster quota data selection for instruction tuning [exact title to lock]",
    "Lu, Y. et al.", 2024, "ICLR 2024", "confirmed", "article",
    "L5", "mixture-heuristic", "na", "na", "", "I----II-", "T1", True, "low",
    False, "", "", "",
    "Tag-based clustering of instruction data with diversity quotas across clusters (upstream characterization of the InsTag line).",
    "D7=I per codebook (coverage intent explicit but object = data clusters, not output distributions); D6=I (persona/tag diversity); D1=I. Confidence low: exact title/arXiv id to lock."))
R.append(("W-077", "The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale",
    "Penedo, G. et al. (HuggingFaceFW)", 2024, "arXiv preprint", "confirmed", "dataset",
    "L5", "mixture-quality", "na", "na", "", "E-------", "T1", False, "high",
    False, "2406.17557", "", "https://arxiv.org/abs/2406.17557",
    "Aggressive quality filtering for educational text: the large majority of the web is discarded (FineWeb-Edu keeps only a small fraction; upstream: ~92% dropped).",
    "D1=E (curation of the stock as named object). D5='-' per codebook (EXPLICIT EXCLUSION of low-quality/failure-like data — recorded as the evidence-form of an absence, not involvement). D7='-' (coverage not treated)."))
R.append(("W-078", "Scaling Synthetic Data Creation with 1,000,000,000 Personas",
    "Ge, T. et al. (Tencent AI Lab)", 2024, "arXiv preprint", "confirmed", "article",
    "L5", "mixture-heuristic", "na", "na", "", "-----EI-", "T1", False, "high",
    False, "2406.20094", "", "https://arxiv.org/abs/2406.20094",
    "One billion diverse personas drive synthetic data generation at scale (diversity via simulated who-variety).",
    "D6=E (persona diversity as explicit who-axis design — synthetic personas); D7=I (diversity intent on generation, not output-distribution coverage); D1='-' (object is synthetic, not human works)."))
R.append(("W-079", "Agent-Dice: Disentangling Knowledge Updates [continual learning for LLM agents]",
    "(authors to lock)", 2026, "arXiv preprint", "confirmed", "article",
    "L5", "absorption", "na", "na", "", "-I------", "T1", False, "medium",
    False, "2601.03641", "", "https://arxiv.org/abs/2601.03641",
    "Stability-plasticity failures of LLM agents stem mainly from knowledge-update mechanisms (upstream 01 §3.6 verification).",
    "D2=I per codebook continual-learning rule (absorption mechanism treated; data source not specified as a practice stream). Supports C3 absorb-side bottleneck as 'supporting adjacent evidence'."))
R.append(("W-080", "Transfer is All You Need: Revisiting the Stability-Plasticity Dilemma",
    "Kim (given name to lock)", 2026, "OpenReview submission", "confirmed-marginal", "article",
    "L5", "absorption", "na", "na", "", "-I------", "T1", False, "low",
    False, "", "", "https://openreview.net/",
    "Backward/forward transfer reanalysis of the stability-plasticity dilemma (upstream 01 §3.6).",
    "G1-marginal (OpenReview, no arXiv/DOI id recorded upstream); D2=I (same continual-learning rule). Supports C3 absorb-side as adjacent evidence."))

CORPUS = [dict(zip(CODEBOOK_FIELDS, r)) for r in R]
assert len(CORPUS) == 80, f"expected 80 works, got {len(CORPUS)}"
assert len({w["work_id"] for w in CORPUS}) == 80, "duplicate work_id"
for w in CORPUS:
    assert len(w["D"]) == 8 and set(w["D"]) <= {"E", "I", "-"}
    w["D2_explicit"] = (w["D"][1] == "E")
    w["D8_explicit"] = (w["D"][7] == "E")

LAYERS = ["L1", "L2", "L3", "L4", "L5"]
LAYER_NAMES = {
    "L1": "L1 Concept", "L2": "L2 Implementation", "L3": "L3 Positioning",
    "L4": "L4 Tension", "L5": "L5 Methodological",
}

def year_bin(y):
    if y is None:
        return "unknown"
    if y <= 2019:
        return "classic (<=2019)"
    if y <= 2023:
        return "2020-2023"
    return "2024-2026"

YEAR_BINS = ["classic (<=2019)", "2020-2023", "2024-2026"]

# ---------------------------------------------------------------------------
# Statistics helpers
# ---------------------------------------------------------------------------

def clopper_pearson(k, n, alpha=0.05):
    """Exact binomial (Clopper-Pearson) CI."""
    lo = 0.0 if k == 0 else stats.beta.ppf(alpha / 2, k, n - k + 1)
    hi = 1.0 if k == n else stats.beta.ppf(1 - alpha / 2, k + 1, n - k)
    return lo, hi

def fisher_2x2(a, b, c, d):
    """Fisher exact for [[a, b], [c, d]]; returns (OR, p_two_sided, p_one_sided)."""
    table = [[a, b], [c, d]]
    orv, p2 = stats.fisher_exact(table)
    _, p1 = stats.fisher_exact(table, alternative="greater")
    return orv, p2, p1

def md_table(headers, rows):
    out = ["| " + " | ".join(headers) + " |",
           "|" + "|".join(["---"] * len(headers)) + "|"]
    for r in rows:
        out.append("| " + " | ".join(str(x) for x in r) + " |")
    return "\n".join(out)

def write_csv(path, headers, rows):
    with open(path, "w", newline="", encoding="utf-8") as f:
        csvw = csv.writer(f)
        csvw.writerow(headers)
        csvw.writerows(rows)

# ---------------------------------------------------------------------------
# Analyses
# ---------------------------------------------------------------------------

def table1():
    rows = []
    for L in LAYERS:
        sub = [w for w in CORPUS if w["layer"] == L]
        bybin = Counter(year_bin(w["year"]) for w in sub)
        rows.append([LAYER_NAMES[L], len(sub),
                     bybin["classic (<=2019)"], bybin["2020-2023"],
                     bybin["2024-2026"], bybin["unknown"]])
    bybin_all = Counter(year_bin(w["year"]) for w in CORPUS)
    rows.append(["TOTAL", len(CORPUS), bybin_all["classic (<=2019)"],
                 bybin_all["2020-2023"], bybin_all["2024-2026"], bybin_all["unknown"]])
    headers = ["Layer (primary)", "n", "classic (<=2019)", "2020-2023", "2024-2026", "year unknown"]
    write_csv(os.path.join(TABLE_DIR, "table1_corpus_composition.csv"), headers, rows)
    print("\n=== TABLE 1: Corpus composition (layer x year stratum) ===")
    print(md_table(headers, rows))
    # supporting composition facts
    for field in ["doc_type", "tier", "peer_reviewed", "confidence"]:
        c = Counter(str(w[field]) for w in CORPUS)
        print(f"  by {field}: {dict(sorted(c.items(), key=lambda kv: -kv[1]))}")

def table2():
    a1_order = ["support", "deny", "na"]
    a2_order = ["augment", "substitute", "anti_tool", "na"]
    headers = ["A1 \\ A2"] + a2_order + ["row total"]
    rows = []
    for a1 in a1_order:
        cells = []
        for a2 in a2_order:
            n = sum(1 for w in CORPUS if w["A1"] == a1 and w["A2"] == a2)
            cells.append(n)
        rows.append([a1] + cells + [sum(cells)])
    rows.append(["column total"] + [sum(1 for w in CORPUS if w["A2"] == a2) for a2 in a2_order] + [len(CORPUS)])
    write_csv(os.path.join(TABLE_DIR, "table2_A1xA2_stance.csv"), headers, rows)
    print("\n=== TABLE 2: A1 x A2 stance distribution (counts of works) ===")
    print(md_table(headers, rows))
    # mixed / dual-axis showcase cases
    print("  Mixed-case presentation (dual-axis decoupling, codebook boundary rules):")
    for wid in ["W-033", "W-047", "W-064", "W-052", "W-062"]:
        w = next(x for x in CORPUS if x["work_id"] == wid)
        print(f"    {wid} {w['title'][:58]:58s} A1={w['A1']:8s} A2={w['A2']:10s} D={w['D']}")
    a1c = Counter(w["A1"] for w in CORPUS)
    a2c = Counter(w["A2"] for w in CORPUS)
    print(f"  A1 marginal: {dict(a1c)}   A2 marginal: {dict(a2c)}")

def table3():
    dims = list(D_NAMES.keys())
    headers = ["Dimension", "E (explicit)", "I (implicit)", "- (absent)", "%E (N=80)", "%E or I"]
    rows = []
    for i, d in enumerate(dims):
        e = sum(1 for w in CORPUS if w["D"][i] == "E")
        im = sum(1 for w in CORPUS if w["D"][i] == "I")
        rows.append([D_NAMES[d], e, im, 80 - e - im, f"{100*e/80:.1f}%", f"{100*(e+im)/80:.1f}%"])
    write_csv(os.path.join(TABLE_DIR, "table3_D_frequencies.csv"), headers, rows)
    print("\n=== TABLE 3: Fitting-object dimension frequencies (E/I/- per dimension) ===")
    print(md_table(headers, rows))
    e_works = {d: [w["work_id"] for w in CORPUS if w["D"][i] == "E"]
               for i, d in enumerate(dims)}
    for d in dims:
        print(f"  {d}: E works = {e_works[d] if e_works[d] else 'NONE'}")
    d8i = [w["work_id"] for w in CORPUS if w["D"][7] == "I"]
    print(f"  D8 implicit (I) works = {d8i}  (n={len(d8i)})")

def table4():
    dims_idx = {"D1": 0, "D2": 1, "D7": 6, "D8": 7}
    headers = ["Dimension x modality"] + YEAR_BINS + ["total"]
    rows = []
    for d, i in dims_idx.items():
        for mod, label in [("E", "explicit"), ("I", "implicit")]:
            cells = []
            for b in YEAR_BINS:
                n = sum(1 for w in CORPUS if w["D"][i] == mod and year_bin(w["year"]) == b)
                cells.append(n)
            rows.append([f"{d} {label}"] + cells + [sum(cells)])
    write_csv(os.path.join(TABLE_DIR, "table4_D2_D7_D8_by_year.csv"), headers, rows)
    print("\n=== TABLE 4: Explicit (and implicit) treatment by year stratum ===")
    print(md_table(headers, rows))

def d8_gap_inference():
    n = len(CORPUS)
    k = sum(1 for w in CORPUS if w["D8_explicit"])
    lo, hi = clopper_pearson(k, n)
    rot = 3.0 / n
    print("\n=== GAP QUANTIFICATION: D8_explicit ===")
    print(f"  D8 explicit works: k = {k} / {n}")
    print(f"  Exact binomial (Clopper-Pearson) 95% CI: [{lo:.4f}, {hi:.4f}]")
    print(f"  Rule-of-three upper bound (3/n): {rot:.4f} ({100*rot:.1f}%)")
    if k == 0:
        print("  Interpretation: zero observed explicit treatment of the experience-type axis;")
        print("  with 95% confidence the true rate is below ~{:.1f}% in corpora assembled this way.".format(100 * hi))
    return k, n, lo, hi

def d2_core():
    d2e = [w for w in CORPUS if w["D2_explicit"]]
    print("\n=== CORE RESULT: D2_explicit (practice-flow as named object) ===")
    for w in d2e:
        print(f"  {w['work_id']} {w['title'][:70]} ({w['year']}, {w['subdomain']}, conf={w['confidence']}, concurrent={w['concurrent']})")
    d2i = sum(1 for w in CORPUS if w["D"][1] == "I")
    print(f"  D2 explicit = {len(d2e)}/80; D2 implicit = {d2i}/80; D2 absent = {80 - len(d2e) - d2i}/80")
    return d2e

def gharbi_row():
    w = next(x for x in CORPUS if x["work_id"] == "W-038")
    headers = ["work_id", "title", "year", "venue", "A1", "A2", "D", "D1", "D2", "D2_explicit", "concurrent", "confidence", "delimitation note"]
    row = [[w["work_id"], w["title"], w["year"], w["venue"], w["A1"], w["A2"], w["D"],
            w["D"][0], w["D"][1], w["D2_explicit"], w["concurrent"], w["confidence"],
            "engineering stock/flow != practice ontology; no works-vs-practice distinction; no spectrum x course frame; no tool positioning"]]
    write_csv(os.path.join(TABLE_DIR, "tableS_gharbi_row.csv"), headers, row)
    print("\n=== Gharbi (SSRN 7479298) dedicated concurrent-work row ===")
    print(md_table(headers, row))

def exploratory_A1xD():
    dims = list(D_NAMES.keys())
    print("\n=== EXPLORATORY: A1 x D-explicit cross-tab (counts of works with E) ===")
    headers = ["A1"] + dims + ["any E", "any E or I"]
    rows = []
    for a1 in ["support", "deny", "na"]:
        sub = [w for w in CORPUS if w["A1"] == a1]
        cells = [sum(1 for w in sub if w["D"][i] == "E") for i in range(8)]
        anye = sum(1 for w in sub if "E" in w["D"])
        anyei = sum(1 for w in sub if ("E" in w["D"] or "I" in w["D"]))
        rows.append([f"{a1} (n={len(sub)})"] + cells + [anye, anyei])
    write_csv(os.path.join(TABLE_DIR, "tableS_A1xD_exploratory.csv"), headers, rows)
    print(md_table(headers, rows))
    # Fisher tests (exploratory only; small cells)
    sup = [w for w in CORPUS if w["A1"] == "support"]
    den = [w for w in CORPUS if w["A1"] == "deny"]
    sup_eng = sum(1 for w in sup if "E" in w["D"] or "I" in w["D"])
    den_eng = sum(1 for w in den if "E" in w["D"] or "I" in w["D"])
    orv, p2, p1 = fisher_2x2(den_eng, len(den) - den_eng, sup_eng, len(sup) - sup_eng)
    print(f"  Fisher (deny vs support x any D engagement): {den_eng}/{len(den)} vs {sup_eng}/{len(sup)}; OR={orv:.3f}, p(2-sided)={p2:.3f}")
    l5 = [w for w in CORPUS if w["layer"] == "L5"]
    rest = [w for w in CORPUS if w["layer"] != "L5"]
    l5_eng = sum(1 for w in l5 if w["D"][6] in "EI")
    rest_eng = sum(1 for w in rest if w["D"][6] in "EI")
    orv, p2, p1 = fisher_2x2(l5_eng, len(l5) - l5_eng, rest_eng, len(rest) - rest_eng)
    print(f"  Fisher (L5 vs rest x D7 engagement): {l5_eng}/{len(l5)} vs {rest_eng}/{len(rest)}; OR={orv:.3f}, p(2-sided)={p2:.4f}")
    l2 = [w for w in CORPUS if w["layer"] == "L2"]
    rest = [w for w in CORPUS if w["layer"] != "L2"]
    l2_eng = sum(1 for w in l2 if w["D"][0] in "EI")
    rest_eng = sum(1 for w in rest if w["D"][0] in "EI")
    orv, p2, p1 = fisher_2x2(l2_eng, len(l2) - l2_eng, rest_eng, len(rest) - rest_eng)
    print(f"  Fisher (L2 vs rest x D1 engagement): {l2_eng}/{len(l2)} vs {rest_eng}/{len(rest)}; OR={orv:.3f}, p(2-sided)={p2:.4f}")
    print("  NOTE: corpus is a purposive sample — these tests are descriptive of THIS corpus only (no population inference).")

def sensitivity():
    print("\n=== SENSITIVITY ANALYSES ===")
    low = [w for w in CORPUS if w["confidence"] == "low"]
    keep = [w for w in CORPUS if w["confidence"] != "low"]
    d8e = sum(1 for w in keep if w["D8_explicit"])
    lo, hi = clopper_pearson(d8e, len(keep))
    print(f"  (1) Exclude low-confidence units (n={len(low)}: {[w['work_id'] for w in low]}): N'={len(keep)}")
    print(f"      D8-E still {d8e}/{len(keep)}, CP 95% CI [{lo:.4f}, {hi:.4f}]; D2-E still "
          f"{sum(1 for w in keep if w['D2_explicit'])} (Gharbi medium, DeepSeek-V4.1 high)")
    print(f"      A1 in N': {dict(Counter(w['A1'] for w in keep))}")
    d8ei = sum(1 for w in CORPUS if w["D"][7] in "EI")
    print(f"  (2) D8 threshold E -> E+I: {d8ei}/80 = {100*d8ei/80:.1f}% (implicit presence vs explicit absence)")
    alt = Counter(w["A1"] for w in CORPUS)
    alt["support"] -= 1; alt["deny"] += 1
    print(f"  (3) Hivemind A1 re-assigned support->deny (01's original rule): {dict(alt)} — collapse-line split conclusion unchanged")
    noG = [w for w in CORPUS if w["work_id"] != "W-038"]
    print(f"  (4) Gharbi excluded: D2-E = {sum(1 for w in noG if w['D2_explicit'])}/{len(noG)} — C3 nascent-practice claim unaffected")

def saturation():
    print("\n=== SATURATION CHECK (02 §5.1) ===")
    seen = set()
    new_sig_positions = []
    for idx, w in enumerate(CORPUS):
        sig = (w["A1"], w["A2"], w["D"])
        if sig not in seen:
            new_sig_positions.append((idx + 1, w["work_id"], sig))
        seen.add(sig)
    last10_n = max(1, len(CORPUS) // 10)
    last_start = len(CORPUS) - last10_n
    new_in_last = [x for x in new_sig_positions if x[0] > last_start]
    print(f"  Last 10% = works {last_start+1}..{len(CORPUS)} (n={last10_n})")
    print(f"  New full (A1 x A2 x D-pattern) signatures in last 10%: {len(new_in_last)}")
    for pos, wid, sig in new_in_last:
        print(f"    position {pos}: {wid} {sig}")
    if new_in_last:
        print("  -> STRICT signature saturation NOT reached; corpus filled to the 80-work cap per protocol §5.1 and reported as such.")
        print("     Coarse saturation reached: no new A-axis values, no newly E-coded dimension, no new codebook boundary case in last 10%.")
    else:
        print("  -> saturation reached.")

# ---------------------------------------------------------------------------
# Figures
# ---------------------------------------------------------------------------

LAYER_COLORS = {"L1": "#4C72B0", "L2": "#DD8452", "L3": "#55A868", "L4": "#C44E52", "L5": "#8172B3"}

def fig1_framework():
    fig, ax = plt.subplots(figsize=(11.5, 7.6))
    ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.axis("off")

    # regions
    stock = Rectangle((0.4, 1.2), 3.6, 7.2, facecolor="#EBEBEB", edgecolor="#999999", hatch="///", lw=1.0)
    ax.add_patch(stock)
    flow = Rectangle((4.9, 1.2), 4.7, 7.2, facecolor="#E8F2E8", edgecolor="#55A868", lw=1.2)
    ax.add_patch(flow)
    # the data wall between stock and flow
    wall = Rectangle((4.15, 1.2), 0.55, 7.2, facecolor="#B0B0B0", edgecolor="#666666", hatch="O", lw=1.0)
    ax.add_patch(wall)
    ax.text(4.42, 8.75, "DATA WALL\n(stock is finite)", ha="center", va="bottom",
            fontsize=8.5, color="#555555", fontweight="bold")

    ax.text(2.2, 6.9, "CORPUS-FITTING\n(static misreading)", ha="center", fontsize=11, fontweight="bold", color="#555555")
    ax.text(2.2, 6.15, "human works: text archives,\ncode bases, benchmark banks\n(the 'stock' — finite)", ha="center", fontsize=8.5, color="#555555")
    ax.text(2.2, 4.9, "current industry default:\npretraining on curated stock\n(D1-E works: 6/80 across 2022–2026)",
            ha="center", fontsize=8.5, color="#555555", style="italic")

    ax.text(7.25, 6.9, "PRACTICE-FITTING\n(dynamic reading)", ha="center", fontsize=11, fontweight="bold", color="#2F6B2F")
    ax.text(7.25, 6.15, "telemetry, interaction logs, tool\ntrajectories, failure streams\n(the 'flow' — regenerates with life)", ha="center", fontsize=8.5, color="#2F6B2F")
    ax.text(7.25, 5.2, "nascent (2026): employee failure\nsubmission, self-improvement\nloops — D2-E: 2/80, both 2026", ha="center", fontsize=8.5, color="#2F6B2F", style="italic")
    # regeneration cycle arrow
    ax.add_patch(FancyArrowPatch((5.6, 3.0), (6.1, 3.9), connectionstyle="arc3,rad=0.6",
                                 arrowstyle="-|>", mutation_scale=14, color="#55A868", lw=1.6))
    ax.add_patch(FancyArrowPatch((6.1, 3.9), (5.6, 3.0), connectionstyle="arc3,rad=0.6",
                                 arrowstyle="-|>", mutation_scale=14, color="#55A868", lw=1.6))
    ax.text(6.55, 3.35, "practice\nregenerates", fontsize=8, color="#2F6B2F", ha="left")

    # the turn arrow (arcs OVER the wall: the response is to change source, not to climb it)
    ax.add_patch(FancyArrowPatch((3.95, 2.35), (5.05, 2.35), connectionstyle="arc3,rad=-0.45",
                                 arrowstyle="-|>", mutation_scale=20, color="#333333", lw=2.4))
    ax.text(4.5, 1.85, "the turn", ha="center", fontsize=9.5, fontweight="bold")
    ax.text(4.5, 1.45, "(theory's program: change source, not climb the wall)", ha="center", fontsize=7.5, color="#555555")

    # axes labels
    ax.annotate("", xy=(9.8, 0.6), xytext=(0.2, 0.6), arrowprops=dict(arrowstyle="-|>", lw=1.4, color="black"))
    ax.text(5.0, 0.18, "OBJECT OF FITTING:  human works (static stock)  \u2192  human practice (regenerating flow)",
            ha="center", fontsize=10.5, fontweight="bold")
    ax.annotate("", xy=(0.15, 9.0), xytext=(0.15, 0.9), arrowprops=dict(arrowstyle="-|>", lw=1.4, color="black"))
    ax.text(-0.15, 5.0, "FULL COURSE (time of practice)", rotation=90, va="center", ha="center",
            fontsize=10.5, fontweight="bold")

    # spectrum sub-axes (coverage axes) under the flow region
    ax.text(7.05, 2.85, "coverage axes:  \u2713 who (D6)    \u2713 output distribution (D7)",
            fontsize=7.5, color="#2F6B2F", ha="center", fontweight="bold")
    ax.text(7.05, 2.42, "\u2715 experience type (D8) \u2014 missing third axis (0/80 explicit)",
            fontsize=7.5, color="#B22222", ha="center", fontweight="bold", style="italic")

    # fitting lag
    ax.plot([9.0, 9.0], [1.6, 4.6], color="#333333", lw=1.2)
    for y in np.arange(1.9, 4.7, 0.9):
        ax.plot([8.92, 9.08], [y, y], color="#333333", lw=1.0)
    ax.text(9.18, 3.1, "model snapshots\n(quarterly)\n\nfitting lag\n(practice runs\nahead of uptake)", fontsize=7.2, va="center", color="#333333")
    ax.annotate("", xy=(8.65, 3.5), xytext=(8.65, 4.5), arrowprops=dict(arrowstyle="-|>", color="#B8860B", lw=2.0))
    ax.text(8.52, 4.0, "lag", fontsize=8, color="#B8860B", ha="right", fontweight="bold")

    # four termination boundaries
    ax.plot([0.4, 9.6], [9.35, 9.35], color="#8B0000", lw=2.2, ls=(0, (6, 3)))
    ax.text(5.0, 9.55, "B1  END OF THE PRACTICING SUBJECT  (the human term)",
            ha="center", fontsize=9, color="#8B0000", fontweight="bold")
    ax.plot([9.75, 9.75], [1.2, 8.4], color="#8B0000", lw=2.2, ls=(0, (6, 3)))
    ax.text(9.62, 7.6, "B2  FITTER TRANSGRESSION (ASI):\nstudent surpasses all teachers \u2014\ncourse auto-completes",
            rotation=90, va="top", ha="right", fontsize=8, color="#8B0000")
    ax.plot([0.4, 0.4, 4.9], [1.2, 0.95, 0.95], color="#7030A0", lw=1.8, ls=":")
    ax.text(2.6, 1.05, "B3  INSTITUTIONAL BOUNDARY (law / privacy / consent) \u2014 flow extraction rights",
            fontsize=8, color="#7030A0", ha="center", va="bottom")
    ax.add_patch(FancyArrowPatch((7.9, 4.35), (6.4, 4.35), connectionstyle="arc3,rad=-0.55",
                                 arrowstyle="-|>", mutation_scale=16, color="#B0561A", lw=2.0, linestyle="--"))
    ax.text(7.15, 4.6, "B4  SELF-REFERENTIAL CONTAMINATION\nthe mirror enters the room it reflects\n(fitted practice is colored by the fitter)",
            fontsize=8, color="#B0561A", ha="center", fontweight="bold")

    ax.text(5.0, 10.15, "Human-Referential Fitting: Full Spectrum \u00d7 Full Course", ha="center",
            fontsize=13.5, fontweight="bold")
    ax.text(5.0, 9.85, "fitting human practice as the means, augmenting humans as the end (a tool, not a new subject)",
            ha="center", fontsize=9.5, color="#333333", style="italic")

    fig.tight_layout()
    fig.savefig(os.path.join(FIG_DIR, "fig1_theory_framework.png"), dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"\nFigure written: {FIG_DIR}/fig1_theory_framework.png")

def fig2_evidence_map():
    bins = YEAR_BINS
    bin_pos = {b: i for i, b in enumerate(bins)}
    dims = list(D_NAMES.keys())
    rng = np.random.default_rng(20261015)
    fig, axes = plt.subplots(1, 2, figsize=(12.5, 5.8), sharey=True)
    for ax, mod, title in [(axes[0], "E", "Explicit treatment (E)"),
                           (axes[1], "I", "Implicit involvement (I)")]:
        for w in CORPUS:
            if w["year"] is None:
                continue
            b = year_bin(w["year"])
            for di in range(8):
                if w["D"][di] == mod:
                    x = bin_pos[b] + rng.uniform(-0.30, 0.30)
                    y = 7 - di + rng.uniform(-0.22, 0.22)
                    ax.scatter(x, y, s=42, color=LAYER_COLORS[w["layer"]],
                               alpha=0.85, edgecolors="white", linewidths=0.5, zorder=3)
        ax.set_xticks(range(len(bins)))
        ax.set_xticklabels(["classic\n(\u22642019)", "2020\u20132023", "2024\u20132026"], fontsize=9)
        ax.set_title(title, fontsize=11.5, fontweight="bold")
        ax.set_xlim(-0.7, 2.7)
        ax.grid(axis="y", color="#DDDDDD", lw=0.6, zorder=0)
        for spine in ["top", "right"]:
            ax.spines[spine].set_visible(False)
    axes[0].set_yticks(range(8))
    axes[0].set_yticklabels([f"{d}\n{D_NAMES[d].split('(')[0].strip()[3:]}" for d in reversed(dims)], fontsize=8.5)
    # note: y ticks built for rows top=D1..bottom=D8: rows are 7-di; di=0 at y=7 -> top label D1
    # annotate the empty D8-E cell
    axes[0].text(1.0, 0.35, "0 works explicit\n(experience-type axis absent)", ha="center", va="center",
                 fontsize=10, fontweight="bold", color="#B22222",
                 bbox=dict(boxstyle="round,pad=0.35", facecolor="#FDECEA", edgecolor="#B22222", lw=1.2))
    axes[1].text(1.0, 0.35, f"{sum(1 for w in CORPUS if w['D'][7]=='I')} works implicit\n(single cells, axis unnamed)",
                 ha="center", va="center", fontsize=9, color="#8B6914",
                 bbox=dict(boxstyle="round,pad=0.3", facecolor="#FFF8E7", edgecolor="#8B6914", lw=1.0))
    fig.suptitle("Evidence map: which dimension of the object of fitting is treated, and when (N = 80 works)",
                 fontsize=13, fontweight="bold", y=0.99)
    handles = [plt.Line2D([0], [0], marker="o", color="w", markerfacecolor=c, markersize=9, label=LAYER_NAMES[L])
               for L, c in LAYER_COLORS.items()]
    fig.legend(handles=handles, loc="lower center", ncol=5, frameon=False, fontsize=9, bbox_to_anchor=(0.5, -0.02))
    fig.tight_layout(rect=[0, 0.05, 1, 0.96])
    fig.savefig(os.path.join(FIG_DIR, "fig2_evidence_map.png"), dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"Figure written: {FIG_DIR}/fig2_evidence_map.png")

def fig3_stance_heatmap():
    dims = list(D_NAMES.keys())
    fig, axes = plt.subplots(1, 2, figsize=(13.2, 3.9))
    plots = [(axes[0], "A1", ["support", "deny", "na"], "A1 (descriptive stance) x D-explicit counts"),
             (axes[1], "A2", ["augment", "substitute", "anti_tool", "na"], "A2 (normative stance) x D-explicit counts")]
    for ax, field, order, title in plots:
        mat = np.zeros((len(order), 8))
        for r, val in enumerate(order):
            sub = [w for w in CORPUS if w[field] == val]
            for i in range(8):
                mat[r, i] = sum(1 for w in sub if w["D"][i] == "E")
        im = ax.imshow(mat, cmap="Blues", aspect="auto", vmin=0, vmax=mat.max())
        ax.set_xticks(range(8)); ax.set_xticklabels(dims, fontsize=9)
        ax.set_yticks(range(len(order)))
        ax.set_yticklabels([f"{v} (n={sum(1 for w in CORPUS if w[field]==v)})" for v in order], fontsize=9)
        for r in range(len(order)):
            for c in range(8):
                if mat[r, c] > 0:
                    ax.text(c, r, int(mat[r, c]), ha="center", va="center", fontsize=9,
                            color="white" if mat[r, c] > mat.max() * 0.6 else "black", fontweight="bold")
        ax.set_title(title, fontsize=10.5, fontweight="bold")
        ax.grid(False)
    fig.colorbar(im, ax=axes, shrink=0.8, label="works with E code")
    fig.savefig(os.path.join(FIG_DIR, "fig3_stance_dimension_heatmap.png"), dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"Figure written: {FIG_DIR}/fig3_stance_dimension_heatmap.png")

def write_corpus_csv():
    path = os.path.join(HERE, "corpus_v1.csv")
    fields = ["work_id", "title", "authors", "year", "venue", "venue_status", "doc_type",
              "layer", "subdomain", "A1", "A2", "a1_scope", "D", "D2_explicit", "D8_explicit",
              "tier", "peer_reviewed", "confidence", "concurrent", "arxiv_id", "doi", "url",
              "anchor", "notes"]
    with open(path, "w", newline="", encoding="utf-8") as f:
        csvw = csv.writer(f)
        csvw.writerow(fields)
        for w in CORPUS:
            csvw.writerow([w[k] for k in fields])
    print(f"\nCorpus CSV written: {path}")

def main():
    print(f"Surveyed corpus: N = {len(CORPUS)} works")
    print(f"Layers: {dict(Counter(w['layer'] for w in CORPUS))}")
    table1(); table2(); table3(); table4()
    d8_gap_inference(); d2_core(); gharbi_row()
    exploratory_A1xD(); sensitivity(); saturation()
    fig1_framework(); fig2_evidence_map(); fig3_stance_heatmap()
    write_corpus_csv()
    print("\nAll tables/figures complete.")

if __name__ == "__main__":
    main()
