import logging
import environ
import psycopg2
import os
from aiogram import Bot, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.webhook import SendMessage
from aiogram.utils.executor import start_webhook

logging.basicConfig(level=logging.INFO)


env=environ.Env()
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


bot = Bot(token=BOT_API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())


@dp.message_handler()
async def echo(message: types.Message):
    # Regular request
    # await bot.send_message(message.chat.id, message.text)

    # or reply INTO webhook
    return SendMessage(message.chat.id, message.text)


async def on_startup(dp):
    logging.warning('Starting.....')
    logging.warning(f"{WEBHOOK_URL}")
    await bot.set_webhook(WEBHOOK_URL)
try:
    logging.warning("Starting connection")
    conn = psycopg2.connect(
        host=env("DB_HOST"),
        user=env("DB_USER"),
        password=env("DB_PASSWORD"),
        database=env("DB_NAME")
    )
    # the cursor for performing database operations
    # cursor = conn.cursor()

    with conn.cursor() as cursor:
        pass
except Exception as _ex:
    logging.warning(_ex, "Error starting connection")



# insert code here to run it after start


async def on_shutdown(dp):

    # insert code here to run it before shutdown
    try:
        if conn:
            # cursor.close()
            conn.close()
            logging.warning("PostgreeSQL connection closed")
    except:
        conn.close()
        logging.warning("Error closing connection database")

    logging.warning('Shutting down..')
    await bot.delete_webhook()
    logging.warning('Bye!')

    # Remove webhook (not acceptable in some cases)


if __name__ == '__main__':
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )