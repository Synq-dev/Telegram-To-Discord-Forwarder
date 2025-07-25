"""
Configuration module for Telegram-Discord Forwarder
"""
import os
import logging
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Configuration class for the application"""
    
    # Telegram API credentials
    TELEGRAM_API_ID = int(os.getenv('TELEGRAM_API_ID', 0))
    TELEGRAM_API_HASH = os.getenv('TELEGRAM_API_HASH', '')
    
    # Discord webhook URL
    DISCORD_WEBHOOK_URL = os.getenv('DISCORD_WEBHOOK_URL', '')
    
    # Telegram channels/groups to monitor
    TELEGRAM_CHANNELS = [
        channel.strip() 
        for channel in os.getenv('TELEGRAM_CHANNELS', '').split(',') 
        if channel.strip()
    ]
    
    # Session name for Telegram client
    SESSION_NAME = os.getenv('SESSION_NAME', 'telegram_forwarder')
    
    # Debug mode
    DEBUG = os.getenv('DEBUG', 'false').lower() == 'true'
    
    @classmethod
    def validate(cls):
        """Validate configuration settings"""
        errors = []
        
        if not cls.TELEGRAM_API_ID or cls.TELEGRAM_API_ID == 0:
            errors.append("TELEGRAM_API_ID is required")
            
        if not cls.TELEGRAM_API_HASH:
            errors.append("TELEGRAM_API_HASH is required")
            
        if not cls.DISCORD_WEBHOOK_URL:
            errors.append("DISCORD_WEBHOOK_URL is required")
            
        if not cls.TELEGRAM_CHANNELS:
            errors.append("At least one TELEGRAM_CHANNEL is required")
            
        if errors:
            raise ValueError("Configuration errors:\n" + "\n".join(f"- {error}" for error in errors))
        
        return True

def setup_logging():
    """Setup logging configuration"""
    log_level = logging.DEBUG if Config.DEBUG else logging.INFO
    
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler('telegram_forwarder.log')
        ]
    )
    
    # Reduce telethon logging noise
    logging.getLogger('telethon').setLevel(logging.WARNING)

