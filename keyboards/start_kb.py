from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton
from aiogram import  types



b1 = types.KeyboardButton('Добавить игроков')





Startkeyboard = ReplyKeyboardMarkup(resize_keyboard=True)

Startkeyboard.add(b1)