import logging
import aiohttp
import os
from config import Config

logger = logging.getLogger(__name__)

class DiscordSender:
    """Handles sending messages and media to Discord webhooks."""

    def __init__(self):
        self.webhook_url = Config.DISCORD_WEBHOOK_URL

    async def send_message(self, chat_title, sender_name, message_text, media_path=None):
        """Sends a message to the configured Discord webhook."""
        payload = {
            "username": "Telegram Forwarder",
            "embeds": [
                {
                    "title": f"New message from {chat_title}",
                    "description": f"**From:** {sender_name}\n\n{message_text}",
                    "color": 3447003  # A nice blue color
                }
            ]
        }

        async with aiohttp.ClientSession() as session:
            if media_path and os.path.exists(media_path):
                # If media exists, send as multipart/form-data
                with open(media_path, 'rb') as f:
                    form = aiohttp.FormData()
                    form.add_field('payload_json', str(payload))
                    form.add_field('file', f, filename=os.path.basename(media_path))
                    
                    try:
                        async with session.post(self.webhook_url, data=form) as response:
                            if response.status == 204:
                                logger.info(f"Message with media from {chat_title} forwarded to Discord.")
                            else:
                                response_text = await response.text()
                                logger.error(f"Failed to forward message with media to Discord. Status: {response.status}, Response: {response_text}")
                    except aiohttp.ClientError as e:
                        logger.error(f"Error sending message with media to Discord: {e}")
                
                # Clean up the downloaded media file
                try:
                    os.remove(media_path)
                    logger.info(f"Cleaned up media file: {media_path}")
                except OSError as e:
                    logger.error(f"Error removing media file {media_path}: {e}")

            else:
                # If no media, send as application/json
                try:
                    async with session.post(self.webhook_url, json=payload) as response:
                        if response.status == 204:
                            logger.info(f"Message from {chat_title} forwarded to Discord.")
                        else:
                            response_text = await response.text()
                            logger.error(f"Failed to forward message to Discord. Status: {response.status}, Response: {response_text}")
                except aiohttp.ClientError as e:
                    logger.error(f"Error sending message to Discord: {e}")


