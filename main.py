import logging
import environ,os
from aiogram import Bot, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.webhook import SendMessage
from aiogram.utils.executor import start_webhook

logging.basicConfig(level=logging.INFO)


env=environ.Env()
env.read_env(".env")

API_TOKEN = env("BOT_TOKEN")
logging.warning(f"BOT_TOKEN: {API_TOKEN}")

# webhook settings
WEBHOOK_HOST = env("HEROKU_APP_NAME")
WEBHOOK_PATH = env("WEBHOOK_PATH")
WEBHOOK_URL = f"http://{WEBHOOK_HOST}{WEBHOOK_PATH}"
logging.warning(f"WEBHOOK_HOST: {WEBHOOK_HOST}")
logging.warning(f"WEBHOOK_PATH: {WEBHOOK_PATH}")
logging.warning(f"WEBHOOK_URL: {WEBHOOK_URL}")

# webserver settings
WEBAPP_HOST = "0.0.0.0"
WEBAPP_PORT = os.getenv('PORT', default=8000)


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())


@dp.message_handler()
async def echo(message: types.Message):
    # Regular request
    # await bot.send_message(message.chat.id, message.text)

    # or reply INTO webhook
    return SendMessage(message.chat.id, message.text)


async def on_startup():
    logging.warning('Starting.....')
    logging.warning(f"{WEBHOOK_URL}")
    await bot.set_webhook(WEBHOOK_URL)
    # insert code here to run it after start


async def on_shutdown():
    logging.warning('Shutting down..')

    # insert code here to run it before shutdown

    # Remove webhook (not acceptable in some cases)
    await bot.delete_webhook()
    logging.warning('Bye!')


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