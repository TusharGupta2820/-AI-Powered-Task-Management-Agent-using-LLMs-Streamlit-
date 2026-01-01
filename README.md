# AI To-Do Manager Agent

An intelligent task management application that uses AI to automatically prioritize your tasks.

## Features

- Simple Streamlit-based UI
- Automatic task prioritization using AI
- Manual override for task priorities
- CRUD operations for tasks
- SQLite database for task storage
- Task statistics dashboard

## Requirements

- Python 3.7+
- OpenAI API key (optional, uses fallback if not provided)

## Setup Instructions

1. Clone or download this repository to your local machine

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Create a `.env` file in the project root directory and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```
   
   > **Note**: If you don't have an OpenAI API key, the application will use a keyword-based fallback for task prioritization.

6. Run the application:
   ```bash
   streamlit run main.py
   ```

## How to Use

1. Enter a task description in the input field
2. The AI will suggest a priority (Urgent or Normal)
3. You can manually override the priority if needed
4. Click "Add Task" to save
5. Use the action buttons to mark tasks as complete, change priority, edit, or delete tasks

## Project Structure

- `main.py`: Streamlit UI implementation
- `database.py`: SQLite database operations
- `ai_agent.py`: AI prioritization logic
- `requirements.txt`: Project dependencies
- `.env`: Environment variables (not included in the repository)

## Architecture

The application follows a modular design:

- **UI Layer**: Streamlit-based interface in `main.py`
- **Data Layer**: SQLite database operations in `database.py`
- **AI Layer**: Task prioritization logic in `ai_agent.py`

## Fallback Mechanism

If no OpenAI API key is provided, the application uses a keyword-based approach to determine task priority, checking for urgent keywords in the task description.

## License

This project is open source and available under the MIT License.