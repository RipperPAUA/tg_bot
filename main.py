import psycopg2
import logging
from aiogram.utils.executor import start_webhook
from create_bot import dp, bot, env, WEBHOOK_URL, WEBHOOK_PATH, WEBAPP_HOST, WEBAPP_PORT

try:
    conn=psycopg2.connect(
        host=env("DB_HOST"),
        user=env("DB_USER"),
        password=env("DB_PASSWORD"),
        database=env("DB_NAME")
    )
except Exception as _ex:
    conn.close()
    logging.warning(_ex, "Error starting connection")


async def on_startup(dp):
    logging.warning('Starting.....')
    logging.warning(f"{WEBHOOK_URL}")
    await bot.set_webhook(WEBHOOK_URL)


# insert code here to run it after start


async def on_shutdown(dp):
    logging.warning('Shutting down..')
    await bot.delete_webhook()
    logging.warning('Bye!')
    conn.execute()

if __name__ == '__main__':
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )
