from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

b1 = KeyboardButton("/start")

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b1)