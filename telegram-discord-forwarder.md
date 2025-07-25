# telegram-discord-forwarder

Sync Telegram channels/groups to Discord in real-time — including media.

## Overview

`telegram-discord-forwarder` is a Python application designed to seamlessly bridge communication between Telegram and Discord. It leverages the `Telethon` library to monitor specified Telegram groups or channels and automatically forwards new messages, including text and media (photos, documents), to a configured Discord webhook. This project is ideal for communities, content creators, or anyone looking to centralize their cross-platform communications.

## Features

*   **Real-time Forwarding:** Instantly relays new messages from Telegram to Discord.
*   **Media Support:** Forwards both text messages and various media types (photos, documents).
*   **User Session Integration:** Uses `Telethon` to log in as a Telegram user, allowing monitoring of private groups and channels.
*   **Secure Configuration:** Utilizes `.env` files for managing sensitive API credentials and webhook URLs.
*   **Modular Design:** Clean and organized file structure for easy understanding and maintenance.
*   **Comprehensive Logging:** Provides detailed logs for monitoring application activity and troubleshooting.
*   **Easy to Run:** Simple execution via `python main.py`.

## Project Structure

```
telegram-discord-forwarder/
├── main.py
├── telegram_bridge.py
├── discord_sender.py
├── config.py
├── .env
├── requirements.txt
└── README.md
```

*   `main.py`: The main entry point of the application. Orchestrates the Telegram monitoring and Discord forwarding.
*   `telegram_bridge.py`: Handles all interactions with the Telegram API, including client initialization, message monitoring, and media downloading.
*   `discord_sender.py`: Manages sending messages and media to the Discord webhook.
*   `config.py`: Loads and validates configuration settings from the `.env` file.
*   `.env`: Environment file for storing sensitive credentials and application settings.
*   `requirements.txt`: Lists all Python dependencies required to run the project.
*   `README.md`: This documentation file, providing setup, usage, and project details.

## Setup Instructions

Follow these steps to get your Telegram-Discord Forwarder up and running.

### 1. Clone the Repository

First, clone this repository to your local machine:

```bash
git clone https://github.com/your-username/telegram-discord-forwarder.git
cd telegram-discord-forwarder
```

*(Note: Replace `your-username` with your actual GitHub username or the repository owner's username if you're forking.)*

### 2. Create a Virtual Environment (Recommended)

It's highly recommended to use a virtual environment to manage dependencies:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies

Install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```

### 4. Obtain Telegram API Credentials

To use Telethon, you need to obtain `api_id` and `api_hash` from Telegram. Follow these steps:

1.  Go to [my.telegram.org](https://my.telegram.org).
2.  Log in using your Telegram phone number.
3.  Click on 


"API development tools" and then "Create new application".
4.  Fill in the required fields. You can put anything for "App title" and "Short name" as they are not critical. For "Platform", select "Desktop".
5.  Click "Create application".
6.  You will now see your `api_id` and `api_hash`. Copy these values.

### 5. Create a Discord Webhook URL

To send messages to Discord, you need a webhook URL. Follow these steps:

1.  Open your Discord server settings.
2.  Go to "Integrations" -> "Webhooks" -> "New Webhook".
3.  Give it a name (e.g., "Telegram Forwarder") and choose the channel where messages will be posted.
4.  Copy the generated Webhook URL.

### 6. Configure `.env` File

Rename the `.env.example` file to `.env` (if you haven't already) and fill in the credentials you obtained:

```bash
mv .env.example .env # If you started with .env.example
```

Open the `.env` file and update it with your details:

```ini
# Telegram API credentials (get from https://my.telegram.org)
TELEGRAM_API_ID=YOUR_API_ID
TELEGRAM_API_HASH=YOUR_API_HASH

# Discord webhook URL
DISCORD_WEBHOOK_URL=YOUR_DISCORD_WEBHOOK_URL

# Telegram channels/groups to monitor (comma-separated)
# Use channel/group usernames (without @) or IDs. Examples: channel_username, -1001234567890
TELEGRAM_CHANNELS=YOUR_TELEGRAM_CHANNEL_OR_GROUP_USERNAME_OR_ID

# Optional: Session name for Telegram client
SESSION_NAME=telegram_forwarder

# Optional: Enable debug logging (true/false)
DEBUG=false
```

**Important Notes for `TELEGRAM_CHANNELS`:**

*   For public channels, you can use their username (e.g., `my_public_channel`).
*   For private channels or groups, you need their numerical ID. You can often get this by forwarding a message from the channel/group to a bot like `@JsonDumpBot` or `@getidsbot` and looking for the `chat.id` or `channel_id`.
*   Make sure to include the `-100` prefix for channel IDs (e.g., `-1001234567890`).
*   Separate multiple channels/groups with commas.

## Usage

Once you have completed the setup, you can run the forwarder:

```bash
python main.py
```

### First Run Authentication

The first time you run `main.py`, Telethon will prompt you to enter your phone number and the verification code sent to your Telegram app. This is a one-time process to create a session file (`telegram_forwarder.session` by default, based on `SESSION_NAME` in `.env`). Once authenticated, you won't need to do this again unless the session file is deleted or becomes invalid.

### Running in the Background (Optional)

For continuous operation, you might want to run this script in the background using tools like `nohup` or `screen` / `tmux` on Linux servers.

Example with `nohup`:

```bash
nohup python main.py > forwarder.log 2>&1 &
```

This will run the script in the background and redirect its output to `forwarder.log`.

## Logging

The application logs its activities to the console and to a file named `telegram_forwarder.log` in the project directory. You can adjust the logging level by setting `DEBUG=true` in your `.env` file for more verbose output.

## Troubleshooting

*   **`telethon.errors.rpc_error_list.AuthKeyUnregisteredError` or similar authentication issues:** Your `api_id` or `api_hash` might be incorrect, or your session file is corrupted. Double-check your `.env` values and try deleting the `.session` file (e.g., `telegram_forwarder.session`) and re-running `main.py` to re-authenticate.
*   **Messages not forwarding:**
    *   Ensure `TELEGRAM_CHANNELS` in `.env` are correctly specified (usernames for public, IDs with `-100` prefix for private).
    *   Check the `telegram_forwarder.log` file for any errors related to message processing or Discord webhook calls.
    *   Verify your Discord webhook URL is correct and active.
*   **`aiohttp.ClientConnectorError`:** This usually indicates a network issue or an incorrect Discord webhook URL. Ensure your internet connection is stable and the webhook URL is valid.

## Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests.

## License

This project is open-source and available under the MIT License.

## Author

Manus AI


