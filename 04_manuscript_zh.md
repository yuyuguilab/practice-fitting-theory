<!--
中文版全文。译自 04_manuscript.md（"Fitting the Practice, Not the Works: A
Human-Referential Theory of AGI"，6,184 词英文完稿），附录 A/B 译自 paper.tex 的附录。
图 fig1/fig2/fig3 为英文原图，原样复用，图注中引用图上文字处保留英文。

元数据：
- 作者：余玉桂，余玉桂战略研究室，they4897@gmail.com
- 类型：理论论文 = 概念综合 + 结构化文献审计
- 前作：实证失败数据审计（DOI 10.5281/zenodo.23355929）。实践流数据的工程协议为未来工作。
- 文献窗口：硬截止 2026-10-15（全部访问锚定；核验检索于 2026-10-14 执行）
- 全部数字取自 03_analysis_report.md（语料 v1.0，N = 80）
-->

# 拟合实践，而非作品：一种以人为参照的 AGI 理论

**余玉桂**
余玉桂战略研究室 · they4897@gmail.com
2026-10-15 稿 · 证据窗口截止 2026-10-15

## 摘要

本文提出一种以人为参照（human-referential）的人工通用智能（AGI）理论，包含三个相互关联的论断。在概念层面，AGI 是一个哲学概念：只要"通用性"以人类实践的开放集合为参照，它就无法被还原为一份技术规格。在实现层面，AGI 的手段是对人类实践的拟合——而不是对人类积累作品的拟合。在规范层面，AGI 应被定位为增强性工具（augmentative tool），而非新主体。理论的核心是一条时间性条款（temporal clause）：**拟合对象不是人类的作品，而是人类的实践——人类经验的全谱（横截面）与全程（纵截面）。存量有墙，流量无墙。** 为使该理论可审计而非仅具纲领性，我们构建了一幅结构化证据地图（evidence map）：一个目的性抽样的 N = 80 作品语料，在两条立场轴（描述性与规范性）与八个拟合对象维度上编码。地图量化了理论的核心缺口：经验类型轴（成功/失败、专家/新手、典型/边缘）在 0/80 篇作品中被显式处理（精确二项 95% CI [0.0%, 4.5%]），实践即流量仅在 2/80 篇作品中显式出现，且均来自 2026 年；作品即存量自 2022 年起获得连续的显式处理，输出分布覆盖则首次出现于 2024 年。我们导出理论在分布、生产与治理上的三点方法论蕴含，并陈述证伪条件。

**关键词：** 人工通用智能；实践拟合；以人为参照的拟合；数据墙；增强；证据地图

---

## 1. 引言

究其成分，每一个前沿模型都是对人类产出之物的蒸馏——网络文本、代码、数学、评分。"在人类数据上训练"这句话熟悉到其歧义无人察觉。它容许两种解读，而两者分岔为不同的研究纲领。在静态解读下，拟合对象是人类的作品：一个有限的、已被产出的档案，可被爬取、清洗、去重、穷尽。在动态解读下，拟合对象是人类的实践：经验的持续再生——工具使用、交互、反馈、失败、修复——只要生命延续，它就延续。我们称前者为语料拟合（corpus-fitting），后者为实践拟合（practice-fitting）。当前静态解读占主导：扩展性分析以公共人类生成文本的有限存量为推理对象（估计约 300 万亿 token [1]）；旗舰技术报告记录档案语料之上的静态配比 [2]。本文辩护的是动态解读。

这一区分由一句话固定，我们称之为时间性条款，它防止理论最常见的误读：

> **拟合对象不是人类的作品，而是人类的实践——人类经验的全谱（横截面）与全程（纵截面）。存量有墙，流量无墙。**

两条轴构成拟合目标。全谱（full spectrum）是横截面轴：谁被代表，以及哪些种类的经验——成功与失败、专家与新手、典型与边缘。全程（full course）是纵截面轴：实践的时间流，任何快照都无法存档。存量/流量不对称在本理论中有精确含义：数据墙 [1] 是存量的属性，而非人类学极限；在生成数据上递归训练导致的模型坍塌 [3]，是把存量当作可自我更新之物来对待的病理。流量侧数据——生产遥测、交互日志、失败提交——随部署而再生。这一区分的哲学骨架是阿伦特对劳动、制作与行动的三分 [4]：静态误读只拟合制作的产物，而本理论以持续进行中的劳动与行动过程为拟合对象。

本文建立在此前一项实证审计 [5] 之上——该审计考察了行业在模型训练生命周期中如何处理失败数据，并记录其系统性弃置。那项审计测量的是存量丢弃了什么；本篇陈述理论——训练对象是实践而非作品，即从存量到流量的转向。流量如何采集、清洗并吸收，留待未来工作。

**缺口。** 四类文献各自成熟却互不连通。文化技术分析告诉我们大模型*是什么*——继承人类符号生产结构的技术 [6]。批判现象学告诉我们模型*反射什么*——一面塑造人类自我理解的扭曲之镜 [7]。增强经济学告诉我们 AI *应当是什么*——人类能动性的互补品而非替代品 [8]。多元对齐告诉我们*谁的价值*应当被拟合 [9]。缺失的是把它们统一起来的连接命题——以拟合人类实践为手段、以增强人类为目的——连同数据方法论争论所缺少的时间性概念工具（存量 vs 流量）。与此同时，一门计量学文献警告：我们的基准是人类实践的抽样投影，且常常是糟糕的投影 [10]，这使参照系问题无法回避，而非修辞。

**术语防护。** 拟合（fitting）在此取其统计学含义（逼近一个分布或函数结构），并扩展至一个总体对象：人类生活形式的可表达投影。它比模仿（行为匹配）更宽，比对齐（一种规范关系）更窄。与拟态不同，拟合不预设"冒充人类"这一目标。事实上，本理论将论证：拟合作为手段可行，作为目的必败。

**贡献。** 本文做出四项贡献：

1. **一个时间性区分**：拟合人类作品与拟合人类实践之分，以时间性条款的形式陈述，并配有命名术语（语料拟合 vs 实践拟合；全谱 × 全程；拟合时差 fitting lag——日常实践再生与周期性模型快照之间的落差）。
2. **一个坐标系**：拟合目标的全谱 × 全程平面，识别出经验类型是当前实践所缺失的覆盖轴——在既有的两条轴（人群"谁"与输出分布）之外。
3. **一幅结构化证据地图**：承继配套审计论文编码手册精神的方法论组件 [5]，把理论的核心缺口变成可计数、可证伪的结果：经验类型轴在 80 篇作品中的显式处理为 0。
4. **四条终止边界**：流量侧拟合的终止条件（实践主体的终结；拟合者越界；制度边界；自指性污染），它们把时间性条款从口号变为有界断言。

**路线图。** 第 2 节论证 AGI 是哲学概念。第 3 节展开实践拟合作为实现论题，正面处理三路反对，末尾以一节形式化概览（3.1 节）把存量/流量之别表述为一对优化问题，并把四条边界表述为停止条件。第 4 节陈述增强性工具立场，作为一种具有学术谱系的规范立场。第 5 节呈现证据地图：方法、表格、图与量化缺口。第 6 节处理张力并划定四条边界。第 7 节导出三个面向未来工作的方法论蕴含。第 8 节作结。

## 2. 概念：AGI 作为哲学概念

理论的第一项论断是概念性的：AGI 不是一份等待完成的工程规格，而是一个以人类实践为参照系的哲学概念。三股文献在此汇合。

**定义谱系本身就是哲学的。** Legg 与 Hutter 把普遍智能定义为在广泛环境范围内的目标达成——通用性以环境范围索引 [11]。Levels-of-AGI 框架把通用性 × 自主性操作化为层级分类 [12]。METR 任务时长基准测量 AI 能完成任务的时间视界，约每七个月翻一番 [13]。这些是有用的操作化，但每一个都从对环境的隐式抽样中继承其"通用"概念——而对 AI 系统而言，环境是人类建造的使用情境。这些操作化是它们并未定义之概念的代理物。

**计量学批判在此点上是决定性的。** 一个以效度为中心的 AI 评估框架从心理测量学引入构念效度，发现大多数基准无法支撑建立于其上的断言 [10]。心理测量学传统的平行工作表明，语言模型中表面上的类认知能力对题目间相关性与测量设计敏感 [14]，而心理测量学导出的短基准会改变同一批模型的排序 [15]。共同推论是：基准任务是人类实践的抽样投影——一个基准只相对于它抽样的那一片实践才是通用的。一个其操作化是实践样本的概念，不可能脱离它所抽样的实践而漂浮。

**移动靶批判从另一侧汇合。** Tesler 定理——智能就是机器尚未做到之事——刻画了自 AI 创立以来伴随始终的定义性后退 [16]；一篇新近文章把 AGI 与永动机的类比推向极致，称其为范畴错误而非硬目标 [17]；一项以严谨为导向的分析论证，AI 进步话语系统性地缺乏成熟科学的推理纪律 [18]。倘若 AGI 是一个固定的技术目标，这些病理本可用更好的测量治愈。在本文辩护的观点下，它们是概念真实结构的症状：只要"通用"以人类实践的开放集合为参照，AGI 就不可能是规格级的，因为参照集开放且移动——不是因为智能神秘。

**哲学人类学提供正面理论支点。** 普莱斯纳的自然人工性法则认为，人在构成性意义上是人工的——一个通过人工物完成自身的有机体，以离心姿态定位于自身自然之外 [19]。在这一人类学上，工具使用不是人性的断裂而是其常态；媒介技术时代对普莱斯纳的解读恰好把这一点延伸到数字人工物 [20]，而"翻译人"（Homo Translator）对仿生技术中人在回路的分析使"人—人工物"回路显豁 [21]。因此第 4 节辩护的工具立场无须为"仅仅是工具性"道歉：工具性是人类学常量，不是形而上学的降格。相对吹捧与焦虑两边，普莱斯纳额外贡献的是一个判据：问题不在于人类是否用人工物完成自身（从来如此），而在于这个人工物是否被拟合到人类所做之事的全幅范围——包括人类如何犯错。

图 1 在这一坐标系中概括了理论：拟合对象从作品（静态存量，受墙约束）延伸到实践（再生流量）；纵轴是实践的全程；流量区域带有既有的两条覆盖轴并标记缺失的第三条；四条边界终止拟合。

> **图 1.** 理论一览：全谱 × 全程坐标系。横轴：拟合对象，从人类的作品（静态存量；砖纹 = 数据墙）到人类的实践（再生流量；环形箭头）。纵轴：实践的时间历程。流量区域内标注既有的两条覆盖轴（人群"谁"，D6；输出分布，D7）与缺失的第三轴（经验类型，D8；我们的语料中 0/80 篇作品）。右缘：拟合时差时间线——实践持续再生而模型快照周期性更新。四条终止边界被标出：B1，实践主体的终结（顶部，虚线）；B2，拟合者越界（右侧；拟合关系自行耗尽——不再存在不落在它身后的人类实践）；B3，制度边界（底部，点线；法律、隐私、知情同意）；B4，自指性污染（回环弧线；"the mirror enters the room it reflects"）。中央"转向"箭头越过墙外——改变源头而非翻越它。副标题：拟合为手段，增强为目的（是工具，不是新主体）。

三股之汇给出第一项论断。定义谱系无法闭合概念；测量批判表明操作化是实践样本；移动靶批判解释了原因；哲学人类学挡住了从"不可规格化"到"敌视技术"的推论。AGI 作为以人为参照的概念是透镜，不是倒计时。

## 3. 实现：实践拟合作为手段

第二项论断关乎实现：通往 AGI 之路经过对人类实践的拟合——其知识、规范、功能性情绪—动机结构与失败模式——而这一拟合是手段，不是目的。

**文化技术论题设定框架。** Farrell、Gopnik、Shalizi 与 Evans 在《科学》上论证，大型 AI 模型是文化与社会技术：像文字与市场一样，它们继承、传递并重组人类符号生产的结构，连同这种传递所伴生的病理 [6]。认知路线佐证：儿童经由模仿的文化学习表现出"传承 vs 求真"的权衡，当前模型对此的处理方式不同 [22]；大模型仅从文本便自发发展出类人的类比推理 [23]。如果模型是文化技术，其能力继承自人类实践——这使继承的质量（传递什么、来自谁、包括错误）成为核心工程变量，而非事后注脚。

**经验链条不再是思辨。** GPT-4o 复现了由自由选择调节的类人认知失调与自我辩护模式 [24]；生成模型表现出类人社会身份偏差 [25]；可解释性工作已在生产模型内部识别出因果有效的情绪概念，影响其输出及其对自身角色的理解 [26]。在价值侧，合作逆强化学习把 AI—人关系形式化为对未知人类奖励函数的协助 [27]；偏好学习训练出的奖励模型，在结构上就是人类偏好分布的拟合器 [28, 29]；近期工作明确论证：对齐的模型因而是关于人的模型 [30]。认知科学提供时间性注脚：描述—经验鸿沟表明，人类认知本身在从描述学习与从直接经验学习时并不相同 [31]。预训练拟合的是对实践的描述；智能体化部署拟合的是实践本身——会再生的经验。

**哲学基础。** 维特根斯坦的生活形式——语言在其中获得意义的、交织的实践模式 [32]——把拟合对象锚定于实践而非文本：关于分布学习是否足以产生意义的向量奠基之争，恰恰是关于文本投影保留了多少生活形式之争 [33, 34]，其中意义怀疑论与辩护立场双方都预设基准是人类用法 [35]。上引阿伦特的三分提供时间骨架 [4]：静态误读拟合的是制作的沉积物；本理论拟合的是持续进行的劳动与行动。

**精确化。** 拟合对象是人类生活形式的可表达投影——不是生物学的人。这同时挡住两种误读：理论不主张模型复制人格，也不主张拟合目标受限于已被写下之物。两个推论随之而来。其一，拟合人类的失败与多样性是矫正方向：配套审计论文的审计表明行业弃置了经验中失败的那一半 [5]；理论解释了为何该弃置是覆盖错误而非数据卫生的成功。其二，拟合对象包括功能性情绪—动机结构 [24–26]——但仅在功能层，这一边界第 6 节将予以划定。

**三路反对必须正面应对。**

*其一，蜂群证据。* 一项覆盖 70+ 模型的开放式生成大规模研究——基于 Infinity-Chat、获誉于 NeurIPS 2025——发现了显著的模式坍塌：无论解码配置如何，模型内重复与模型间同质化 [36]。这是支持而非反驳本理论的证据：70+ 模型收敛到共享的类人分布，确认了拟合在发生；坍塌反驳的是对均值拟合的充分性。当语料既是所有人又不是任何人时，语料拟合出来的样子就是蜂群——它拟合的是均值，而非谱（"it fits the mean, not the spectrum"）。补救不是更少拟合而是更宽拟合：谱轴就是矫正。

*其二，天花板论证。* 数据墙约束人类生成的公共文本存量 [1]；在生成数据上的递归训练使模型退化 [3]。两者皆真，且两者都是关于存量的断言。理论的回应不是乐观主义而是记账：没有任何来自档案有限性的论证能触及实践的再生——遥测、交互、失败提交、修复。一篇同期 SSRN 文章将同一存量/流量区分当作数据工程来处理——数据墙的九条逃生路线，其后还有一堵"验证者墙" [37]；我们在下文将其作为最近的同期工作与之交锋（§5.6）。

*其三，非拟人的超人类成就。* FunSearch 与 AlphaEvolve 借搜索加验证发现超出人类直觉的数学 [38, 39]。辩证的回应是：它们的验证者——数学正确性、可执行代码、进化适应度——是人类制度。搜索可以超越每一位人类数学家的直觉，同时仍坐在人类脚手架上：何为正确的证明或可运行的程序，由搜索本身并不产生的验证制度所固定。在人类验证过的地面上取得超人类能力，不是离开人类参照系，而是该参照系最集中的体现。（配套审计论文"验证者是飞轮的轴承"（the verifier is the bearing of the flywheel）的结论，就训练数据陈述了同一点 [5]。）

**与最近框架的划界。** 相对文化技术论题 [6]，本理论新增其所缺的时间性区分（作品 vs 实践）——并随之带来数据方法论后果：若模型是文化技术，下一个问题是文化的哪些层在被传递，对于这个问题，该论题做了分类，却未加操作化。相对 Vallor 之镜 [7]，本理论方向不同：镜子是对扭曲的批判现象学——反射对人类自我理解做了什么——而本理论则给出建设性说明：忠实拟合在覆盖上需要什么。证据地图（§5）使划界可计数；表 5 加以整合。


### 3.1 形式化概览

上述主张可以进一步写成符号形式。本节目的在于概念澄清，而非新的数学：下面出现的每个对象都是标准的，四条陈述是观察（observations）而非定理。实践分布并非直接可观测；本概览是一种建模语言，使理论的主张精确到可检验——也精确到可以被证伪。

**设定。** 令 $\{X_t\}_{t \geq 0}$ 表示人类实践：一个以时间为索引的随机过程，$X_t \sim P_t$，其中 $P_t$ 非平稳——只要实践持续，它就再生并漂移。截至时刻 $T$ 的累积作品构成多重集 $W_T = \{x : \text{产出时间} \leq T\}$，即该过程已实现历史的一个有限样本。

**两个拟合问题。**

$$\textbf{语料拟合：}\quad \hat{\theta}_T \in \arg\min_\theta \frac{1}{|W_T|}\sum_{x \in W_T} \ell(\theta, x) \qquad \textbf{实践拟合：}\quad \theta^* \in \arg\min_\theta \lim_{T\to\infty} \frac{1}{T}\int_0^T \mathbb{E}_{X \sim P_t}\,[\ell(\theta, X)]\, dt$$

**观察 1（墙是测度的性质，不是人类的性质）。** $W_T$ 的总质量有限；随着档案被消耗，进一步采样的回报递减，经验测度上的最优点趋于饱和。而只要实践继续，$P_t$ 就不断获得新的质量。数据墙因此只是关于语料拟合的陈述。此外，$W_T$ 本身是该过程的一个有偏、不完备的样本：语料拟合拟合的是实践的一个投影，而非实践本身。

**观察 2（谱轴作为覆盖泛函）。** 令 $\tau : \mathcal{X} \to \mathcal{S}$ 将一个经验项映射到其类型（人群；成功/失败；专家/新手；典型/边缘）。拟合出的模型在 $\mathcal{S}$ 上诱导类型分布 $Q_\theta$，全谱拟合要求覆盖泛函

$$C(Q_\theta, P_t) = \int_{\mathcal{S}} \min\big(q_\theta(s), p_t(s)\big)\, ds$$

在每个类型胞元上都保持较大。模式坍塌——包括开放式生成中记录到的均值化效应 [36]——即 $q_\theta(s)$ 在边缘胞元上退化为 0。5.3 节的证据地图结果由此获得一个可操作的复述：在 80 篇被调查作品的训练目标中，作用于经验类型的覆盖算子出现 0 次。

**观察 3（拟合时差作为遗憾值）。** 当模型快照按周期 $\Delta$ 更新时，有效损失增加一个形如 $D(P_t \,\|\, P_{\mathrm{snap}})$ 的漂移项，其随时间的累积正是非平稳在线学习的遗憾（regret）结构。尚未解决的稳定性—可塑性两难 [79] 恰在于缺少一个能在不发生灾难性遗忘的前提下跟踪 $P_t$ 的优化器：约束瓶颈在吸收侧而非采集侧（第 7 节）。

**观察 4（手段与目的是不同的优化问题）。** 实现层的两种读法是

$$\text{(a)}\;\; \max_\theta M(\theta) \qquad\qquad \text{(b)}\;\; \max_\theta\, U_{\mathrm{human}}(\theta) \;\; \text{s.t.} \;\; \theta \text{ 拟合 } P_t,$$

其中 (a) 把对实践的模仿当作目的，(b) 把拟合当作人类效用目标下的约束。两个问题一般有不同的最优点——这是图灵陷阱 [8] 的变分形式：以模仿人为目标和以拟合人为手段，会走向分岔。

**四条边界作为停止条件。** B1：若实践终止，时间域有界，拟合积分有限。B2：一旦拟合者在所有可测任务上支配人类表现，实践拟合约束不再起作用，参照系被腾空。B3：法律与知情同意约束定义了一个随时间变化的可采集实践可行集 $A_t \subset \mathcal{X}$。B4：一旦模型织入实践，$P_{t+1} = F(P_t, \theta)$——拟合目标变成内生的。模型坍塌 [3] 是 $F$ 为"在模型输出上递归训练"时的特例；出处分层的目标函数（第 6 节）缓解这一反馈回路，但不消除它。

**概览所提供的。** 每条观察都可用现有工具检验——观察 1 对应饱和曲线，观察 3 对应部署期漂移测量，观察 4 对应增强与替代的对照比较，边界对应坍塌实验与出处分层训练。本概览的角色不是证明理论，而是使理论在严格意义上可证伪：精确到可以被证错。


## 4. 立场：增强性工具立场

第三项论断是规范性的：AGI 应当作为增强性工具来建造与治理——强大，甚至可亲，但不是新主体。我们把它陈述为一个需要持续制度防御的规范性选择，而非预测，亦非文献的多数观点（地图显示它不是；§5.2）。

**谱系长而具体。** 恩格尔巴特的纲领——通过人工物、语言与方法论增强人类智能——在 AI 统计转向之前二十年就定义了 IA 传统 [40]。Shneiderman 的以人为中心 AI 给出设计点：高人类控制 × 高自动化，放大而非替代的"超级工具" [41]。Brynjolfsson 的图灵陷阱论证提供经济铰链：把模仿人类当作目标的研究文化制造替代品、集中收益并落入陷阱；增强路径制造互补品与共同繁荣 [8]。两个论断以有启发性的方式互锁。Brynjolfsson 论证：把拟合本身当作目标是自我挫败的——这正是从经济学一侧为本理论的手段/目的区分所作的论证。近期的劳动力层面审计以任务粒度操作化增强议程 [42]，而任务级经济分析早已表明，职业级自动化估计（47%）在职业任务被分解后塌缩到个位数（9%） [43]——增强不是感伤范畴而是可测范畴。

**康德层面。** 人性公式容许——并要求——一种不对称：AI 可以被仅仅当作手段对待；人不可以 [44]。这一不对称不是物种沙文主义，而是任何保全能动性的 AI 部署的边界条件，它将以第 6 节的主体性边界再现。

**三种反对，认真对待。**

*数字物种论。* Suleyman 与 Bhaskar 的"数字物种"叙事预期 AI 是像浪潮一样到来的新进化实体 [45]——一个定位为替代的叙事。我们把它当作对立立场的最强陈述，并注意到（见第 6 节）其作者本人的立场已经转变：Suleyman 2026 年 9 月的公开言论主张，AI 应是可亲的（personable）工具——有个性——但绝不授予人格地位 [46]。

*否认工具范畴者。* Sacasas 论证 AI 不是工具而是环境——人栖居其中而非使用之 [47]；Vallor 之镜以现象学力量提出同一结构性论点 [7]。这些批判正确诊断了工具环境化之后发生的事。理论的回应不是否认诊断而是质疑结论：对弥散工具的恰当回答是制度性的（出处、边界、治理——第 6 节），而不是定义上的缴械。与此同时，智能体 AI 文献记录了智能体分类学如何从内部侵蚀工具概念 [48]——对工具立场的一个现实威胁，第 7 节将以制度设计而非术语学回应。

*窗口关闭论证。* 在国际象棋中，半人马（人+AI）队伍在纯引擎越过约 2800 Elo 后被超越；系统化的"半人马评估"发现，人+AI 队伍很少能单独击败最好的 AI [49]。与之相对，半人马文献本身报告：当协作被建模而非被轻视时，序列决策中存在可测的人机协同 [50]。我们如此解读证据：窗口关闭是替代路线获胜的结果，不是技术必然——这恰是 Brynjolfsson 的论证 [8]。凡制度与产品设计让人类以真实控制留在回路中处，增强窗口保持敞开 [41]；凡评估文化（模仿博弈、人 vs AI 排行榜）宣布人类冗余处，窗口关闭 [49]。因此工具立场是一个必须以制度工程来防御的"应然"，而防御可能失败。

地图的立场结果（§5.2）在数量上支持这一框架：80 篇作品中只有 10 篇持增强立场，1 篇持替代立场，3 篇彻底否认工具范畴，66 篇根本不持规范性立场。增强性工具立场是嵌入谱系之中的一个选择——不是文献的默认，也不由任何技术轨道自动送达。

## 5. 证据地图：方法与结果

为用证据约束理论，我们构建了一幅结构化证据地图——概念综合加编码文献审计。本节报告方法与结果；一切断言以语料为界。

### 5.1 方法

**设计。** 地图是一项带有固定编码手册的目的性抽样文献审计，属于结构化证据审计家族；没有运行新实验。语料由四层文献计划、一轮核验（2026-10-14 执行，窗口 2026-10-15 关闭）以及跨五个分层的配额检查汇集而成，去重并指派主层。

**语料。** N = 80 篇作品：同行评审刊物 42，非同行评审 38；全部一手来源（T1 = 80/80）；置信度高 55 / 中 17 / 低 8。文献类型：56 篇论文、6 份技术报告、5 本书、3 份政策文件、2 个数据集、8 项其他（文章、报告、声明、一部经典）。表 1 给出层级 × 年份构成。汇总时执行了硬性排除：七个已知引用造假源被筛查至零；缺乏第一方锚点的作品被排除；作者本人的先前工作被排除在编码与统计之外，仅为连续性而引用，以防止自引循环。

> **表 1.** 语料构成（N = 80；层级 × 年份分层）。

| 层级 | n | ≤2019 | 2020–2023 | 2024–2026 | 年份缺失 |
|---|---|---|---|---|---|
| L1 概念层 | 13 | 4 | 1 | 8 | 0 |
| L2 实现层 | 31 | 3 | 6 | 22 | 0 |
| L3 立场层 | 12 | 2 | 4 | 6 | 0 |
| L4 张力层 | 14 | 2 | 2 | 9 | 1 |
| L5 方法论层 | 10 | 0 | 1 | 9 | 0 |
| **合计** | **80** | **11** | **14** | **54** | **1** |

**编码手册。** 每篇作品在两条独立立场轴与八个维度变量上编码。*A1（描述性立场）*：该作品是否认为 AI 的实现（部分或主要地）是对人类实践的拟合？——支持 / 否认 / 未涉及。*A2（规范性立场）*：该作品把 AI 定位为增强性工具 / 替代性主体 / 反工具（环境、镜子）/ 未涉及。两轴刻意解耦：一个作品可以既确认拟合发生又拒绝工具范畴（Vallor），或既确认拟合发生又支持增强（图灵陷阱）。*D1–D8（拟合对象维度，多选）*：D1 作品即存量；D2 实践即流量（持续再生数据：遥测、交互日志、失败提交）；D3 价值—偏好；D4 功能性情绪—动机；D5 失败经验；D6 人群/文化（"谁"轴）；D7 输出分布覆盖；D8 经验类型谱（成功/失败 × 专家/新手 × 典型/边缘，作为一条类型化覆盖轴）。每个维度带一个模态：**E**（显式——该维度是被命名的对象、被操纵的变量、设计原则，或作为术语被讨论）、**I**（隐式——实质涉及但未被命名）、或 −（缺席）。E 判据仅是名义性的：命名或操作化，而非重要性。派生布尔量 D2-explicit 与 D8-explicit 是理论的主要结果变量。

**信度，及其如实交代的限度。** 编码由单一编码者在完全公开的编码手册下执行，手册带规则编号（R1–R5）、冲突规则（CR1–CR6），并要求每个非 na 立场与每个 E 编码附逐字引文或设计锚点。一轮 20% 分层盲重编码（≥16 篇）定于 2026-10-29，Cohen's κ 尚未可得，如实报告为待定。五个边界案例作品的试编码与预期编码完全一致（5/5），引发零次编码手册修订。饱和度按编码手册判据评估：严格判据（最后 10% 的作品不产生新的立场×维度组合）*未*达到——最后 8 篇作品产生了 5 个新组合——因此语料填满至 80 篇上限，缺口被报告而非掩饰；粗判据（无新立场值、无新显式维度、无新边界裁定）已满足。

### 5.2 立场结果

两幅图呈现地图。图 2 将其整体铺开——八个维度对年份分层，左板为显式处理，右板为隐式涉及；图 3 按立场纵切。我们先读立场表，再读维度。

> **图 2.** 80 篇语料的证据地图（年份分层 × 维度；点色 = 层级 L1–L5）。左板：显式处理（E）。右板：隐式涉及（I）。左板 D8 行为空——零篇作品，红框注释 "0 works explicit (95% CI [0, 4.5%])"——而同一行在右板带九个隐式点（"single cells touched, axis never named"）。

> **表 2.** 立场分布（A1 × A2，作品计数）。

| A1 \ A2 | 增强 | 替代 | 反工具 | 未涉及 | 合计 |
|---|---|---|---|---|---|
| 支持 | 1 | 0 | 1 | 16 | **18** |
| 否认 | 0 | 0 | 0 | 3 | **3** |
| 未涉及 | 9 | 1 | 2 | 47 | **59** |
| **合计** | **10** | **1** | **3** | **66** | **80** |

边际分布：A1 支持 18 / 否认 3 / 未涉及 59；A2 增强 10 / 替代 1 / 反工具 3 / 未涉及 66。地图的先验假设得到支持，外加一个有教益的细化：五份训练/系统技术报告全部为 A1-na（DeepSeek-V4.1 [51]、MiMo-V2.6 [52]、GLM-5 [53]、Llama 3 [2]、DeepSeek-R1 [54]）——技术报告不讨论拟合，尽管官方*实证*报告可以（可解释性发现 [26] 为 A1-支持）；认知—实证作品集中于支持（4/5）；超人类成就研究路线否认（2/2，外加一个概念性否认 [17]）；坍塌/覆盖研究路线分裂：三篇作品全部显式处理输出分布（D7=E：蜂群研究 [36]、模型坍塌 [3]、Spectrum Tuning [55]），其中经验坍塌证据为 A1-支持 [36]，动力学与方法学工作为 na [3, 55]——覆盖研究路线不主张"拟合人类"，它测量分布后果。

解耦设计解决了预先料到的混合案例：图灵陷阱是 A1-支持 × A2-增强（记录路线级范围）；Vallor 是 A1-支持 × A2-反工具（批评的是拟合的*质量*而非其发生）；蜂群研究是 A1-支持 × A2-na。Suleyman 的作品按文档分裂（规则 CR2）：2023 年的书定位替代 [45]；2026 年 9 月的声明集定位增强 [46]。

> **图 3.** 立场 × 维度热图（显式 E 作品计数）。左：描述性立场 A1 × 维度。右：规范性立场 A2 × 维度。左图全零的*否认*行与右图全零的*替代*行把下述结构性发现可视化：框架级否认与主体替代主张不做任何维度级工程。

结构性发现值得单独一句：图 3 左板的*否认*行全空，右板的*替代*行亦然。在描述意义上且限于本语料：三篇 A1-否认作品无一携带任何维度码（显式或隐式均 0/3），而 A1-支持作品中为 16/18——否认在框架层运作，不在设计层。（这些对比的探索性列联表连同 Fisher 精确检验在分析报告中给出，未校正且不外推；我们刻意不在本文将其复述为推断性证据，因为目的性抽样不支持任何总体推断。）

### 5.3 主要结果：一条未被命名的轴

> **表 3.** 拟合对象维度：显式（E）、隐式（I）、缺席（−）处理的频次。

| 维度 | E | I | − | %E | %E 或 I |
|---|---|---|---|---|---|
| D1 作品存量 | 6 | 16 | 58 | 7.5% | 27.5% |
| **D2 实践流量** | **2** | 7 | 71 | **2.5%** | 11.2% |
| D3 价值—偏好 | 9 | 1 | 70 | 11.2% | 12.5% |
| D4 功能性情绪—动机 | 3 | 0 | 77 | 3.8% | 3.8% |
| D5 失败经验 | 8 | 1 | 71 | 10.0% | 11.2% |
| D6 人群/文化（谁） | 4 | 4 | 72 | 5.0% | 10.0% |
| D7 输出分布覆盖 | 3 | 4 | 73 | 3.8% | 8.8% |
| **D8 经验类型谱** | **0** | **9** | 71 | **0.0%** | **11.2%** |

**D8-explicit = 0/80（0.0%）**，精确二项（Clopper–Pearson）95% CI [0.0%, 4.5%]，三倍法则（rule of three）上界 ≈ 3.8%。该结果对置信度不敏感：剔除全部 8 篇低置信度作品后，D8-E = 0/72，CI [0.0%, 5.0%]。与零同样重要的是对照模态：**D8-implicit = 9/80**——失败数据工作（LEMA [56]、PRM800K [57]、SPAR [58]、ETO [59]、UltraInteract [60]、DeepSeek-V4.1 [51]、MiMo [52]、GLM-5 [53]）与蜂群研究 [36] 各自只触及类型空间的单一格（只有失败，或只有均值）；无一命名或操作化经验类型为覆盖轴。发现因此得以精确陈述：**话题被触及；轴从未被命名。** 这是理论第三覆盖轴主张的可计数形式。

**缺席检索程序。** 零计数的力度，至多与其背后检索的力度相当。我们运行了注册式缺席检索（8 个查询族，横跨 arXiv 全历史、ACL Anthology 域内检索与中文网络检索；日志见附录 A）：全部命中按 D8-E 判据筛选（经验类型维度*被命名为*覆盖/抽样轴，*且*被用于设计数据、实验或指标）。零篇通过；八个近似命中族连同理由被记录。最接近命中的案例具有教益：智能体经验基准把"经验"当作智能体自身先前情节（时间性，非类型性）；数据配比研究路线优化域权重；而最近的一对——两篇 2026 年工作把*机器 rollout 中模型错误的多样性*塑造为探索/RL 信号 [61, 62]。后一对表明第三轴正从机器一侧被逼近，而人类数据一侧仍为零；我们的主张因此限定于"作为人类实践数据上的覆盖轴"，并将随着该轴被操作化而遭证伪。图 2 展示合并结果：显式板中空缺的 D8 行，与右板实际的九个隐式点形成对照——轴被触及，从未被命名。

### 5.4 时间模式

> **表 4.** 按年份分层的显式处理（附 D8 隐式对照）。

| 维度 × 模态 | ≤2019 | 2020–2023 | 2024–2026 | 合计 |
|---|---|---|---|---|
| D1 显式 | 0 | 2 | 4 | 6 |
| D2 显式 | 0 | 0 | **2** | 2 |
| D7 显式 | 0 | 0 | 3 | 3 |
| **D8 显式** | **0** | **0** | **0** | **0** |
| D8 隐式 | 0 | 1 | 8 | 9 |

三行对照叙述了理论本身。作品即存量是*成熟*纲领：D1-E 作品 2022–2026 连续出现（数据墙分析 [1]、配比优化 [63, 64]、旗舰语料设计 [2, 65]）。输出分布覆盖是*正在抵达*的自觉：D7-E 首现于 2024 年 [3] 并获巩固 [36, 55]。经验类型轴是*缺失*的第三轴：每个分层均为 0。实践即流量是*新芽而非建制*：D2-E = 2/80，均来自 2026 年——DeepSeek 的员工失败提交流（"we collect negative feedback and model failure cases submitted by internal employees at scale" [51]）与同期存量/流量工程文章 [37]。我们强调措辞：两篇作品构成的是一个开端，而非一个趋势。

来自地图的两点限定。其一，WEIRD 悖论单元 [66]：提高训练数据的文化代表性可能*放大*歧视性观点的复现——代表*谁*不修复*什么*。覆盖问题因此是"两轴已知而未解"，不是"两轴已解"——这正是第三轴进入的空间。其二，一个探索性结构观察（描述性，仅限语料内）：显式维度工程集中于 A1-na 作品（至少有一个显式维度者 23 篇，A1-支持作品中为 9 篇）。结合 §5.2 的空否认行，模式是解耦：辩论 AI 是否拟合人类的人大多不做覆盖工程，做覆盖工程的人大多不辩论它。这一解耦是 §1 所述缺口——缺失的连接命题——的定量足迹。

### 5.5 证据地图的局限

持怀疑态度的审稿人也应当能够接受这些限度。(i) **无总体推断**：语料为带配额分层的目的性抽样；一切断言都是"本语料内"。(ii) **单一编码者**：κ 重编码已排期（2026-10-29），目前尚不可得；缓解措施是公开的编码手册、强制的引文锚点与公开的边界案例日志。(iii) **严格饱和未达**：语料填满至 80 篇上限并报告缺口。(iv) **缺席断言受程序约束**：0/80 加 8 查询缺席检索在其窗口内（2026-10-15 关闭）有力，但非永恒。(v) **核心断言与置信度无关**（§5.3 敏感性分析），但 8 个单元仍为低置信度、留待核验。(vi) 地图约束的是*描述性*断言；第 4 节的*规范性*立场是论证的选择，不是地图结果。

### 5.6 同期工作与整合划界

两篇同期工作被标记并划界（隔离优先权断言是一项诚实要求，不是形式主义）。**Gharbi 的 SSRN 文章** [37] 以显式的存量/流量工程框架分析数据墙的九条逃生路线，并识别出数据墙之后的"验证者墙"——与我们的时间性条款最接近的已发表表述。划界是锐利的：它是数据工程。它不含作品 vs 实践的本体区分，没有全谱 × 全程坐标系，没有覆盖轴，没有工具定位；它的流量是供应链，不是拟合对象。其 D1-E/D2-E 编码在专门的单元行补充（S1）中报告，不计入理论的缺口断言。**Fenoglio 的非对称交流文章** [67] 论证 LLM 输出在承诺不对称之下于人类实践中获得意义——一个意义侧理论，没有拟合纲领、没有增强定位、没有坐标系。两篇同期工作都未主张时间性条款的三要素组合（实践而非作品 + 全谱 × 全程 + 存量有墙/流量无墙）；截至窗口关闭，该组合的优先权仍归本文。

> **表 5.** 本理论与相邻框架。

| 框架 | 提供 | 缺失（本理论所补） |
|---|---|---|
| 文化技术 [6, 22] | 描述性分类：LLM 继承人类符号结构 | 时间性区分（作品 vs 实践）；覆盖轴；数据方法论后果 |
| 批判现象学（镜子） [7] | 警告：扭曲的反射重塑人类自我理解 | 忠实拟合的建设性说明；全谱/全程坐标；边界条件 |
| 增强经济学 [8, 40, 41] | 规范目标：互补优先于替代；设计点（控制 × 自动化） | 拟合本体论（为何模仿作为*手段*不同于作为*目的*）；终止边界 |
| 存量/流量数据工程 [37]（同期） | 供给侧分析：逃生路线、验证者墙 | 实践本体论；第三覆盖轴；工具定位 |

## 6. 张力与边界

理论的第四层处理：拟合在哪里自我绷紧，又在哪里停止。

**价值多元主义：谁的谱？** 全谱在是"什么"问题之前先是"谁"问题。对齐文献早已认识到，价值拟合未定谁的价值 [9]；多元对齐路线图把多元性跨人群操作化 [68]；社会选择批判表明，偏好聚合内嵌有争议的规范承诺（对异质反馈的功利主义 vs 最小最大化（leximin）聚合） [69]；聚合问题分析编目其失败模式 [70]；约 1,000 名（美国）参与者的集体宪法实验同时证明了当下集体过程的可行性与*地理窄化* [71]。谱轴不消解这一张力——它继承之。全谱拟合仍需一个聚合决定，这正是第 7 节将治理单列一问的原因。

**主体性边界：永不人格化，永不拟合现象状态。** 语料中最尖锐的现实冲突富有教益。Anthropic 的模型福祉计划追问模型是否可能值得道德考量 [72]；Suleyman 2026 年 9 月的言论公开拒绝该路线：AI 应是可亲的（personable）工具——有个性——但绝不授予人格地位 [46]。我们把此读作对立阵营之间的一次意外结盟，并基于独立理由持有该立场：永不授予人格地位与永不拟合现象状态，是同一枚边界硬币的两面。拟合目标包括功能性情绪—动机结构——而因果功能性情绪概念的可解释性证据 [26] 确认这一层*正在*被拟合——但理论的边界恰好落在功能层：对感受经验，理论不作断言——既不做出、不予许可，亦无此需要。镜子批判 [7] 提供互补的警告：被拟合之镜的危险不在于它感受，而在于它的反射重构人类对自身的理解。

**中国脉络：一条没有主体性语言的平行线。** 官方中国 AI 治理谱系从 2019 年治理原则（负责任 AI 的"以人为本"发展） [73]，经 2023 年全球人工智能治理倡议 [74]，到 2025 年国务院"人工智能+"行动意见 [75]——一部充满*赋能*与*人机协同*词汇、不含主体性归因的政策文本语料。古典根源以罕见的简洁契合工具立场：庄子的"物物而不物于物" [76] 在工具范畴辩论之前二十三个世纪就陈述了掌握条件——使用工具，而不被工具使用。在我们的语料内，儒家角色伦理单元读作对朴素纯工具解读的一次内部矫正（护理机器人无法履行孝式义务），记录于地图注记而不作过度解读。

**四条终止边界。** 时间性条款止于其术语止步之处；理论显式划定四条边界。

- **B1——实践主体的终结。** 流量随生命再生；最后一次实践之后，拟合无对象。（一条生存性边界，不是工程边界。）
- **B2——拟合者越界。** 若拟合者超越每一位教师——称之为 ASI——拟合关系便自行耗尽：已不存在不落在它身后的人类实践可供拟合。本理论关乎作为以人为参照概念的 AGI，在此边界之外刻意沉默，仅作标记。
- **B3——制度边界。** 法律、隐私与知情同意约束可采集之物；第 4 节的规范性立场还反向定义了对流量的取用权——工具立场不仅约束 AI 为何而造，也约束它可以取走什么。（上文多元主义张力即生活在此边界之内。）
- **B4——自指性污染。** 一旦 AGI 织入日常，被采集的实践已被 AGI 染色：拟合目标被拟合这一行为本身改变——镜子进入了它所反射的房间。这是模型坍塌在流量体制下的新形态 [3]：不是静态存量上的递归，而是活流的污染。缓解是工程而非禁止：原生与 AI 中介实践的分层出处标注（留待未来工作的协议组件）。

**可证伪性。** 理论点名自己的证伪者。若流量侧被证明有一堵与存量墙同构的硬墙（例如一个击败持续学习的原则性下界），或若全谱拟合可证地在任意尺度坍塌为均值，时间性条款便弱化为一个启发式。若显式的经验类型覆盖在中性文献中频繁出现，第三轴缺口断言（0/80）失败。若实践流数据被证明无法以生产级质量建造，D2-E 计数（2/80）作为证据失败。这些被陈述出来，是为了让理论可以输。

## 7. 方法论蕴含

从理论到方法：对下面三个问题中的每一个，我们陈述问题、证据地图所显示的现状、以及答案的形态。完整协议留待未来工作。

**分布 = 全谱覆盖。** 在当前实践中，多样性以三种身份存在：作为回归变量（域权重优化 [63, 64]，及隐式多语言配额如 Llama 3 的 8% [2]）；作为局部启发式（十亿规模的人物设定（persona）条件化合成 [77]）；以及作为质量过滤的牺牲品（教育语料策展按约 92% 的比例弃置原始网络 [65]）。把覆盖作为显式后训练目标的转向——针对指令微调坍塌恢复分布覆盖 [55]——是正确类型的动作，但它覆盖的是*输出分布*轴；人群轴有自己的研究路线（多语言策展，如 65 语言指令集合 [78]）；经验类型轴则为 0/80（§5.3）。WEIRD 悖论 [66] 警告，朴素的人群配额会反噬（代表*谁* ≠ 修复*什么*），因此全谱覆盖必须整合各轴而非堆叠配额。我们刻意用"覆盖"，不用"配额"。

**生产 = 永续采集协议。** 流量侧需要一个组织装置，其先例可见：规模化的员工提交失败案例 [51]；智能体训练中的失败反思与错误保留实践 [52, 53]。协议组件在此定义、待未来工作细化：以失败案例为一等数据的采集协议；区分真失败与奖励作弊式伪失败的毒性清洗（审计论文的边界条件 [5]）；三段式记录结构（错误类型、根因、纠正）；以及针对任何合成增强的坍塌防护（真实数据掺混加生成侧多样性约束）。约束瓶颈不是采集而是*吸收*：实践每日再生而模型快照按周期更新——*拟合时差*——且智能体的稳定性—可塑性两难仍未解决 [79]。地图把吸收侧工作编码为 D2-隐式：其数据源（尚）未被规定为实践流。

**治理 = 多元聚合与制度。** 谁聚合谱、谁许可流、谁裁定失败：聚合工具箱横跨社会选择机制 [69]、多宪法过程 [71]、人物设定条件化生成 [77] 与主权本地模型；许可权直面出处权利在少数大出版商手中的集中；而验证者问题——谁认证一个失败是失败——是整个飞轮转动所依的轴承 [5, 37]。B4 的缓解（原生 vs AI 中介出处分层）同样是对数据基础设施的一项制度要求，而不仅仅是一种标注约定。

## 8. 结论

本文论证了一个三层论题：AGI 是一个以人类实践为参照系的哲学概念；其实现是对该实践的拟合——作品即存量是静态误读的成熟形态，实践即流量是正确解读的开端；其恰当位置是增强性工具，一个必须由制度持续防御的规范性选择。证据地图使理论的主张可计数：一个 80 篇作品的语料，其中经验类型覆盖轴从未被命名（0/80；95% CI [0.0%, 4.5%]），实践即流量仅在两篇作品中显式（均 2026 年），且立场与对象在文献中解耦——描述性、规范性与方法论文献各自成熟，未被那个需要三者兼备的命题所连接。理论的贡献就是那个命题、它的坐标系、它的边界与它点名的证伪者。

我们在理论开始之处结束，下面这句话区分了本领域的两种未来——积累档案直至高墙，或拟合再生中的实践：

> **拟合对象不是人类的作品，而是人类的实践——人类经验的全谱（横截面）与全程（纵截面）。存量有墙，流量无墙。**

流量是否被拟合好——跨全谱、沿全程、在四条边界之下、朝向增强——不是一个等待应验的预测，而是一个有待执行的纲领。其执行留待未来工作。

---

**数据与代码可用性。** 语料（corpus_v1，80 篇作品 × 24 个变量）、编码手册、缺席检索日志、全部表格 CSV、图（300 dpi）与单文件复现脚本（`analysis/coding_data.py`；seed 20261015）随论文仓库发布。配套审计论文的完整材料：DOI 10.5281/zenodo.23355929。

**AI 辅助披露。** 沿用配套审计论文的做法：文献检索、核验、编码与起草在作者监督与规则化协议（编码手册规则 R1–R5、CR1–CR6；核验日志见分析报告）之下借助 AI 完成；全部编码断言附逐字或设计锚点，单一编码者的局限在 §5.5 披露。

**利益冲突。** 无声明。

## 附录 A：缺席检索日志（2026-10-14 执行）

支撑 D8-explicit = 0/80 断言（§5.3）的注册式缺席检索：三个引擎（arXiv 全历史；ACL Anthology 域内检索；中文网络检索）上的八个查询族。筛选判据（两个合取项均需满足）：(i) 经验类型维度（成功/失败 × 专家/新手 × 典型/边缘）被命名为覆盖/抽样/分层轴；(ii) 该轴被用于设计数据、实验或指标。结果：**0 篇通过；八个近似命中族连同理由被记录**。代表性命中附可核验的标识符；包含全部命中的完整日志随仓库发布。

> **表 A1.** 缺席检索日志：八个查询族，0 个 D8-E 命中。

| # | 查询族（引擎） | 代表性命中与注册的近似命中理由 |
|---|---|---|
| Q1 | "success and failure" coverage training（arXiv） | 持续预训练合并（2511.02451）；用户编辑微调（NeurIPS 2025）。定性案例分析，无覆盖轴设计。 |
| Q2 | "expert" "novice" data mixture（arXiv） | SimInstruct（2508.04428）把专家—新手对话生成为*数据类型*，而非配比/覆盖轴；配比研究路线（2502.15950、2607.01104、2601.17858）优化域权重。 |
| Q3 | "experience type" coverage（arXiv） | AhaBench（智能体从先前情节学习）；VCR（AAAI 2025）。"经验"= 智能体自身情节（时间性），非类型谱——最接近命中的案例，逐条记录。 |
| Q4 | "error diversity" curriculum（arXiv） | DiVERT（2406.19356，EMNLP 2024）；GEC 数据加权。错误多样性用于干扰项生成/纠错，非拟合数据覆盖。 |
| Q5 | "typical" "edge" spectrum coverage（arXiv） | 自动驾驶边缘案例综述（2410.08491）；角落案例生成。典型到边缘为*场景测试*操作化，非人类实践拟合数据。 |
| Q6 | 中文网络：成功/失败案例比例；专家/新手覆盖 | LLM 训练数据综述（2411.07715）；数据瓶颈的新闻报道。唯一命题级命中是一个 T3 媒体源（仅动机层，按一手来源规则排除）。 |
| Q7 | success failure expert novice coverage data selection（ACL Anthology） | 数据选择研究路线（Albalak 2402.16827；ACL 2025；LESS）。以影响力/质量为轴；无经验类型轴。 |
| Q8 | "error diversity" / "failure diversity" training coverage（arXiv） | **D-FUSEr**（ICML 2026，PMLR 306）；**EDAS**（2605.17333）。两者都塑造*模型 rollout* 的错误分布（机器侧多样性作为探索/RL 信号），非人类经验类型覆盖——最重要的一对近似命中：第三轴正从机器侧被逼近，而人类数据一侧仍为零。 |

## 附录 B：补充材料 S1：同期工作编码行（Gharbi）

> **表 B1.** 补充材料 S1：同期存量/流量数据工程文章（按同期工作规则处理）的专门单元行编码记录，单独报告，不计入理论的缺口断言（§5.6）。

| 项目 | 内容 |
|---|---|
| 作品 | W-038：Gharbi（2026），SSRN 预印本 7479298（2026-09-17） |
| 编码 | A1 = na；A2 = na；D1 = E；D2 = E；D2-explicit = True；concurrent = True；置信度 = 中 |
| 划界 | 工程意义的存量/流量 ≠ 实践本体论：无作品 vs 实践区分、无全谱 × 全程框架、无覆盖轴、无工具定位 |

## 参考文献

*按首次引用顺序编号；机器可读的 BibTeX 文件 `references.bib` 随本文附上，条目顺序相同。*

1. Villalobos, P., Sevilla, J., Ho, L., Barrett, D., & Besiroglu, T. (2022). *Will we run out of data? Limits of LLM scaling based on projected dataset size sequences*. arXiv:2211.04325. (Epoch AI.)
2. Grattafiori, A., et al. (2024). *The Llama 3 herd of models*. arXiv:2407.21783. (Meta.)
3. Shumailov, A., et al. (2024). AI models collapse when trained on recursively generated data. *Nature*, 631. doi:10.1038/s41586-024-07566-y.
4. Arendt, H. (1958). *The Human Condition*. University of Chicago Press.
5. Yu, Y. (2026). *Success Provides Direction, Failure Provides Precision: A Structured Audit of Failure Data in LLM Training*. Zenodo. doi:10.5281/zenodo.23355929. (配套审计论文；排除在证据地图统计之外。)
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
17. Imeri, B. (2025). *The benefits of AI and the illusion of AGI* [self-archived essay]. ResearchGate. (收录边缘；低置信。)
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
37. Gharbi, M. (2026). *A model cannot be its own source of truth: Nine escape routes from the data wall, and the verifier wall behind them*. SSRN 7479298 (2026-09-17). (同期工作。)
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
58. SPAR (2026). *SPAR f26: Human-annotated agent failure traces*. sparai.org. (低置信单元。)
59. Song, Y., Yin, D., Yue, X., Huang, J., Li, S., & Lin, B. Y. C. (2024). *Trial and error: Exploration-based trajectory optimization for LLM agents* (ETO). arXiv:2403.02502.
60. Yuan, L., et al. (2024). Advancing LLM reasoning generalists with preference trees (UltraInteract). *ICML 2024*; arXiv:2404.02078.
61. Baek, D., Estornell, A., Zhang, Y., Taufiq, M. F., et al. (2026). D-FUSEr: Diverse failure, unified success via error-distribution shaping in LLM reasoning. *ICML 2026, PMLR* 306.
62. Liu, W., et al. (2026). *Leveraging error diversity in group rollouts for reinforcement learning* (EDAS). arXiv:2605.17333.
63. Xie, S. M., Santurkar, S., Ma, T., & Tsipras, P. (2023). DoReMi: Optimizing data mixtures speeds up language model pretraining. *NeurIPS 2023*; arXiv:2205.10434.
64. Ye, H., et al. (2024). *Data mixing laws: Optimizing data mixtures by scaling law for pretraining*. arXiv:2403.16952.
65. Penedo, G., et al. (2024). *The FineWeb datasets: Decanting the web for the finest text data at scale* (FineWeb / FineWeb-Edu). arXiv:2406.17557.
66. Zhou, K., Constantinides, M., & Quercia, D. (2025). Should LLMs be WEIRD? Exploring WEIRDness and human rights in large language models. *AIES 2025*; arXiv:2508.19269.
67. Fenoglio, E. (2026). *Asymmetric communication: Large language models and language games*. arXiv:2607.28137. (同期工作。)
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
