# 🌙 Sleep & Soul Companion

A gentle, sleep-focused CBT companion built with FastAPI backend and React frontend. This application helps users wind down and explore their emotions before sleep through calming conversations and evidence-based CBT techniques.

## 🏗️ Project Structure

```
cbt-therapy-assistant/
├── backend/                    # Backend API package
│   ├── __init__.py
│   ├── api/                    # API routes and endpoints
│   │   ├── __init__.py
│   │   └── routes.py           # FastAPI routes
│   ├── config/                 # Configuration management
│   │   ├── __init__.py
│   │   └── settings.py         # Application settings
│   ├── models/                 # Pydantic models and schemas
│   │   ├── __init__.py
│   │   └── schemas.py          # API request/response models
│   └── services/               # Business logic services
│       ├── __init__.py
│       └── ai_service.py       # AI conversation management with CBT techniques
├── frontend/                   # React frontend application
│   ├── public/
│   ├── src/
│   │   ├── App.js              # Main React component
│   │   ├── App.css             # Styles
│   │   └── ...
│   ├── package.json
│   └── ...
├── main.py                     # FastAPI application entry point
├── pyproject.toml              # Python dependencies
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Python 3.12+
- Node.js 16+
- [Ollama](https://ollama.ai/) installed locally
- UV package manager

### Quick Start

**Option 1: Automated Startup (Recommended)**
```bash
# Install dependencies
pip install -r requirements.txt

# Start Ollama
ollama serve

# In another terminal, run the startup script
python start_app.py
```

**Option 2: Manual Setup**

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   # or with UV:
   uv sync
   ```

2. **Pull the AI model:**
   ```bash
   ollama pull mistral:latest
   ```

3. **Start the backend server:**
   ```bash
   python main.py
   ```

   The API will be available at:
   - **Main API**: http://localhost:8000
   - **API Documentation**: http://localhost:8000/docs
   - **Health Check**: http://localhost:8000/health

### Frontend Setup

1. **Navigate to frontend directory:**
   ```bash
   cd frontend
   ```

2. **Install Node.js dependencies:**
   ```bash
   npm install
   ```

3. **Start the React development server:**
   ```bash
   npm start
   ```

   The frontend will be available at http://localhost:3000

## 🔧 API Endpoints

### Base URL: `http://localhost:8000/api`

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/chat` | Send a message to the CBT therapy assistant |
| GET | `/reset` | Reset the conversation history |
| GET | `/health` | Health check endpoint |
| GET | `/conversation` | Get current conversation history (debug) |

### Bedtime Ritual Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/bedtime/start` | Start a new bedtime ritual session |
| POST | `/bedtime/continue` | Continue an active session with follow-up questions |
| POST | `/bedtime/end` | End a bedtime ritual session |
| GET | `/bedtime/session/{id}` | Get session status |
| GET | `/bedtime/sessions` | List all active sessions |

### Example API Usage

**Chat with the assistant:**
```bash
curl -X POST "http://localhost:8000/chat" \
     -H "Content-Type: application/json" \
     -d '{"message": "I have been feeling anxious about work lately"}'
```

**Reset conversation:**
```bash
curl -X GET "http://localhost:8000/reset"
```

## ✨ Features

### Backend Features
- **FastAPI** with automatic OpenAPI documentation
- **Modular architecture** with separate services, models, and API layers
- **Ollama integration** for local AI model inference
- **Emotion-focused CBT conversation management** with privacy-safe dialogue
- **CBT technique evaluation system** to track helpful interactions
- **Clinical boundaries** and professional disclaimers
- **Evidence-based technique selection** based on emotional state
- **CORS enabled** for frontend integration
- **Environment-based configuration**

### Frontend Features
- **Modern React interface** with hooks
- **Real-time chat** with typing indicators
- **CBT technique tracking** with visual badges showing:
  - Questions asked
  - Thought exploration
  - Reflection encouragement
  - CBT technique usage
- **Natural conversation flow** that asks one question at a time, respecting privacy and focusing on feelings
- **Sleep-oriented design** with navy and light blue theme
- **Enhanced chat visibility** with larger containers and better spacing
- **Responsive design** for mobile and desktop
- **Error handling** and loading states
- **Auto-scroll** to latest messages

### CBT Assistant Capabilities
- Guides users through cognitive behavioral therapy techniques
- Asks thoughtful, open-ended questions to promote self-reflection
- Uses CBT methods like:
  - Thought challenging and cognitive restructuring
  - Identifying cognitive distortions
  - Behavioral activation
  - Mindfulness and grounding exercises
  - Problem-solving strategies
  - Goal setting and action planning
- Maintains therapeutic conversation context
- Provides compassionate, non-judgmental responses
- Focuses on teaching CBT tools rather than providing direct therapy

## 🎯 Usage

### Sleep-Focused CBT Chat
1. **Start both servers** (backend on :8000, frontend on :3000)
2. **Open your browser** to http://localhost:3000
3. **Start sharing** your thoughts and feelings with the sleep companion
4. **Try messages like:**
   - "I've been feeling anxious about tomorrow"
   - "My mind keeps racing with thoughts"
   - "I'm having trouble winding down for sleep"
   - "I feel overwhelmed and need to relax"

The companion will start with gentle, emotion-focused questions (one at a time) to understand how you're feeling, then offer relevant CBT techniques based on your emotional state, helping you choose and practice the best one for peaceful sleep while maintaining privacy and clinical boundaries.

## 🧠 CBT Techniques Implemented

- **Thought Records**: Exploring and documenting negative thoughts
- **Cognitive Restructuring**: Challenging unhelpful thinking patterns
- **Behavioral Experiments**: Testing negative predictions
- **Mindfulness**: Present-moment awareness exercises
- **Problem-Solving**: Breaking down overwhelming situations
- **Activity Scheduling**: Planning positive activities
- **Cognitive Distortion Identification**: Recognizing thinking traps

## 🔧 Configuration

You can customize the application by modifying `backend/config/settings.py` or creating a `.env` file:

```env
AI_MODEL=mistral:latest
HOST=0.0.0.0
PORT=8000
ALLOWED_ORIGINS=["http://localhost:3000"]
```

## 📚 Development

### Adding New CBT Techniques

1. **API Changes**: Add new therapeutic routes in `backend/api/routes.py`
2. **Data Models**: Define new therapeutic schemas in `backend/models/schemas.py`
3. **CBT Logic**: Implement therapeutic services in `backend/services/ai_service.py`
4. **Configuration**: Update settings in `backend/config/settings.py`
5. **Frontend**: Modify React components in `frontend/src/`

### Running in Production

1. Build the React frontend: `npm run build`
2. Configure environment variables
3. Use a production ASGI server like Gunicorn
4. Set up reverse proxy with Nginx

## ⚠️ Important Disclaimer

This application is designed as a CBT learning tool and is **not a replacement for professional therapy or mental health treatment**. If you are experiencing severe mental health issues, please seek help from a qualified mental health professional.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.
