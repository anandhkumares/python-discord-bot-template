# Python Discord Bot Template
A template repository for discord bot that is written in python using discord.py.

## Motivation
I made this template so that I don't spend time creating a default project structure that I usually use every time I want to make a bot. (Trust me, I have done it dozens of times, and every time I wished there was a template that I could copy.)

## Getting Started
### Virtual Environment
```bash
# Of course for Linux (more in https://docs.python.org/3/library/venv.html)
python3 -m venv .venv
source .venv/bin/activate
```

### Installing Dependencies
```bash
pip install -r requirements.txt
```

### Secrets
Create a `.env` file on root dir.
```py
DISCORD_TOKEN="YOUR_DISCORD_BOT_TOKEN"
LOG_LEVEL="" # Values like "DEBUG", "INFO", "WARN" ...
```

### Running Bot
```bash
python3 -m bot
```

### Additional
- You can configure logger in `bot/logging_config.py`
- You can configure rest of the things including variables used in `.env`, emojis and embed color in `bot/constants.py`