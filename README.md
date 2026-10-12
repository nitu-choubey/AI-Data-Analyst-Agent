# 🤖 AI-Powered Data Analyst Agent

An intelligent, interactive data analysis tool built with **Streamlit**, **Pandas**, and **SQLite**. This agent allows users to ask questions about their sales data in plain English, automatically converts them into SQL queries, executes them against a database, and displays dynamic insights and charts.

## 🚀 Features
* **Natural Language to SQL:** Translate everyday English questions into structured SQLite queries.
* **Automated Data Analysis:** Instantly queries the SQLite database (`sales.db`) and processes results using Pandas.
* **Interactive Dashboard:** Built with Streamlit for a clean, user-friendly web interface.
* **Dynamic Visualizations:** Automatically generates charts and data tables based on query results.

## 🛠️ Tech Stack
* **Frontend/UI:** Streamlit
* **Data Manipulation:** Pandas
* **Database:** SQLite
* **Language:** Python

## 📂 Project Structure
```text
AI-Data-Analyst-Agent/
│
├── app.py                # Main Streamlit web application interface
├── ai_sql_agent.py       # Core logic for handling natural language / SQL generation
├── database_engine.py    # Database connection and query execution helper
├── setup_database.py     # Script to initialize and populate the SQLite database
├── sales.db              # SQLite database containing sales and product records
└── .gitignore            # Files and directories to ignore by Git

⚙️ How to Run Locally
1.Clone the repository:
git clone [https://github.com/nitu-choubey/AI-Data-Analyst-Agent.git](https://github.com/nitu-choubey/AI-Data-Analyst-Agent.git)
cd AI-Data-Analyst-Agent

2.Install dependencies:
pip install streamlit pandas

3.Run the Streamlit app:
streamlit run app.py
