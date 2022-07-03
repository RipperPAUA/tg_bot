import psycopg2
import logging
from aiogram.utils.executor import start_webhook
from create_bot import dp, bot, env, WEBHOOK_URL, WEBHOOK_PATH, WEBAPP_HOST, WEBAPP_PORT


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

except Exception as _ex:
    logging.warning(_ex, "Error starting connection")


from handlers import other
other.register_handlers_other(dp)

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
