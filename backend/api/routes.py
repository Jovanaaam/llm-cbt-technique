from fastapi import APIRouter, HTTPException
from backend.models.schemas import UserMessage, ChatResponse, ResetResponse, HealthResponse, CBTEvaluation
from backend.services.ai_service import AIService
from datetime import datetime

# Create router
router = APIRouter()

# Initialize AI service (in production, this would be dependency injected)
ai_service = AIService()

@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(user_input: UserMessage):
    """Chat with the CBT therapy assistant"""
    try:
        # Get AI response
        ai_response = await ai_service.get_ai_response(user_input.message)
        
        # Evaluate the response for CBT techniques
        evaluation_dict = ai_service.evaluate_response(ai_response)
        evaluation = CBTEvaluation(**evaluation_dict)
        
        return ChatResponse(
            response=ai_response,
            evaluation=evaluation,
            timestamp=datetime.now()
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing chat: {str(e)}")

@router.get("/reset", response_model=ResetResponse)
def reset_conversation():
    """Reset the conversation history"""
    try:
        ai_service.reset_conversation()
        return ResetResponse(
            status="success",
            message="Conversation has been reset"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error resetting conversation: {str(e)}")

@router.get("/health", response_model=HealthResponse)
def health_check():
    """Health check endpoint"""
    return HealthResponse(
        status="healthy",
        message="CBT Therapy Assistant API is running"
    )

@router.get("/conversation")
def get_conversation():
    """Get current conversation history (for debugging)"""
    return {
        "conversation_history": ai_service.get_conversation_history(),
        "message_count": len(ai_service.get_conversation_history())
    } 