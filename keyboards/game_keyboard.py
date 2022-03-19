from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton
from aiogram import  types



b1 = types.KeyboardButton('Правда😜')
b2 = types.KeyboardButton('Действие😉') 




Gamekeyboard = ReplyKeyboardMarkup(resize_keyboard=True)

Gamekeyboard.add(b1).add(b2)
