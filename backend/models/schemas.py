from pydantic import BaseModel
from typing import List, Dict, Optional
from datetime import datetime

class UserMessage(BaseModel):
    message: str

class ConversationMessage(BaseModel):
    role: str  # "user", "assistant", or "system"
    content: str
    timestamp: Optional[datetime] = None

class CBTEvaluation(BaseModel):
    asks_questions: bool
    explores_thoughts: bool
    encourages_reflection: bool
    uses_cbt_language: bool

class ChatResponse(BaseModel):
    response: str
    evaluation: CBTEvaluation
    timestamp: datetime

class ResetResponse(BaseModel):
    status: str
    message: str

class HealthResponse(BaseModel):
    status: str
    message: str 