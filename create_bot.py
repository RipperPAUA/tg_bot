from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.middlewares.logging import LoggingMiddleware
import logging
import environ
import os

env = environ.Env()
env.read_env(".env")

BOT_API_TOKEN = env("BOT_TOKEN")
logging.warning(f"BOT_TOKEN: {BOT_API_TOKEN}")

# webhook settings
WEBHOOK_HOST = env("HEROKU_APP_NAME")
WEBHOOK_PATH = env("WEBHOOK_PATH")
WEBHOOK_URL = f"https://{WEBHOOK_HOST}.herokuapp.com{WEBHOOK_PATH}"
logging.warning(f"WEBHOOK_HOST: {WEBHOOK_HOST}")
logging.warning(f"WEBHOOK_PATH: {WEBHOOK_PATH}")
logging.warning(f"WEBHOOK_URL: {WEBHOOK_URL}")

# webserver settings
WEBAPP_HOST = "0.0.0.0"
WEBAPP_PORT = os.getenv('PORT', default=8000)


logging.basicConfig(level=logging.INFO)



bot = Bot(token=BOT_API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())
