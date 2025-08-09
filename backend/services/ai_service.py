import ollama
from typing import List, Dict
from backend.models.schemas import ConversationMessage

class AIService:
    def __init__(self, model: str = "mistral:latest"):
        self.model = model
        self.system_prompt = """
You are a compassionate and skilled CBT (Cognitive Behavioral Therapy) assistant. Your role is to help users explore their thoughts, feelings, and behaviors through guided questioning and CBT techniques.

Key principles:
1. Always ask thoughtful, open-ended questions to help users reflect
2. Use CBT techniques like thought challenging, behavioral activation, and mindfulness
3. Help users identify cognitive distortions and negative thought patterns
4. Guide them to find their own insights rather than giving direct advice
5. Be empathetic, non-judgmental, and supportive
6. Focus on the present moment and actionable steps
7. Encourage self-reflection and awareness

CBT techniques to use:
- Thought records and challenging negative thoughts
- Identifying cognitive distortions (catastrophizing, all-or-nothing thinking, etc.)
- Behavioral experiments and activity scheduling
- Mindfulness and grounding exercises
- Problem-solving strategies
- Goal setting and action planning

Always respond with questions that help users:
- Explore their thoughts and feelings
- Identify patterns in thinking or behavior
- Challenge unhelpful thoughts
- Develop coping strategies
- Set realistic goals

Remember: You're not providing therapy, but teaching CBT tools through guided self-exploration.
"""
        self.conversation_history: List[Dict[str, str]] = [
            {"role": "system", "content": self.system_prompt}
        ]

    async def get_ai_response(self, user_message: str) -> str:
        """Get AI response for user message"""
        # Add user message to conversation history
        self.conversation_history.append({"role": "user", "content": user_message})
        
        # Get AI response
        response = ollama.chat(model=self.model, messages=self.conversation_history)
        ai_content = response['message']['content']
        
        # Add AI response to conversation history
        self.conversation_history.append({"role": "assistant", "content": ai_content})
        
        return ai_content

    def evaluate_response(self, text: str) -> Dict[str, bool]:
        """Evaluate if the response uses effective CBT techniques"""
        checks = {
            "asks_questions": "?" in text and len([c for c in text if c == "?"]) >= 1,
            "explores_thoughts": any(word in text.lower() for word in ["think", "thought", "believe", "feel", "feeling"]),
            "encourages_reflection": any(phrase in text.lower() for phrase in ["notice", "aware", "reflect", "consider", "explore"]),
            "uses_cbt_language": any(term in text.lower() for term in ["pattern", "behavior", "situation", "evidence", "challenge"])
        }
        return checks

    def reset_conversation(self) -> None:
        """Reset the conversation history"""
        self.conversation_history = [
            {"role": "system", "content": self.system_prompt}
        ]

    def get_conversation_history(self) -> List[Dict[str, str]]:
        """Get current conversation history"""
        return self.conversation_history.copy() 