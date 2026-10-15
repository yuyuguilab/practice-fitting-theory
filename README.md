**English** | [简体中文](README.zh-CN.md)

# Fitting the Practice, Not the Works: A Human-Referential Theory of AGI

*Yugui Yu · YYG Strategy Lab · they4897@gmail.com*

**[Read the paper (PDF)](paper.pdf) · [LaTeX source](paper.tex) · [Figures](figures/) · [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23391808.svg)](https://doi.org/10.5281/zenodo.23391808)**

## The theory in one sentence

The object of fitting is not humanity's works but its practice — the full spectrum and the full course of human experience; **the stock has a wall; the flow does not.**

Three connected claims:

1. **Concept** — AGI is a philosophical concept: as long as "generality" is referenced to the open set of human practice, it cannot be reduced to a technical specification.
2. **Implementation** — the means of AGI is *practice-fitting* (the regenerating flow: telemetry, interaction, failure, repair), not *corpus-fitting* (the finite stock of accumulated works bounded by the data wall).
3. **Position** — AGI should be built and governed as an **augmentative tool, not a new subject**: fitting is the means, augmenting humans is the end.

## The evidence map in numbers

To make the theory auditable, we coded a purposefully sampled corpus of **N = 80 works** on two stance axes (descriptive A1 / normative A2) and eight fitting-object dimensions (D1–D8, each E=explicit / I=implicit / −):

| Finding | Number |
|---|---|
| Experience-type axis (success/failure × expert/novice × typical/marginal) **explicitly treated** | **0/80** (95% CI [0.0%, 4.5%]) |
| Same axis *touched implicitly* (single cells only) | 9/80 |
| Practice-as-flow explicit | 2/80 — both from 2026 |
| Works-as-stock explicit, continuously from 2022 | 6/80 |
| Works taking an augmentation stance | 10/80 (66 take no normative stance) |
| Absence-search (8 query families × 3 engines) D8-E hits | 0 |

The one-line result: **the topic is touched; the axis is never named.**

This paper builds on a prior empirical audit: [Success Provides Direction, Failure Provides Precision (DOI 10.5281/zenodo.23355929)](https://doi.org/10.5281/zenodo.23355929). Engineering protocols for practice-flow data are future work.

## Repository Structure

```
paper.pdf / paper.tex / paper.bbl   # English manuscript (compiled + source)
references.bib                      # 79 numbered references
figures/                            # Fig 1 theory framework, Fig 2 evidence map,
                                    # Fig 3 stance x dimension heatmap (300 dpi)
analysis/coding_data.py             # All 80 coded records + reproducible tables/figures
analysis/corpus_v1.csv              # Full coded corpus (80 works x 24 fields)
analysis/tables/                    # Table CSVs incl. supplement S1 (concurrent-work row)
02_experiment_protocol.md           # Codebook: A1/A2 + D1-D8 + E/I modality, rules R1-R5, CR1-CR6
03_analysis_report.md               # Statistics: binomial CIs, Fisher tests, absence-search log
```

## Reproduce

```bash
python3 analysis/coding_data.py    # regenerates all tables + figures from embedded coding records
tectonic paper.tex                 # rebuild the PDF (requires references.bib + figures/)
```

Every coding decision in `analysis/coding_data.py` carries its supporting quotation, source URL, and confidence tier. All claims are bounded to the corpus ("within this corpus"); the map is a purposeful sample, not a population inference. Cohen's κ from a 20% stratified blind re-coding is scheduled for 2026-10-29 and will be reported in the next version.

## Citation

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23391808.svg)](https://doi.org/10.5281/zenodo.23391808)

```bibtex
@article{yu2026practicefitting,
  title   = {Fitting the Practice, Not the Works: A Human-Referential Theory of AGI},
  author  = {Yugui Yu},
  journal = {YYG Strategy Lab, preprint},
  year    = {2026},
  month   = {10},
  doi     = {10.5281/zenodo.23391808},
  url     = {https://github.com/yuyuguilab/practice-fitting-theory}
}
```

## AI-assistance disclosure

Literature search, verification, coding, and drafting were conducted with AI assistance under the author's supervision and a rule-governed protocol (codebook rules R1–R5, CR1–CR6); all coded claims carry verbatim or design anchors; single-coder limitations are disclosed in the paper (§5.5). The author is responsible for all content.

## License

- **Code** (`analysis/`): MIT
- **Manuscript, codebook, figures, and coding data**: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

## Contact

Yugui Yu · YYG Strategy Lab · they4897@gmail.com
