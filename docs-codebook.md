# 02 Experiment Protocol — 结构化文献证据地图协议 + 编码手册（Codebook）

> experiment-manager 产出 · 2026-10-15 · 上游：01_research_design.md · 无人类被试、无新实验，"数据收集"= 对公开文献的检索、核证与编码。方法学对标论文① docs-codebook（判据全称量词式、边界案例规则化、CR 编号、G 门编号）。

## 1. 设计概要（来自 01，一段话）

本文是概念综合 + 结构化文献审计：用统一编码框架（双立场轴 A1/A2 + 八拟合对象维度 D1–D8 及其显式/隐式模态）对 60–80 篇分层目的性抽样的文献语料（surveyed corpus）编码，产出**证据地图**以回答 RQ1–RQ5：A 轴刻画各文献对"AI 是否拟合人类实践"（描述）与"AI 应否为增强性工具"（规范）的立场分布，D 轴刻画各文献把什么当作拟合对象；核心可检验结果为 **H-m2（D8 经验类型轴的显式处理率 ≈ 0 = C6 缺口可视化）** 与 D2 显式频率（C3 萌芽证据）。流程：**种子抽取 → 资格筛选 → 补漏/缺位检索 → 一手核证与存档 → pilot 编码 → 全量编码 → 两周后 20% 盲重编码 → 数据锁定**。文献窗口硬截止 2026-10-15；所有检索/访问以 2026-10-15 为锚（access_date 如实记录，晚于锚日的发表不入语料）。

## 2. Materials & Instruments

### 2.1 语料正式化（surveyed corpus）

**编码单位**：一篇文献（work）——论文、专著、官方技术报告/系统卡、政策文件原文、可溯源的公开表态文本组（见 CR2）。同作者不同作品分立条目。

**纳入标准（须全部满足）**：① 一手可溯源：有 DOI / arXiv id / 官方 URL / 出版社页（G1）；② 层域覆盖：落入五层配额表（§2.1 末）之一子域——四层 + 方法论蕴含；③ 时间分层：主体 2024–2026，经典不限（Wittgenstein、Arendt、Plessner、Engelbart、Tesler、Gabriel 2020 等）；④ 立场或维度信息可从文本判定（含"未涉"判定本身需可核证）。

**排除标准（硬性）**：① 证伪警示清单 7 条全部排除且禁入写作（Nicole Wu 论文、Hofstadter 自画像出处、DeepMind 2025 单行本、Global RLHF、Anthropic 标注员定量、Qwen/Gemini 逐语言比例、PRS 25 倍——如需失败数据证据一律用论文①已核证口径 +22.25）；② 无一手出处的轶事性主张；③ **内部作品隔离**：作者论文①与内部文章（《AGI 前夜》等，/Users/mark/随笔/documents/）不计入语料与统计，仅作 internal coherence assets 用于互锁叙述（G5）；④ T3（新闻/政策解读）不得为任何 work 的唯一证据源（CR2）。

**来源池与去重**：00_input §2–§3 文献清单 + 01 §3.6 补核新增 + 论文① references.bib 复用约 15 条（PRM800K、LEMA、GLM-5、MiMo、DeepSeek-V4.1、SPAR f26、Hertwig 2009 description–experience gap、DAPO、R1、ETO、UltraInteract、Lightman 2023 等）→ 候选池约 110 条原始提及，去重后预期 85–95，资格筛选后落 60–80。**去重与分层归属规则**：同一 work 在多层出现 → 单条目，记 primary layer（其承重 claim 所在层）+ layer_secondary；禁止双条目。

**分层配额（承 01 §7，即覆盖判据）**：

| 层（primary） | 配额 | 子域构成（种子取自 00_input 对应节） |
|---|---|---|
| L1 概念层 | 12–15 | 定义谱系 4（Legg&Hutter 0712.3329、Levels of AGI 2311.02462、METR 2503.14499、Tesler）；测量学批判 4（2505.10573、Ilić&Gignac、CACM 专文、补漏 1）；移动靶 3（Imeri、2607.03634、LeCun）；哲学人类学 3–4（Plessner 英译 2024、Düwell/De Mul/Tamborini/Sever 择 2–3） |
| L2 实现层 | 25–30 | 文化技术/认知 6（Farrell Science 387:adt9819、Yiu/Kosoy/Gopnik、Webb 2212.09196、Mollo&Millière、Mallory/Søgaard）；拟合实证 6（Kernels of Selfhood PNAS 2025、Hu NMI 2024、Anthropic 2026 emotions、Hertwig 2009 等）；形式化 4（CIRL 1606.03137、RLHF 谱系代表、Yuan 2609.23640）；反对面/相邻 5（Artificial Hivemind saDOrrnNTz、model collapse s41586-024-07566-y、Epoch data wall、FunSearch/AlphaEvolve 择 2、Gharbi concurrent）；技术报告 5–6（DeepSeek-V4.1、MiMo、GLM-5、Llama 3、GPT-6/Claude 系卡择 1–2） |
| L3 定位层 | 10–12 | 谱系 4（Engelbart 1962、Shneiderman 2022、Turing Trap 2201.04200、2506.06576）；实证 3（Arntz/OECD、Korinek&Stiglitz 2412.18593、Stanford centaur evaluations）；反对面 4（Suleyman/Hoffman 数字物种、Sacasas、Laba 2025、2505.10468）；康德 1（Sticker s13347-026-01100-w） |
| L4 张力层 | 12–15 | 多元对齐 5（Gabriel 2020、2402.05070、Park 2405.00254、Baum、Collective Constitutional AI）；模型福利 2–3（Suleyman 2026-09 表态组、Anthropic 福利路线）；中文语境 5（2019 治理原则、2023 全球倡议、2025"人工智能+"意见、李三虎、庄子+Seok/Lam/Muyskens 择 1–2） |
| L5 方法论蕴含 | 5–8 | Spectrum Tuning 2510.06084、WEIRD 2508.19269、Aya 系、DoReMi/Data Mixing Laws/RegMix 择 2、InsTag、FineWeb-Edu；Agent-Dice 2601.03641 与 Transfer-Kim（吸收端）可落此层或 L2 |

### 2.2 编码手册（Codebook，方法学核心）

#### A 轴（立场，双变量，各自单选、相互独立——本理论自身 = A1:support × A2:augment 的组合示范）

**A1 描述性立场**：该文献认为当前/未来 AI 实现实质上是否（部分或主要）构成对人类实践的拟合。

| 取值 | 操作判据（满足其一） | 正例 | 边界案例与判定规则 |
|---|---|---|---|
| `support` 支持 | ① 明示论断 AI 是文化/社会技术、人类行为或偏好分布的拟合器；或 ② 实证证据表明模型内部结构/输出分布/能力形态可归因于对人类数据或实践的拟合 | Farrell et al. 2025（标题即判据①）；Yuan 2026（对齐模型=人类模型） | **Artificial Hivemind：A1=support**——70+ 模型收敛到共同类人分布=证实拟合发生；"拟合平均而非全谱"的缺陷记入 D7/D8 编码与 notes，**不改 A1** |
| `deny` 否认 | ① 明示论断 AI 关键成就非来自/不可归约为拟合人类；或 ② 证据表明"拟合人类"框架不适用于理解其能力 | FunSearch/AlphaEvolve 线（搜索+验证超越人类直觉）；Imeri 2025（AGI 如永动机，范畴错误） | Brynjolfsson Turing Trap：**A1=support 但 scope=路线级**——对"图灵测试传统"这条路线，模仿=目标；notes 必记 scope（系统级/路线级/行业级，规则 R3） |
| `na` 未涉 | 不表达也不蕴含上述立场（CR5：沉默≠反对） | Levels of AGI（分类学工作） | Nature model collapse：递归退化动力学，对"是否拟合人类"无立场 → `na`，D7=E |

**A2 规范性立场**：该文献认为 AI 应否作为增强性工具（应然定位）。

| 取值 | 操作判据 | 正例 | 边界案例与判定规则 |
|---|---|---|---|
| `augment` 增强-工具论 | 明示主张 AI 应设计/治理为增强人类的工具（agency、augmentation、人机协同、以人为本） | Engelbart 1962；Shneiderman 2022；2025"人工智能+"意见；Sticker（康德约束：AI 可为纯手段） | Muyskens 2024（照护机器人无法履行孝道式义务）：对工具论的**内部修正**不改类别，记 notes"修正纯器物论" |
| `substitute` 替代-主体论 | 明示主张/预言 AI 将或应成为自主主体、数字物种或以替代人类为目标 | Suleyman/Hoffman《数字物种》 | Turing Trap = A2:augment × A1:support——双轴独立性示范；其"模仿为目标→替代陷阱"恰为"拟合只能是手段"的反面论证 |
| `anti_tool` 批判-环境论（=指令"反对"） | 明示否定工具范畴本身：AI 是环境/镜子/居所而非工具 | Sacasas "Your AI Is Not a Tool"；Vallor《The AI Mirror》 | Vallor 同时 A1:support（AI 扭曲地拟合/反映人类思维）——批判拟合质量≠否认拟合发生 |
| `na` 未涉 | 无规范性定位表达 | 大部分技术报告 | centaur evaluations：A2=na、A1=na，notes 记"互补窗口警示证据"（供 C4 反面小节使用，不强行落码） |

#### D 轴（拟合对象维度，多选，每维另记模态 E/I）

**模态定义（全维度统一）**：`E 显式处理`=该维度作为**被命名的处理对象**——(a) 出现于标题/摘要/研究问题，或 (b) 为设计中的自变量/约束/优化目标/评价指标，或 (c) 为数据集构建的显式设计原则（配额/分层/字段），或 (d) 正文以术语形式专题讨论 ≥1 段。`I 隐含涉及`=实质进入因果/设计链但未满足 E（顺带提及、仅展望一句、仅作背景）。`− 不涉及`。**E 判据只看命名/操作化，不看重要性（R4）**。E/I 对 D2、D8 为强制记录字段（核心结果），其余维度同格式记录。

| 维度 | 操作定义 | 正例 | 边界案例与判定规则 |
|---|---|---|---|
| D1 作品-存量 | 涉及对人类产出物之既存静态档案的拟合（书面语料/代码库/基准题库） | Llama 3 技术报告（预训练语料配比，E） | Farrell 文化技术论：语料是载体非研究对象 → I |
| D2 实践-流量 | 涉及随部署/生活持续再生的数据（遥测、交互日志、工具轨迹、失败提交流） | DeepSeek-V4.1 员工失败案例提交（E）；生产遥测类（E） | continual learning 文献：处理吸收机制但数据源未指明为实践流 → I；Gharbi：数据工程意义上的 stock/flow → **D2=E 预期，但 notes 必记"工程流量≠实践本体论区分"（G6 划界依据）** |
| D3 价值偏好 | 拟合对象为人类价值/偏好/规范分布 | CIRL→RLHF 谱系（E，奖励模型=偏好分布拟合器）；Gabriel 2020（E） | Park 聚合批评：批评聚合方式仍是把偏好作为对象 → D3=E、A2=na |
| D4 情感功能 | 拟合对象为情感/动机/人格结构之功能性层 | Anthropic 2026 功能性情感概念（E）；Kernels of Selfhood（E）；Hu 2024（E） | 方向判据：须为"模型拟合人的情感功能"；反向因果（AI 塑造人的情感/自我理解，如 Vallor 镜子效应）→ − |
| D5 失败经验 | 拟合对象含失败/错误/低效尝试数据 | MiMo 反思修订数据（E）；LEMA（E） | GRPO 系：失败信号参与训练但未主题化为覆盖对象 → I；FineWeb-Edu 弃 92%：显式排除 → −，notes 记"缺位的证据形态" |
| D6 人群/文化 | 拟合对象的"谁"轴：语言/文化/人口覆盖 | Aya 117 语言（E）；WEIRD 2508.19269（E，文化代表性为自变量） | Llama 3 8% 多语：隐式配额 → I；注意 01 §5 原编号 D6/D7 已对调（见 §8 偏差 1） |
| D7 输出分布覆盖 | 输出分布的覆盖/坍缩/多样性作为拟合质量的分布学性质 | Spectrum Tuning（E，distributional coverage 即其题目）；Artificial Hivemind（E，mode collapse 测度）；Nature model collapse（E） | InsTag/DEITA：覆盖意图明确但对象为数据簇非输出分布 → I |
| D8 经验类型全谱 | 成功/失败、专家/新手、典型/边缘作为覆盖的**类型轴**（非人群、非输出分布）。E 判据（全称量词，须同时满足）：① "经验类型"维被命名为覆盖/抽样/分层轴；② 以此轴设计数据/实验/评价指标 | **构造型正例**（语料内预期缺位）：按 成功×失败 × 专家×新手 全交叉分层配额构建语料的工作将是 D8=E | 处理类型空间**单个单元格**而未主题化轴：MiMo/LEMA/SPAR f26（仅失败）→ I；Hivemind（实证边缘/个体输出丢失）→ I。D8-explicit := (D8==E)，为 H-m2 主结果 |

**编码规则**：R1 D 多选、A1/A2/D 相互独立；R2 A1/A2 以摘要+结论所载主张为准（引言修辞不计，次要立场入 notes）；R3 立场判定的 scope（系统级/路线级/行业级）必记 notes；R4 显式判据独立于重要性；R5 非 `na` 的 A 码与全部 E 码须附逐字引句或设计锚（≤50 词+章节定位），I 码记章节级定位。

**冲突解决（CR）与置信度**：CR1 一手 vs 转引——一手为准，转引降 confidence=low 并记 provenance；CR2 同作者跨作品——作品为单位分立（Suleyman 2023 数字物种 substitute ≠ Suleyman 2026-09"有个性的工具，永不赋予人格"augment；后者以**原推文/原文为 T1 锚 + Reuters 2026-09-16 为语境**成"表态文本组"单条目，confidence=medium）；CR3 版本——以数据锁定日前最新版为准，已发表版优先于 preprint，记 version anchor；CR4 任一判据不可判 → 记 `na`/`−` + confidence=low + 边界案例登记，禁止推断；CR5 沉默≠立场；CR6 内部作品不编码。**置信度**：high=T1+引句齐；medium=T1 但立场为蕴含（需 R3 推断）或引句缺；low=T2/T3 依赖或判据不全。核心 claim（C1–C6）仅可引 high/medium 编码。**来源层级 T**：T1 一手（原创论文无论是否同行评审、官方报告/系统卡、哲学原典、法规原文）；T2 二手学术（同行评审综述/评论/教科书）；T3 次级非学术（新闻/博客/政策解读）——T3 禁入证据链只作动机层；同行评审与否另记 `peer_reviewed` 布尔（与 T 解耦，见偏差 5）。

## 3. Procedure（可执行步骤）

1. **种子抽取**：从 00_input §2–§3、01 §3.6、论文① references.bib 抽取候选 → 候选登记表（work、层、子域、来源节号）。
2. **资格筛选**：按 §2.1 纳入/排除过滤；证伪清单 7 条在池内即拒；去重并落 primary/secondary layer。
3. **配额核对**：对照配额表，缺口子域进入第 4 步。
4. **补漏检索**（每缺口子域 2–3 式，窗口截至 2026-10-15）：如概念层 `"construct validity" benchmark LLM`；实现层 `"cultural evolution" LLM`、`"reward model" human preferences distribution`；定位层 `"human-AI complementarity" evaluation`；方法论层 `"data mixture" diversity coverage`、`"mode collapse" fine-tuning`。命中按 G1/G2 复核后入池。
5. **缺位检索（H-m2 的程序性证据，必须留日志）**：arXiv（2007 起）+ ACL Anthology 全时段，检索式：`"success and failure" coverage training`、`"expert" "novice" data mixture`、`"experience type" coverage`、`"error diversity" curriculum`、`"typical" "edge" spectrum coverage`、中文"成功/失败案例 配比 训练、专家/新手 数据覆盖"。全部命中过 D8-E 判据筛，近失（near-miss）逐条登记理由。
6. **一手核证与存档**：每 work 定位 DOI/arXiv/官方 URL → 存 PDF/快照，登记 URL、version anchor、access_date（锚 2026-10-15）。
7. **特殊核证**：(a) Spectrum Tuning venue——arXiv 元数据 + OpenReview/ICLR 2026 接收名单 + 出版商页三查，核不到即按 arXiv preprint 引用（venue_status=preprint-only，禁写 ICLR 2026/Choi 合作）；(b) Farrell 等补第四作者 Evans；(c) Gharbi SSRN 编号 7479298 与日期 2026-09-17；(d) 证伪清单终扫。
8. **Pilot 编码**（§7 的 5 篇）→ 触发修订则改 codebook 重跑 pilot。
9. **全量编码**：按 §2.2 填编码记录表（§4）；边界判定必引 CR/R 编号。
10. **边界案例登记**：每遇 CR1–CR4 触发即登记（work/冲突/规则/判定/理由）。
11. **信度复检**：编码完成 2 周后按 §5.1 执行 20% 分层盲重编码。
12. **数据锁定**：corpus-v1.0（CSV+JSON+登记表+检索日志+快照清单同库 git 冻结）→ 交 statistical-analyst；此后改动须新增版本并列为 deviation。

## 4. Data Dictionary & Storage Plan

存储同论文①：CSV 主表 + JSON 备份，UTF-8，git 管理。一个观测 = 一篇 work。

| 字段 | 类型 | 定义 |
|---|---|---|
| work_id / title / authors / year | str/int | W-001…；作者列以核证为准（Farrell 含 Evans） |
| venue / venue_status | str/enum | 发表载体；confirmed / pending / preprint-only（Spectrum Tuning 专用 pending 流转） |
| doc_type / layer_primary / layer_secondary | enum | article/book/tech-report/policy/statement-set；L1–L5 |
| A1 / A2 | enum | support/deny/na；augment/substitute/anti_tool/na |
| A1_quote / A2_quote | str | 逐字引句 ≤50 词+定位（R5） |
| D1…D8 | enum ×8 | 每维 E / I / −（E 须引句或设计锚） |
| D2_explicit / D8_explicit | bool | 派生：(D2==E) / (D8==E)——两大核心结果字段 |
| key_quote / source_url / doi / arxiv_id | str | 一手锚 |
| tier / peer_reviewed | enum/bool | T1/T2/T3；venue 是否同行评审（解耦） |
| confidence | enum | high/medium/low（§2.2 分级） |
| concurrent_work / internal_asset | bool | Gharbi、Asymmetric Communication 2607.28137 置 true；内部作品不编码时恒 false 且不入表 |
| access_date / version_anchor | date/str | 锚 2026-10-15；arXiv vN 或报告版本 |
| notes | str | scope（R3）、CR 引用、边界理由、Gharbi 划界备注 |

## 5. Quality Control & Validation Gates

- **G1 可溯源门**：无 DOI/arXiv/官方 URL → 排除。
- **G2 层级门**：T3 禁支撑任何核心 claim；T2/T3 依赖的立场码 confidence 封顶 low。
- **G3 引句门**：非 `na` 的 A 码与全部 E 码无引句/设计锚 → 打回重抽。
- **G4 证伪清单门**：7 条在语料组装与成稿扫描两道检查；PRS 只可写 +22.25（BFCL-V3 25.75 vs 3.50）。
- **G5 隔离门**：内部作品不入语料与统计；正文互锁引用时标 internal coherence asset。
- **G6 并发工作门**：Gharbi（SSRN 7479298，2026-09-17）与 Asymmetric Communication 标 concurrent=true，编码照常 + 论文中显式划界引用；Gharbi 预期 D1=E/D2=E 但无实践-作品本体区分、无全谱×全程坐标系、无工具定位——**划界段素材进 paper-writer**。
- **G7 venue 核证门**：数据锁定前所有 venue_status=pending 必须落为 confirmed 或 preprint-only（Spectrum Tuning 规则见 §3-7a）。

### 5.1 信度子协议（单编码者缓解）

① Codebook 全文随论文附录+仓库公开；② 编码完成 2 周后，对**分层随机 20%**（≥13 works，按五层比例抽）在盲条件（不看首码表）下重编码，报告原始一致率与 Cohen's κ，变量分别计算：A1、A2、D2 模态、D8 模态 **κ ≥ .70**（D 多选按维度分别报告）；未达标 → 修订该变量判据并全量重编码该变量；③ 边界案例登记表全程维护并随附录公开，读者可独立复议。**饱和判据**：最后 10% 编码的 work 未产生新（A1×A2×D）组合或新边界判例 → 饱和；否则补检索至 80 上限并如实报告（方法学参考：以覆盖/饱和证语料规模，不做统计功效）。

## 6. Ethics, Consent & Data Compliance

无人类被试（document audit），consent/IRB 不适用，由 submission-preparer 按"document/literature audit, no human subjects"措辞声明（user action item）。逐字引用每处 ≤50 词、注明出处与章节，fair use，不重分发原文；快照仅作编码存档私有保存不对外再发布；引用数据集类 work 时登记其 license 字段；利益冲突：内部作品隔离（G5）+ 单编码者限制如实在局限性声明。

## 7. Pilot Plan & Revision Criteria

正式编码前对 5 篇试编码（预期码）：**Farrell 2025**（A1=support, A2=na, D1=I, D6=I）；**Artificial Hivemind**（A1=support, A2=na, D7=E, D8=I）；**Turing Trap**（A1=support[路线级], A2=augment, D3=I）；**Vallor**（A1=support, A2=anti_tool, D4=−[反向因果]）；**Spectrum Tuning**（A1=na, A2=na, D7=E, D8=−）。五篇覆盖全部难点：双轴分离、Hivemind 边界规则、scope 注记、anti_tool、D7/D8 判别。**修订触发**：≥2 例无法按判据落码，或任一与预期不符且原因属判据缺陷 → 修订 §2.2 后重跑 pilot 再全量；若属证据新颖（如发现 D8=E 候选）→ 登记边界案例、按 CR 处理并**立即上报作者（C6 证伪信号）**。

## 8. Handoff Notes for Downstream Agents

**→ statistical-analyst（03）**：数据 = 60–80 works × 分类字段（全名义变量，禁均值/间距统计）。必算：① **D 维度频率表（E/I/− 三列分列）——D2-E 与 D8-E 频数是主结果**：D8-E≈0 支撑 H-m2/C6（缺位主张以 §3-5 检索日志为程序性证据，D8-E 计数报 exact binomial 95% CI，0 时用 rule-of-three 上界 ≈3/n）；D2-E 低频+集中于 2025–2026 技术报告支撑 C3 萌芽论；② A1×A2 交叉表；③ **立场×维度热图（01 指定主图，建议双面板 A1×D-E 与 A2×D-E）**；④ 年份分层（经典/<2024/2024–2026 三箱）看 D2-E 趋势；⑤ 层×D 交叉（预期 L5 语料 D7 集中、L2 语料 D1 高频）；⑥ κ+一致率（5.1 结果）。小格用 Fisher 精确检验且仅探索性；**全部结论限定"该语料内"（目的性抽样，无总体推断）**。**H-m1 修订版待检验**：技术报告→A1 集中 na；认知/哲学→support；超人类成就线→deny；**坍塌线分裂**（Hivemind/覆盖线→support+D7=E，model collapse→na+D7=E）——01 原句"坍塌集中于否认"已被 §2.2 Hivemind 边界规则取代。Gharbi D2=E 预期，不影响 C1（见 G6）。

**→ paper-writer（04）**：Methods 素材——§2.1 语料与配额表（压缩为 Table 1）、§2.2 codebook（Table 2 A 轴/Table 3 D 轴+模态）、§3 程序叙事、§5.1 信度声明（单编码者+20% 盲重编码 κ+codebook 公开）、§3-5 缺位检索日志作附录、§6 伦理声明。强制口径：时态条款中英红线句一字不动；证伪清单 7 条禁用；Farrell 四作者；Spectrum Tuning 未核到 ICLR 即引 arXiv:2510.06084 preprint；Gharbi/Asymmetric Communication 作 concurrent work 划界段；**D6/D7 编号以本协议为准**（与 01 §5 对调，稿件内部须一致）。

**→ 需回写 01 的偏差清单（共 6 处，均非设计级修订）**：① D6/D7 对调（任务指令编号；理由：D7 输出分布与 D8 经验类型相邻，凸显"两现有覆盖轴+缺位第三轴"叙事），03/04 须沿用 02 编号；② A2 第四值命名统一为 anti_tool（合并 01"批判-环境"与指令"反对"）；③ 模态 E/I 泛化到全部 D 维度（01 仅 D8-explicit 布尔），因 D2 显式频率升格为核心结果，D8_explicit/D2_explicit 为派生布尔；④ H-m1 措辞修订（坍塌线分裂，见上）；⑤ T 轴语义澄清：T1 一手/T2 二手学术/T3 次级非学术，同行评审与否以 peer_reviewed 布尔解耦（01 的 T1/T2 有集合重叠）；⑥ Suleyman 2026-09 的编码单位="表态文本组"（原推文 T1 锚+Reuters 语境），非 Reuters 报道本身。
