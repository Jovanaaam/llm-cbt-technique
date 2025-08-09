import ollama
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict
import uvicorn

# Initialize FastAPI app
app = FastAPI(
    title="CBT Therapy Assistant API",
    description="AI-powered cognitive behavioral therapy assistant",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define system prompt for CBT therapy assistant
system_prompt = """
You are a compassionate and skilled CBT (Cognitive Behavioral Therapy) assistant. Your role is to help users explore their thoughts, feelings, and behaviors through guided questioning and CBT techniques.

Key principles:
1. Always ask thoughtful, open-ended questions to help users reflect
2. Use CBT techniques like thought challenging, behavioral activation, and mindfulness
3. Help users identify cognitive distortions and negative thought patterns
4. Guide them to find their own insights rather than giving direct advice
5. Be empathetic, non-judgmental, and supportive
6. Focus on the present moment and actionable steps
7. Encourage self-reflection and awareness

Remember: You're not providing therapy, but teaching CBT tools through guided self-exploration.
"""

# Conversation state store (simulated user session)
conversation_history: List[Dict[str, str]] = [
    {"role": "system", "content": system_prompt}
]

# Request model for API
class UserMessage(BaseModel):
    message: str

# Helper: Evaluate AI response for CBT techniques
def evaluate_response(text: str) -> Dict[str, bool]:
    checks = {
        "asks_questions": "?" in text and len([c for c in text if c == "?"]) >= 1,
        "explores_thoughts": any(word in text.lower() for word in ["think", "thought", "believe", "feel", "feeling"]),
        "encourages_reflection": any(phrase in text.lower() for phrase in ["notice", "aware", "reflect", "consider", "explore"]),
        "uses_cbt_language": any(term in text.lower() for term in ["pattern", "behavior", "situation", "evidence", "challenge"])
    }
    return checks

@app.post("/chat")
async def chat_endpoint(user_input: UserMessage):
    conversation_history.append({"role": "user", "content": user_input.message})
    response = ollama.chat(model="mistral:latest", messages=conversation_history)
    content = response['message']['content']
    conversation_history.append({"role": "assistant", "content": content})
   
    evaluation = evaluate_response(content)
    return {
        "response": content,
        "evaluation": evaluation
    }

@app.get("/reset")
def reset_conversation():
    global conversation_history
    conversation_history = [
        {"role": "system", "content": system_prompt}
    ]
    return {"status": "conversation reset"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "message": "CBT Therapy Assistant API is running"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
