import openai
from typing import Optional
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class AIPrioritizer:
    def __init__(self):
        # Initialize OpenAI API key from environment variable
        self.api_key = os.getenv("OPENAI_API_KEY")
        if self.api_key:
            openai.api_key = self.api_key
        else:
            # If no API key is provided, we'll use a mock implementation
            print("Warning: No OPENAI_API_KEY found. Using mock AI prioritization.")
    
    def analyze_task_priority(self, task_description: str) -> str:
        """
        Analyze the task description and return priority (Urgent/Normal)
        Uses OpenAI API if available, otherwise uses a simple keyword-based approach
        """
        if self.api_key:
            return self._analyze_with_openai(task_description)
        else:
            return self._analyze_with_keywords(task_description)
    
    def _analyze_with_openai(self, task_description: str) -> str:
        """
        Analyze task priority using OpenAI API
        """
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system", 
                        "content": "You are an AI assistant that analyzes tasks and determines their priority. Respond with only 'Urgent' or 'Normal'."
                    },
                    {
                        "role": "user",
                        "content": f"Analyze this task: '{task_description}'. Determine if it is Urgent or Normal priority. Respond with only one word: Urgent or Normal."
                    }
                ],
                max_tokens=10,
                temperature=0.1
            )
            
            priority = response.choices[0].message.content.strip()
            
            # Validate the response
            if priority.lower() in ["urgent", "normal"]:
                return priority.capitalize()
            else:
                # Fallback to keyword analysis if API returns unexpected result
                return self._analyze_with_keywords(task_description)
                
        except Exception as e:
            print(f"Error calling OpenAI API: {e}")
            # Fallback to keyword analysis if API fails
            return self._analyze_with_keywords(task_description)
    
    def _analyze_with_keywords(self, task_description: str) -> str:
        """
        Simple keyword-based priority analysis as fallback
        """
        task_lower = task_description.lower()
        
        urgent_keywords = [
            "urgent", "asap", "immediately", "emergency", "critical", 
            "today", "now", "deadline", "crucial", "important", 
            "meeting", "due", "expire", "cancel", "call", "response"
        ]
        
        # Check for urgent keywords
        for keyword in urgent_keywords:
            if keyword in task_lower:
                return "Urgent"
        
        # Default to Normal if no urgent indicators
        return "Normal"