# -AI-Powered-Task-Management-Agent-using-LLMs-Streamlit-
An AI-powered task management system that helps users organize daily tasks intelligently.
The agent automatically prioritizes tasks (Urgent / Normal) using a Large Language Model and allows users to manage tasks through a simple Streamlit UI.

This project demonstrates Agentic AI behavior using perception, reasoning, and action.

🚀 What This Project Does

✔ Allows users to add, update, delete, and complete tasks
✔ Automatically assigns priority using AI reasoning
✔ Stores tasks persistently using SQLite
✔ Provides a clean and interactive Streamlit interface
✔ Demonstrates real-world use of AI agents (CRUD + reasoning)

🤖 Agentic AI Behavior

The AI To-Do Manager works like an intelligent agent:

1️⃣ Perception

Takes natural language task input from the user
Example:

“Submit internship report tomorrow morning”

2️⃣ Reasoning

Uses an LLM to analyze task urgency

Decides whether the task is Urgent or Normal

3️⃣ Action

Stores the task with priority in the database

Displays prioritized tasks in the UI

Allows users to update task status

🛠 Tech Stack

Python 3.10+

Streamlit – UI

SQLite – Database

LLM API (OpenAI / compatible) – Task prioritization

dotenv – Environment variable management

📁 Project Structure
ai-todo-manager-agent/
│
├── app.py              # Streamlit UI
├── database.py         # SQLite CRUD operations
├── ai_agent.py         # AI priority classification logic
├── requirements.txt    # Project dependencies
├── .env                # API keys (not committed)
├── todo.db             # SQLite database
└── README.md

📌 Features

✅ Add new tasks

✅ AI-based priority detection

✅ Manual priority override

✅ Update task status (Pending / Completed)

✅ Delete tasks

✅ Persistent storage with SQLite

🔑 Prerequisites

Python 3.10 or higher

LLM API key (OpenAI / compatible)

Git (optional)

⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/your-username/ai-todo-manager-agent.git
cd ai-todo-manager-agent

2️⃣ Create Virtual Environment
python -m venv venv


Activate it:

Windows

venv\Scripts\activate


Linux / Mac

source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Set Environment Variables

Create a .env file in the project root:

OPENAI_API_KEY=your_api_key_here


⚠️ Do not commit this file to GitHub

5️⃣ Run the Application
streamlit run app.py


Open in browser:

http://localhost:8501

🖥 Example Usage

User Input:

“Prepare slides for client meeting tomorrow morning”

AI Output:

Priority: Urgent

Status: Pending

Stored in database automatically

📦 Database Schema (SQLite)
Column	Type
id	INTEGER (Primary Key)
task	TEXT
priority	TEXT
status	TEXT
created_at	TIMESTAMP
🔮 Future Enhancements

🔔 Notifications & reminders

🎤 Voice input support

📊 Task analytics dashboard

🧠 Memory-based task suggestions

🐳 Docker deployment

☁️ Cloud database support

🎯 Why This Project Is Internship-Ready

✔ Uses real AI reasoning (not hardcoded rules)
✔ Demonstrates agent architecture
✔ Clean modular code
✔ Practical real-world use case
✔ Easy to extend and scale
