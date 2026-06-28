# 🤖 AI Career Mentor Agent

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-green?style=for-the-badge)
![Groq](https://img.shields.io/badge/Groq-LLM-orange?style=for-the-badge)
![Tavily](https://img.shields.io/badge/Tavily-Search-purple?style=for-the-badge)

**Your Personal AI-Powered Career Guide**
*Built by Kumar Basu Singh*

</div>

---

## 🌟 What Does This Agent Do?

**AI Career Mentor Agent** is an intelligent career guidance tool that helps anyone
who wants to break into the tech industry. You simply type your dream job role
and the agent does everything for you:

- 🔍 **Analyzes** the role deeply using AI
- 🛠️ **Identifies** the top 10 most important skills needed for that role
- 🌐 **Searches** real and official documentation links for every skill
- 🗺️ **Generates** a detailed, phase-wise, step-by-step learning roadmap
- 📄 **Creates** a beautifully formatted downloadable PDF of your roadmap

Whether you want to become a **Data Scientist**, **Full Stack Developer**,
**AI Engineer**, **DevOps Engineer**, or any other tech role — this agent
will guide you from zero to job-ready with a clear and structured path.

---

## ⚙️ How Does The Agent Work?

The agent is built using **LangGraph** — a framework for building agentic AI workflows.
It runs through **3 intelligent nodes** in a graph pipeline:
User enters Role
↓
┌─────────────────────┐
│  Node 1             │
│  Analyze Role       │  ← Groq LLM extracts top 10 skills
└─────────────────────┘
↓
┌─────────────────────┐
│  Node 2             │
│  Search Docs        │  ← Tavily searches official documentation links
└─────────────────────┘
↓
┌─────────────────────┐
│  Node 3             │
│  Generate Roadmap   │  ← Groq LLM generates full structured roadmap
└─────────────────────┘
↓
PDF Generated + Displayed on UI

### Node Details:

| Node | Tool Used | Job |
|------|-----------|-----|
| `analyze_role_node` | Groq LLM | Extracts top 10 skills for the given role |
| `search_docs_node` | Tavily API | Finds real official documentation links |
| `generate_roadmap_node` | Groq LLM | Generates full phase-wise roadmap |

---

## 🛠️ Tech Stack

### Language
| Technology | Purpose |
|------------|---------|
| ![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white) **Python 3.10+** | Core programming language |

### Frameworks & Libraries
| Technology | Purpose |
|------------|---------|
| **Streamlit** | Frontend UI framework |
| **LangGraph** | Agentic AI graph orchestration |
| **LangChain** | LLM integration and tooling |
| **LangChain-Groq** | Groq LLM integration |
| **LangChain-Community** | Community tools and loaders |
| **Pydantic** | Data validation |
| **ReportLab** | PDF generation |
| **Python-dotenv** | Environment variable management |

### AI & Search
| Technology | Purpose |
|------------|---------|
| **Groq** (llama-3.3-70b-versatile) | Fast LLM inference |
| **Tavily API** | Real-time web search for documentation |

---

## 📁 Project Architecture
AICareerMentorAgent/
│
├── 📄 app.py                    ← Main Streamlit UI application
├── 📄 requirements.txt          ← All Python dependencies
├── 📄 .env                      ← API keys (never push to GitHub)
├── 📄 .gitignore                ← Files to ignore in GitHub
├── 📄 README.md                 ← Project documentation
│
├── 📁 graph/                    ← LangGraph agent folder
│   ├── 📄 init.py           ← Makes graph a Python package
│   ├── 📄 state.py              ← State schema (TypedDict)
│   ├── 📄 nodes.py              ← All 3 agent node functions
│   └── 📄 builder.py            ← Graph builder and compiler
│
└── 📁 utils/                    ← Utility functions folder
├── 📄 init.py           ← Makes utils a Python package
└── 📄 pdf_generator.py      ← PDF generation logic

### File Responsibilities:

| File | Responsibility |
|------|---------------|
| `app.py` | Streamlit UI, user input, displays roadmap, download button |
| `graph/state.py` | Defines the data structure flowing through the graph |
| `graph/nodes.py` | Contains all 3 node functions with AI logic |
| `graph/builder.py` | Connects nodes with edges and compiles the graph |
| `utils/pdf_generator.py` | Creates branded, formatted PDF from roadmap |

---

## 📦 requirements.txt

```txt
streamlit
langchain
langchain-groq
langchain-community
langgraph
tavily-python
reportlab
python-dotenv
pydantic
```

---

## 🚀 Run From Zero To Final — Step By Step

### Step 1: Clone The Repository
```bash
git clone https://github.com/mr-basu-singh/AICareerMentorAgent.git
cd AICareerMentorAgent
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv
```

### Step 3: Activate Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

> ✅ You will see **(venv)** at the start of your terminal

### Step 4: Install All Dependencies
```bash
pip install -r requirements.txt
```

### Step 5: Create `.env` File
Create a file named `.env` in the root folder and add your API keys:
```env
GROQ_API_KEY=your_groq_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

#### Get Your API Keys:
- **Groq API Key** → https://console.groq.com
- **Tavily API Key** → https://app.tavily.com

### Step 6: Run The Application
```bash
streamlit run app.py
```

### Step 7: Open In Browser
http://localhost:8501

> 🎉 Your AI Career Mentor Agent is now running!

---

## 🔑 Environment Variables

| Variable | Description | Get From |
|----------|-------------|----------|
| `GROQ_API_KEY` | Groq LLM API key | https://console.groq.com |
| `TAVILY_API_KEY` | Tavily search API key | https://app.tavily.com |

---

## 👨‍💻 About The Author

<div align="center">

### Kumar Basu Singh

*AI & Machine Learning Engineer | LangChain & LangGraph Developer*

| Contact | Link |
|---------|------|
| 📧 Email | basueps@gmail.com |
| 💼 LinkedIn | https://www.linkedin.com/in/kumar-basu-singh/ |
| 🐙 GitHub | https://github.com/mr-basu-singh |

---

### 🚀 Open For Opportunities

✅ **Internship** — Looking for AI Agent Enginner internship opportunities

✅ **Full Time Job** — Open for AI Agent Engineer, GenAI Enginner, Agentic AI Developer

✅ **Freelancing** — Available for freelance AI and Python development projects

> 💬 *Feel free to reach out via email or LinkedIn for any opportunities!*

</div>

---

<div align="center">

**⭐ If you found this project helpful, please give it a star on GitHub! ⭐**

*Built  by Kumar Basu Singh*

</div>

Save the file then push to GitHub:
bashgit add .
git commit -m "Added detailed README.md"
git push origin main
