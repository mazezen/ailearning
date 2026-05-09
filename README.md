# AI Learning

**目标**：从零基础到能够独立开发大模型应用、智能体（Agent）和 RAG 系统，并具备模型微调、部署优化能力。

---

## 阶段 0：前置基础

### 0.1 数学基础

- 线性代数：向量、矩阵运算、特征值、特征向量
- 概率与统计：分布、期望、方差、贝叶斯定理
- 微积分：导数、偏导、梯度、链式法则
- **推荐资源**：
  - 3Blue1Brown 《线性代数本质》《概率》系列
  - Khan Academy

### 0.2 机器学习基础

- 监督学习、无监督学习、回归、分类
- 决策树、随机森林、SVM、KNN
- 模型评估（Accuracy、Precision、Recall、F1、ROC、过拟合、正则化）
- **工具**：Scikit-learn
- **推荐**：Andrew Ng《Machine Learning》或李宏毅《机器学习》202X版

### 0.3 深度学习基础

- 神经网络、前向传播、反向传播
- 激活函数、损失函数、优化器（SGD、Adam）
- CNN、RNN、LSTM 基础
- **框架**：**PyTorch**（强烈推荐）
- **推荐**：Karpathy《Neural Networks: Zero to Hero》、动手学深度学习

---

## 阶段 1：Python 编程

### 1.1 Python 编程

- 基础语法、数据结构
- 函数、装饰器、生成器
- 文件 I/O、异常处理
- 面向对象编程
- 高阶语法（迭代器、上下文管理器、元编程）
- 网络编程（requests、FastAPI 基础）
- 多任务编程（threading、multiprocessing、asyncio）
- 虚拟环境、Git、调试、单元测试

**推荐资源**

- https://www.python.org/
- https://www.runoob.com/python3/python3-tutorial.html

---

## 阶段 2: 数据处理与统计分析

### 2.1 数据存储

- **SQL**（基础 + 窗口函数、CTE、性能优化）
  - SQL
  - SQLite

### 2.2 数据统计分析

- **NumPy**：Ndarray、广播机制、矩阵运算
- **Pandas**：Series、DataFrame、数据清洗、聚合、分组、合并
- **数据可视化**：Matplotlib + Seaborn + Plotly

**推荐资源**

- https://www.runoob.com/sql/sql-tutorial.html

- https://sqlite.org/

- https://www.runoob.com/sqlite/sqlite-tutorial.html

---

## 阶段 3：大模型应用开发基础

### 3.1 大模型基本概念

- Tokenization、Embedding、Context Window
- Transformer 初步理解（Attention 机制）
- 主流模型家族（GPT、LLaMA、Qwen、Mistral、Gemma 等）

### 3.2 使用 LLM API

- OpenAI、Anthropic、Groq、DeepSeek、硅基流动、通义千问等
- 流式输出、结构化输出（JSON Mode）、函数调用（Tool Calling）
- 成本控制与 Token 管理

### 3.3 Prompt Engineering

- Zero-shot、Few-shot、Chain-of-Thought (CoT)
- ReAct、Tree-of-Thought、自一致性
- Prompt 优化技巧与迭代方法
- **推荐**：LearnPrompting.org + 日常大量实验

### 3.4 Hugging Face 实战

- `transformers` 库、pipeline
- 模型下载、推理、本地部署
- Datasets 库与模型 Hub

---

## 阶段 4：Transformer 模型详解（核心模块）

- Scaled Dot-Product Attention 与 Multi-Head Attention
- Positional Encoding、LayerNorm、Residual Connection
- Encoder-Decoder、Decoder-only、Encoder-only 架构对比
- 预训练目标：Next Token Prediction、Masked LM
- 经典模型解读（BERT、GPT 系列、LLaMA、Qwen2、Mistral）
- 从零实现小型 Transformer（推荐 NanoGPT 或 Karpathy 教程）
- **推荐资源**：
  - 《The Annotated Transformer》
  - Hugging Face LLM Course
  - Andrej Karpathy 相关视频

---

## 阶段 5：大模型智能体与 RAG（核心实战）

### 5.1 RAG（Retrieval-Augmented Generation）

- **基础**：Chunking 策略、Embedding 模型、Vector Database（Chroma、FAISS、PGVector、Weaviate）
- **进阶**：
  - Query 改写（HyDE、Rewrite-Retrieve-Read）
  - Reranking、Metadata 过滤
  - Parent-Document、Hypothetical Questions
  - Corrective RAG、Self-RAG、多模态 RAG
- **评估**：RAGAS、ARES、TruLens

### 5.2 LangChain 生态

- LangChain 核心概念与模块
- **LangGraph**：构建复杂 Agent 工作流（状态机）
- **LangSmith**：调试、追踪、评估
- **LlamaIndex**（RAG 专用，建议同时掌握）

### 5.3 Agent 开发

- Tool Calling / Function Calling
- ReAct、Plan-and-Execute、Multi-Agent
- 记忆机制（短期记忆、长期记忆、向量记忆）
- **推荐框架**：LangGraph、CrewAI、AutoGen

---

## 阶段 6：模型评估、优化与部署

### 6.1 系统评估

- 传统指标 + LLM-as-Judge（G-Eval）
- MT-Bench、Arena Elo、Human Evaluation
- 安全性、幻觉、偏见评估

### 6.2 模型优化

- **量化**：INT8、INT4、GPTQ、AWQ、BitsAndBytes
- **高效微调**：LoRA、QLoRA、DoRA、PEFT
- **推理加速**：vLLM、TensorRT-LLM、Ollama、LM Studio
- **知识蒸馏**: Speculative Decoding

### 6.3 部署与 MLOps / LLMOps

- FastAPI + vLLM 部署
- Docker、Kubernetes 基础
- 实验追踪（Weights & Biases、MLflow）
- 监控（LangSmith、Phoenix、Prometheus）
- 成本优化与 Scaling

---

## 阶段 7：项目实战与案例集合（持续进行）

1. **RAG 智能问答系统**（企业知识库）
2. **多工具智能体**（自动化研究、数据分析）
3. **垂直领域模型微调**（中文 + 特定行业）
4. **多模态应用**（LLaVA、GPT-4o 类）
5. **本地完整应用**（Ollama + LangGraph + Web UI）
6. **生产级项目**（带评估、监控、用户反馈闭环）
7. **开源贡献或个人作品集**（GitHub）

**推荐技术栈组合**：

- 后端：FastAPI + LangGraph
- 向量库：PGVector / Chroma
- 推理：vLLM / Ollama
- 前端：Streamlit / Gradio / Next.js
