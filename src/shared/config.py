"""
Desc: Configuration variables file
"""

from os import getenv

from dotenv import load_dotenv

load_dotenv(override=True)

# Server Conf
PROD = getenv("ENV") == "production"

# Mongo DB
MONGO_URI = getenv("MONGO_URI")

# Telegram Bot Conf
BOT_TOKEN = getenv("BOT_TOKEN")
