from typing import List
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # API Configuration
    app_name: str = "CBT Therapy Assistant API"
    app_description: str = "AI-powered cognitive behavioral therapy assistant"
    app_version: str = "1.0.0"
    
    # Server Configuration
    host: str = "0.0.0.0"
    port: int = 8000
    reload: bool = True
    
    # CORS Configuration
    allowed_origins: List[str] = ["http://localhost:3000"]
    
    # AI Configuration
    ai_model: str = "mistral:latest"
    
    # Logging
    log_level: str = "INFO"
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

# Create settings instance
settings = Settings() 