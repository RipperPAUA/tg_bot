import logging
import os
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram import Bot, types

TOKEN = os.getenv('BOT_TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

HEROKU_APP_NAME = os.getenv('HEROKU_APP_NAME')

# webhook settings
WEBHOOK_HOST = f'https://{HEROKU_APP_NAME}.herokuapp.com'
WEBHOOK_PATH = "/webhook"
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

logging.warning(f"TOKEN: {TOKEN}")
logging.warning(f"HEROKU_APP_NAME: {HEROKU_APP_NAME}")
logging.warning(f"WEBHOOK_HOST: {WEBHOOK_HOST}")
logging.warning(f"WEBHOOK_PATH: {WEBHOOK_PATH}")
logging.warning(f"WEBHOOK_URL: {WEBHOOK_URL}")

# webserver settings
WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = os.getenv('PORT', default=8000)

async def on_startup(dp):
    await bot.set_webhook(WEBHOOK_URL)

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

async def on_shutdown(dp):
    await bot.delete_webhook()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )