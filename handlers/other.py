from aiogram import types, Dispatcher
from create_bot import bot
from keyboards import kb_client

# @dp.message_handler(commands=["start", "help"])
async def echo_send(message: types.Message):
    # Regular request
    await bot.send_message(message.from_user.id, message.text, reply_markup=kb_client)

    # or reply INTO webhook
    # return SendMessage(message.chat.id, message.text)

def register_handlers_other(dp:Dispatcher):
    dp.register_message_handler(echo_send, commands=["start", "help"])
