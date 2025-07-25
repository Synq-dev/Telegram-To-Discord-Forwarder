import asyncio
import logging
from config import Config, setup_logging
from telegram_bridge import TelegramBridge
from discord_sender import DiscordSender

# Setup logging as early as possible
setup_logging()
logger = logging.getLogger(__name__)

async def main():
    """Main function to run the Telegram-Discord forwarder."""
    logger.info("Starting Telegram-Discord Forwarder...")

    try:
        Config.validate()
        logger.info("Configuration validated successfully.")
    except ValueError as e:
        logger.error(f"Configuration error: {e}")
        return

    discord_sender = DiscordSender()
    telegram_bridge = TelegramBridge(discord_sender)

    try:
        await telegram_bridge.start()
        logger.info("Telegram bridge started. Listening for messages...")
        await telegram_bridge.run_until_disconnected()
    except KeyboardInterrupt:
        logger.info("Forwarder stopped by user (KeyboardInterrupt).")
    except Exception as e:
        logger.critical(f"An unhandled error occurred: {e}", exc_info=True)
    finally:
        await telegram_bridge.stop()
        logger.info("Telegram-Discord Forwarder stopped.")

if __name__ == "__main__":
    asyncio.run(main())


