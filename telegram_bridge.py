import logging
from telethon import TelegramClient, events
from telethon.tl.types import MessageMediaPhoto, MessageMediaDocument
from config import Config

logger = logging.getLogger(__name__)

class TelegramBridge:
    """Handles Telegram client operations and message monitoring."""

    def __init__(self, discord_sender):
        self.client = TelegramClient(
            Config.SESSION_NAME,
            Config.TELEGRAM_API_ID,
            Config.TELEGRAM_API_HASH
        )
        self.discord_sender = discord_sender
        self.monitored_entities = []

    async def start(self):
        """Starts the Telegram client and begins listening for messages."""
        logger.info("Starting Telegram client...")
        await self.client.start()
        logger.info("Telegram client started.")

        # Resolve monitored entities (channels/groups)
        for entity_str in Config.TELEGRAM_CHANNELS:
            try:
                entity = await self.client.get_entity(entity_str)
                self.monitored_entities.append(entity)
                logger.info(f"Monitoring Telegram entity: {entity.title} (ID: {entity.id})")
            except Exception as e:
                logger.error(f"Could not resolve Telegram entity {entity_str}: {e}")

        # Add event handler for new messages
        self.client.add_event_handler(self.on_new_message, events.NewMessage)

        logger.info("Telegram bridge is ready to forward messages.")

    async def on_new_message(self, event):
        """Handles new incoming Telegram messages."""
        if event.is_private or event.is_channel or event.is_group:
            sender = await event.get_sender()
            chat = await event.get_chat()

            # Only process messages from monitored entities
            if chat not in self.monitored_entities:
                return

            message_text = event.message.message
            media_path = None

            if event.message.media:
                if isinstance(event.message.media, MessageMediaPhoto):
                    logger.info(f"Downloading photo from {chat.title}...")
                    media_path = await event.message.download_media(file=f'./downloads/{event.id}.jpg')
                    logger.info(f"Photo downloaded to {media_path}")
                elif isinstance(event.message.media, MessageMediaDocument):
                    # Handle documents (e.g., files, videos, gifs)
                    # For simplicity, we'll download all documents, but you might want to filter by type
                    logger.info(f"Downloading document from {chat.title}...")
                    media_path = await event.message.download_media(file=f'./downloads/{event.id}_{event.message.media.document.id}.' + event.message.media.document.mime_type.split('/')[-1])
                    logger.info(f"Document downloaded to {media_path}")
                else:
                    logger.warning(f"Unsupported media type received: {type(event.message.media)}")

            await self.discord_sender.send_message(
                chat_title=chat.title,
                sender_name=sender.first_name or sender.username or str(sender.id),
                message_text=message_text,
                media_path=media_path
            )

    async def run_until_disconnected(self):
        """Keeps the client running until disconnected."""
        await self.client.run_until_disconnected()

    async def stop(self):
        """Stops the Telegram client."""
        logger.info("Stopping Telegram client...")
        await self.client.disconnect()
        logger.info("Telegram client stopped.")


