<h1 align="center">📡 Telegram → Discord Forwarder</h1>
<p align="center">
  <b>Real-time bridge from Telegram to Discord, including media.</b><br>
  Built with ❤️ by <a href="https://github.com/Synq-dev">Synq</a>
</p>

---

## 🧩 Overview

`telegram-discord-forwarder` is a Python-based message bridge that forwards **Telegram** group or channel content directly to a **Discord** channel using webhooks.  
It supports **text**, **photos**, **files**, and works via user session (not a bot) for maximum flexibility.

---

## 🚀 Features

- 🔄 Real-time forwarding from Telegram → Discord
- 🖼️ Supports media (photos, documents, etc.)
- 🧑‍💻 Uses Telethon user session login (not restricted like bots)
- 🔐 `.env` config for secure setup
- 📂 Modular, clean code structure
- 📜 Logging system with debug toggle
- 🟢 Simple: `python main.py`

---

## 🗂️ Project Structure

```
Telegram-To-Discord-Forwarder/
├── main.py
├── telegram_bridge.py
├── discord_sender.py
├── config.py
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup

### 1. Clone the Repo

```bash
git clone https://github.com/Synq-dev/Telegram-To-Discord-Forwarder.git
cd Telegram-To-Discord-Forwarder
```

### 2. (Recommended) Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Get Telegram API Credentials

- Go to https://my.telegram.org
- Log in and go to **API Development Tools**
- Create an application → Copy `api_id` and `api_hash`

### 5. Create Discord Webhook

- Open your Discord server settings
- Go to: **Integrations → Webhooks → New Webhook**
- Copy the webhook URL

### 6. Configure `.env`

Rename `.env.example` (if exists) or create `.env`:

```ini
TELEGRAM_API_ID=YOUR_API_ID
TELEGRAM_API_HASH=YOUR_API_HASH
DISCORD_WEBHOOK_URL=YOUR_DISCORD_WEBHOOK_URL
TELEGRAM_CHANNELS=channel_username,-1001234567890
SESSION_NAME=telegram_forwarder
DEBUG=false
```

---

## ▶️ Run the App

```bash
python main.py
```

On first run, you’ll authenticate your Telegram account (code sent to Telegram app).  
Session is saved as a `.session` file for future use.

---

## 📓 Logging

- All logs are printed to the terminal
- A log file `telegram_forwarder.log` is also created
- Set `DEBUG=true` in `.env` to see more output

---

## 🛠️ Troubleshooting

- ❌ **Auth errors:** Re-check API credentials, or delete `.session` and retry
- ❌ **No messages forwarding:** Ensure `TELEGRAM_CHANNELS` is valid (usernames or `-100` IDs)
- ❌ **Webhook errors:** Verify Discord webhook URL
- ❌ **Network errors:** Check your internet and try again

---

## 💼 Need Custom Telegram/Discord Bots?

Get custom tools built for your server or business. I build:
- Telegram + Discord Bots
- Cross-platform automation
- Private API integrations

**📩 Contact Me for Paid Projects:**
- 💬 Discord: [`synq.dev`](https://discord.com/users/synq.dev)
- 📧 Email: `dev.synq@proton.me`

---

## ❤️ Support This Project

If you found this useful, you can support my work by donating crypto:

| Coin       | Address |
|------------|---------|
| ![Bitcoin](https://img.shields.io/badge/Bitcoin-BTC-orange?style=flat-square&logo=bitcoin) | `bc1qepy6uzu6k5hgtvzeqw7nyzpn98dzq9chna8jgl` |
| ![Solana](https://img.shields.io/badge/Solana-SOL-purple?style=flat-square&logo=solana) | `mmNe77AYbSRQRs54Db4Xuk3zoDY2gCNF8J4gPkCaKvF` |
| ![Litecoin](https://img.shields.io/badge/Litecoin-LTC-gray?style=flat-square&logo=litecoin) | `ltc1qf5tjcfdvwf9py4yd9ss9hdn2q6v2c8lgjyeax0` |


---

## 📄 License

MIT License
