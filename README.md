
# 🎓 Student Support Agentic AI using FastMCP

This project is an AI-powered student support agent built using **FastMCP (Fast Modular Cognitive Processing)**. The goal is to assist students in navigating course content, answering academic queries, and automating routine support tasks using modular and agentic AI capabilities.

## 🚀 Features

- 🔍 Context-aware academic query answering
- 🧠 Modular agent-based architecture using Claude's FastMCP
- 📊 Dynamic course data handling via JSON datasets
- 💬 Prompt-optimized interactions with ChatGPT, Claude, and Gemini
- 🤖 Extensible pipeline for integrating new tools and workflows

## 📁 Project Structure

```
student\_support\_agent/
├── dataset/
│   └── mock\_course\_data.json   # Sample academic content for agent reference
├── main.py                     # Entry point for running the AI agent
├── LICENSE                     # MIT License
├── README.md                   # You're here
├── .gitignore
├── pyproject.toml              # Python project config
└── .python-version             # Python version specification

```

## ⚙️ Tech Stack

- **Claude FastMCP** for modular cognitive workflows
- **OpenAI GPT / ChatGPT** for natural language generation
- **Google Gemini** for enhanced research and academic support
- **Python 3.10+** as the core development language

## 📌 Use Cases

- Answering student doubts on course topics
- Recommending resources based on query context
- Automating repetitive student queries
- Providing summaries and explanations of difficult topics

## 🛠️ Installation

> This is a prototype, so the following steps assume a local development setup.


# Clone the repository
git clone https://github.com/PratikPorc/Student-Support-Agentic-AI-using-FastMCP.git
cd Student-Support-Agentic-AI-using-FastMCP

# (Optional) Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt  # or use pyproject.toml with poetry/pdm

# Run the agent
python main.py

## 🌐 Future Improvements

* Web interface for student interaction
* Real-time chat integration
* Multi-language academic support
* Integration with LMS (e.g., Moodle, Google Classroom)

## 📜 License

This project is licensed under the **MIT License** – see the [LICENSE](./LICENSE) file for details.

---

### 🤝 Contributions & Feedback

Contributions, ideas, or improvements are welcome! Feel free to open issues or submit pull requests.

---

