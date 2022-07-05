from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

b1 = KeyboardButton("/start")

kb_client = ReplyKeyboardMarkup()

kb_client.add(b1)