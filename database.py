import sqlite3
from datetime import datetime
from typing import List, Dict, Optional

class TaskDatabase:
    def __init__(self, db_path: str = "tasks.db"):
        self.db_path = db_path
        self.init_db()
    
    def init_db(self):
        """Initialize the database with tasks table"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT NOT NULL,
                priority TEXT NOT NULL,
                created_date TEXT NOT NULL,
                status TEXT NOT NULL
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def add_task(self, description: str, priority: str = "Normal", status: str = "Pending") -> int:
        """Add a new task to the database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        created_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        cursor.execute('''
            INSERT INTO tasks (description, priority, created_date, status)
            VALUES (?, ?, ?, ?)
        ''', (description, priority, created_date, status))
        
        task_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        return task_id
    
    def get_all_tasks(self) -> List[Dict]:
        """Retrieve all tasks from the database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('SELECT id, description, priority, created_date, status FROM tasks ORDER BY created_date DESC')
        rows = cursor.fetchall()
        
        tasks = []
        for row in rows:
            task = {
                'id': row[0],
                'description': row[1],
                'priority': row[2],
                'created_date': row[3],
                'status': row[4]
            }
            tasks.append(task)
        
        conn.close()
        return tasks
    
    def get_task_by_id(self, task_id: int) -> Optional[Dict]:
        """Retrieve a specific task by ID"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT id, description, priority, created_date, status
            FROM tasks WHERE id = ?
        ''', (task_id,))
        
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return {
                'id': row[0],
                'description': row[1],
                'priority': row[2],
                'created_date': row[3],
                'status': row[4]
            }
        return None
    
    def update_task(self, task_id: int, description: str = None, priority: str = None, status: str = None):
        """Update a task in the database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Build the update query dynamically based on provided fields
        updates = []
        params = []
        
        if description is not None:
            updates.append("description = ?")
            params.append(description)
        
        if priority is not None:
            updates.append("priority = ?")
            params.append(priority)
        
        if status is not None:
            updates.append("status = ?")
            params.append(status)
        
        if updates:
            query = f"UPDATE tasks SET {', '.join(updates)} WHERE id = ?"
            params.append(task_id)
            
            cursor.execute(query, params)
            conn.commit()
        
        conn.close()
    
    def delete_task(self, task_id: int):
        """Delete a task from the database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
        conn.commit()
        conn.close()
    
    def update_task_priority(self, task_id: int, priority: str):
        """Update the priority of a specific task"""
        self.update_task(task_id, priority=priority)
    
    def update_task_status(self, task_id: int, status: str):
        """Update the status of a specific task"""
        self.update_task(task_id, status=status)