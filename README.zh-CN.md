[English](README.md) | **简体中文**

# 拟合实践，而非作品：AGI 人本拟合论

*Yugui Yu · YYG Strategy Lab · they4897@gmail.com*

**[阅读论文（PDF）](paper.pdf) · [LaTeX 源码](paper.tex) · [图件](figures/) · [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23391808.svg)](https://doi.org/10.5281/zenodo.23391808)**

## 理论一句话

《拟合实践，而非作品》提出 **AGI 人本拟合论**（human-referential fitting theory——一种以人为参照的 AGI 理论）：

拟合对象不是人类的作品，而是人类的实践——经验的**全谱**与**全程**；**存量有墙，流量无墙。**

三条相互连接的主张：

1. **概念层** —— AGI 是一个哲学概念：只要"通用"以人类实践的开放集合为参照系，它就无法被归约为技术规格。
2. **实现层** —— AGI 的手段是**实践拟合**（持续再生的流量：遥测、交互、失败、修复），而非**语料拟合**（被数据墙所限的存量作品）——后者是前者的第一阶段与永久基座：存量是实践的投影，墙限定它的未来，不否定它的过去。
3. **定位层** —— AGI 应当作为**增强性工具**而非新主体来构建与治理：拟合是手段，增强人是目的。

## 证据地图数字版

为使理论可审计，我们对目的性抽样的 **N = 80 篇文献** 按双立场轴（描述性 A1 / 规范性 A2）与八个拟合对象维度（D1–D8，各维度 E=显式 / I=隐式 / −）编码：

| 发现 | 数字 |
|---|---|
| 经验类型轴（成功/失败 × 专家/新手 × 典型/边缘）**被显式处理** | **0/80**（95% CI [0.0%, 4.5%]） |
| 同一轴被隐式触及（仅单格） | 9/80 |
| 实践-流量显式 | 2/80 —— 均为 2026 年 |
| 作品-存量显式（2022 年起连续） | 6/80 |
| 持增强定位的文献 | 10/80（66 篇无规范立场） |
| 缺位检索（8 组检索式 × 3 引擎）D8-E 命中 | 0 |

一句话结果：**话题被触及，轴线从未被命名。**

本文建立在此前实证审计之上：[《成功给方向，失败给精度》（DOI 10.5281/zenodo.23355929）](https://doi.org/10.5281/zenodo.23355929)。实践流数据的工程方法论见姊妹篇《拟合实践：前沿模型训练的数据方法论——附 2026 旗舰管线就绪度审计》（[GitHub: practice-fitting-methodology](https://github.com/yuyuguilab/practice-fitting-methodology)）。

## 仓库结构

```
paper.pdf / paper.tex / paper.bbl   # 英文论文（编译产物 + 源码）
references.bib                      # 107 条编号参考文献
figures/                            # 图1 理论框架、图2 证据地图、图3 立场×维度热图（300dpi）
analysis/coding_data.py             # 全部 80 条编码记录 + 可复现表格/图件
analysis/corpus_v1.csv              # 完整编码语料（80 篇 × 24 字段）
analysis/tables/                    # 表格 CSV，含增补 S1（并发工作单行记录）
02_experiment_protocol.md           # 编码手册：A1/A2 + D1-D8 + E/I 模态，规则 R1-R5、CR1-CR6
03_analysis_report.md               # 统计：二项 CI、Fisher 检验、缺位检索日志
```

## 复现

```bash
python3 analysis/coding_data.py    # 从内嵌编码记录重建全部表格与图件
tectonic paper.tex                 # 重新编译 PDF（需 references.bib + figures/）
```

`analysis/coding_data.py` 中每条编码决策都带有支持引文、来源 URL 与置信层级。所有主张限定于语料内（"该语料内"）；证据地图是目的性样本，不做总体推断。20% 分层盲重编码的 Cohen's κ 已排期于 2026-10-29，将于下一版本报告。

## 引用

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

## AI 辅助披露

文献检索、核验、编码与起草在作者监督下按规则化协议（编码手册规则 R1–R5、CR1–CR6）借助 AI 完成；所有编码主张均带逐字引文或设计锚点；单编码者局限已在论文 §5.5 如实披露。作者对全部内容负责。

## 许可

- **代码**（`analysis/`）：MIT
- **论文、编码手册、图件与编码数据**：[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

## 联系

Yugui Yu · YYG Strategy Lab · they4897@gmail.com
