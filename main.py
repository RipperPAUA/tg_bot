import psycopg2
import logging
from aiogram.utils.executor import start_webhook
from create_bot import dp, bot, env, WEBHOOK_URL, WEBHOOK_PATH, WEBAPP_HOST, WEBAPP_PORT

global conn

async def on_startup(dp, conn):
    logging.warning('Starting.....')
    logging.warning(f"{WEBHOOK_URL}")
    await bot.set_webhook(WEBHOOK_URL)
    try:
        conn = psycopg2.connect(
            host=env("DB_HOST"),
            user=env("DB_USER"),
            password=env("DB_PASSWORD"),
            database=env("DB_NAME")
        )
        logging.warning("Connecting to PostgreSQL success")
    except:
        logging.warning("Starting connection is falled")
        conn.close()
        return conn


from handlers import other
other.register_handlers_other(dp)

async def on_shutdown(dp, conn):
    logging.warning('Shutting down..')
    await bot.delete_webhook()
    logging.warning('Bye!')
    try:
        conn.close()
        logging.warning("Connection is closed")
    except:
        logging.warning("Connection was closed failld")
        conn.close()


if __name__ == '__main__':
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )
