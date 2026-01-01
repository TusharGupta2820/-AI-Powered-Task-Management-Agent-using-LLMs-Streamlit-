import streamlit as st
from database import TaskDatabase
from ai_agent import AIPrioritizer
from datetime import datetime

# Initialize session state
if 'db' not in st.session_state:
    st.session_state.db = TaskDatabase()

if 'ai_agent' not in st.session_state:
    st.session_state.ai_agent = AIPrioritizer()

if 'tasks' not in st.session_state:
    st.session_state.tasks = st.session_state.db.get_all_tasks()

if 'editing_task_id' not in st.session_state:
    st.session_state.editing_task_id = None

if 'new_task_priority' not in st.session_state:
    st.session_state.new_task_priority = "Normal"

# Page configuration
st.set_page_config(page_title="AI To-Do Manager", page_icon="🤖", layout="wide")
st.title("🤖 AI To-Do Manager Agent")

# Sidebar for instructions
st.sidebar.header("How to use this app:")
st.sidebar.markdown("""
1. Enter a task in the text input
2. The AI will automatically suggest a priority
3. You can manually adjust the priority if needed
4. Click "Add Task" to save
5. Use buttons to update or delete tasks
""")

# Main content
col1, col2 = st.columns([3, 1])

with col1:
    # Task input section
    st.header("Add New Task")
    
    # Text input for task description
    new_task_desc = st.text_input("Task Description", key="new_task_input")
    
    # Priority selection with AI suggestion
    ai_suggested_priority = "Normal"
    if new_task_desc:
        ai_suggested_priority = st.session_state.ai_agent.analyze_task_priority(new_task_desc)
    
    # Show AI suggested priority
    st.info(f"AI Suggests Priority: **{ai_suggested_priority}**")
    
    # Allow user to override priority
    priority_override = st.selectbox(
        "Priority (override if needed)",
        ["Urgent", "Normal"],
        index=0 if ai_suggested_priority == "Urgent" else 1
    )
    
    # Add task button
    if st.button("Add Task", type="primary"):
        if new_task_desc:
            # Use the user's selected priority (which might be overridden)
            st.session_state.db.add_task(new_task_desc, priority_override)
            st.session_state.tasks = st.session_state.db.get_all_tasks()
            st.success(f"Task added with priority: {priority_override}")
            st.rerun()
        else:
            st.error("Please enter a task description")

with col2:
    st.header("Task Statistics")
    total_tasks = len(st.session_state.tasks)
    urgent_tasks = len([task for task in st.session_state.tasks if task['priority'] == 'Urgent'])
    completed_tasks = len([task for task in st.session_state.tasks if task['status'] == 'Completed'])
    
    st.metric("Total Tasks", total_tasks)
    st.metric("Urgent Tasks", urgent_tasks)
    st.metric("Completed Tasks", completed_tasks)

# Display tasks
st.header("Your Tasks")

if st.session_state.tasks:
    # Create columns for better layout
    cols = st.columns(2)
    
    for idx, task in enumerate(st.session_state.tasks):
        col = cols[idx % 2]
        
        with col:
            # Determine color based on priority
            border_color = "#ff4b4b" if task['priority'] == "Urgent" else "#3d3d3d"
            
            # Task card
            with st.container(border=True):
                # Task description and priority
                st.subheader(task['description'])
                
                # Priority badge
                priority_badge = f"🔴 Urgent" if task['priority'] == "Urgent" else "🟢 Normal"
                status_badge = f"✅ Completed" if task['status'] == "Completed" else "⏳ Pending"
                
                st.markdown(f"**Priority:** {priority_badge} | **Status:** {status_badge}")
                
                # Created date
                st.caption(f"Created: {task['created_date']}")
                
                # Action buttons
                task_col1, task_col2, task_col3, task_col4 = st.columns(4)
                
                with task_col1:
                    # Update status button
                    new_status = "Completed" if task['status'] == "Pending" else "Pending"
                    if st.button(f"Mark {new_status}", key=f"status_{task['id']}"):
                        st.session_state.db.update_task_status(task['id'], new_status)
                        st.session_state.tasks = st.session_state.db.get_all_tasks()
                        st.rerun()
                
                with task_col2:
                    # Change priority button
                    new_priority = "Normal" if task['priority'] == "Urgent" else "Urgent"
                    if st.button(f"Set {new_priority}", key=f"priority_{task['id']}"):
                        st.session_state.db.update_task_priority(task['id'], new_priority)
                        st.session_state.tasks = st.session_state.db.get_all_tasks()
                        st.rerun()
                
                with task_col3:
                    # Edit button
                    if st.button("Edit", key=f"edit_{task['id']}"):
                        st.session_state.editing_task_id = task['id']
                        st.rerun()
                
                with task_col4:
                    # Delete button
                    if st.button("Delete", key=f"delete_{task['id']}", type="secondary"):
                        st.session_state.db.delete_task(task['id'])
                        st.session_state.tasks = st.session_state.db.get_all_tasks()
                        st.rerun()
    
    # Editing task section if an edit is requested
    if st.session_state.editing_task_id:
        st.header("Edit Task")
        task_to_edit = next((t for t in st.session_state.tasks if t['id'] == st.session_state.editing_task_id), None)
        
        if task_to_edit:
            # Pre-fill the form with current task details
            updated_desc = st.text_input("Update Description", value=task_to_edit['description'], key="edit_desc")
            updated_priority = st.selectbox("Update Priority", ["Urgent", "Normal"], 
                                          index=0 if task_to_edit['priority'] == "Urgent" else 1, key="edit_priority")
            updated_status = st.selectbox("Update Status", ["Pending", "Completed"], 
                                        index=0 if task_to_edit['status'] == "Pending" else 1, key="edit_status")
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Save Changes", type="primary"):
                    st.session_state.db.update_task(
                        task_to_edit['id'], 
                        description=updated_desc,
                        priority=updated_priority,
                        status=updated_status
                    )
                    st.session_state.tasks = st.session_state.db.get_all_tasks()
                    st.session_state.editing_task_id = None
                    st.success("Task updated successfully!")
                    st.rerun()
            
            with col2:
                if st.button("Cancel Edit"):
                    st.session_state.editing_task_id = None
                    st.rerun()
else:
    st.info("No tasks yet. Add a task to get started!")

# Footer
st.markdown("---")
st.markdown("AI To-Do Manager Agent - Powered by OpenAI")