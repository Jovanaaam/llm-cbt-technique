import React, { useState, useRef, useEffect } from 'react';
import axios from 'axios';
import { Send, RotateCcw, MessageCircle, CheckCircle, XCircle } from 'lucide-react';
import './App.css';

const API_BASE = 'http://localhost:8000';

function App() {
  const [messages, setMessages] = useState([
    {
      content: "🌙 Hello! I'm here to help you wind down and prepare for peaceful sleep.\n\nHow has your evening been so far? ✨",
      isUser: false,
      timestamp: new Date(),
    }
  ]);
  const [inputMessage, setInputMessage] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const sendMessage = async () => {
    if (!inputMessage.trim() || isLoading) return;

    const userMessage = {
      content: inputMessage,
      isUser: true,
      timestamp: new Date(),
    };

    setMessages(prev => [...prev, userMessage]);
    setInputMessage('');
    setIsLoading(true);

    try {
      const response = await axios.post(`${API_BASE}/chat`, {
        message: inputMessage
      });

      const botMessage = {
        content: response.data.response,
        isUser: false,
        timestamp: new Date(),
        evaluation: response.data.evaluation,
      };

      setMessages(prev => [...prev, botMessage]);
    } catch (error) {
      console.error('Error sending message:', error);
      const errorMessage = {
        content: 'Sorry, I encountered an error. Please try again.',
        isUser: false,
        timestamp: new Date(),
        isError: true,
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  const resetChat = async () => {
    try {
      await axios.get(`${API_BASE}/reset`);
      setMessages([
        {
          content: "🌙 Chat has been reset.\n\nHow has your evening been so far? ✨",
          isUser: false,
          timestamp: new Date(),
        }
      ]);
    } catch (error) {
      console.error('Error resetting chat:', error);
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  };

  const EvaluationBadges = ({ evaluation }) => {
    if (!evaluation) return null;

    const badges = [
      { key: 'asks_questions', label: 'Questions', value: evaluation.asks_questions },
      { key: 'explores_thoughts', label: 'Thoughts', value: evaluation.explores_thoughts },
      { key: 'encourages_reflection', label: 'Reflection', value: evaluation.encourages_reflection },
      { key: 'uses_cbt_language', label: 'CBT Techniques', value: evaluation.uses_cbt_language },
    ];

    return (
      <div className="evaluation-badges">
        {badges.map(badge => (
          <div key={badge.key} className={`badge ${badge.value ? 'success' : 'pending'}`}>
            {badge.value ? <CheckCircle size={12} /> : <XCircle size={12} />}
            <span>{badge.label}</span>
          </div>
        ))}
      </div>
    );
  };

  return (
    <div className="app">
      <div className="chat-container">
        <div className="chat-header">
          <div className="header-content">
            <MessageCircle className="header-icon" />
            <h1>🌙 Sleep & Soul Companion</h1>
            <p>Emotion-focused CBT guidance for peaceful evenings</p>
          </div>
          <button onClick={resetChat} className="reset-button">
            <RotateCcw size={18} />
            Reset Chat
          </button>
        </div>

        <div className="messages-container">
          {messages.map((message, index) => (
            <div key={index} className={`message ${message.isUser ? 'user' : 'bot'} ${message.isError ? 'error' : ''}`}>
              <div className="message-content">
                <div className="message-text">{message.content}</div>
                {message.evaluation && <EvaluationBadges evaluation={message.evaluation} />}
              </div>
              <div className="message-time">
                {message.timestamp.toLocaleTimeString()}
              </div>
            </div>
          ))}
          {isLoading && (
            <div className="message bot">
              <div className="message-content">
                <div className="typing-indicator">
                  <span></span>
                  <span></span>
                  <span></span>
                </div>
              </div>
            </div>
          )}
          <div ref={messagesEndRef} />
        </div>

        <div className="input-container">
          <div className="input-wrapper">
            <textarea
              value={inputMessage}
              onChange={(e) => setInputMessage(e.target.value)}
              onKeyPress={handleKeyPress}
              placeholder="Share how you're feeling this evening... 🌙"
              className="message-input"
              rows="1"
              disabled={isLoading}
            />
            <button
              onClick={sendMessage}
              disabled={!inputMessage.trim() || isLoading}
              className="send-button"
            >
              <Send size={20} />
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
