import logging
from aiogram import Bot, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
# import os
from venv_var import WEBHOOK_PATH, WEBHOOK_URL, WEBAPP_HOST, WEBAPP_PORT, TELEGRAM_BOT_TOKEN, DATABASE_APP_HOST,USER_DB,PASSWORD_DB,DB_NAME
import random, psycopg2

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

async def on_startup(dp):
    print("Set webhook")
    print(WEBHOOK_URL)
    await bot.set_webhook(WEBHOOK_URL)
    print("Бот увійшов в онлайн")
    try:
        logging.warning("Connecting PostgreSQL")
        conn = psycopg2.connect(DATABASE_APP_HOST)
        logging.warning("Succses")
    except:
        logging.warning("[ERROR]: Connecting PostgreSQL closed")



foo = [
    "Щоб життя стало краще, вона спочатку повинна стати гірше.",
    "Коли не можеш висловити свої почуття, це ще не означає, що вони неглибокі.",
    "Життя – хвороба матерії, мислення – хвороба життя.",
    "Хіба це важливо, хто ти і як ти виглядаєш, якщо тебе люблять?"
]

@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    print("Message")
    print(message.text)
    try:
        await bot.send_message(message.from_user.id, message.text)
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://web.telegram.org/z/#5314647341')


@dp.message_handler(commands="list")
async def command_list(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, foo[random.randrange(len(foo))])
    except:
        await message.reply("Упс что-то пошло не так")


async def on_shutdown(dp):
    logging.warning('Shutting down..')
    await bot.delete_webhook()
    print("Бот вийшов з чату")


if __name__ == '__main__':
    # executor.start_polling(dp, on_startup=on_startup)
    logging.warning(WEBAPP_HOST)
    logging.warning(WEBAPP_PORT)

    executor.start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT
    )