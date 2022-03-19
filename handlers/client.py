import string
from aiogram import types, Dispatcher
from QuestionFabric.TruethGeneration import CheckRepeats, GetRandDigit, Parse
from create_bot import dp, bot
from keyboards import game_keyboard as gkb
from keyboards import start_kb as skb
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db
from aiogram.dispatcher.filters import Text
import  QuestionFabric  



# Клиентская часть

list_questions=Parse('C:\\telegram_bot\\QuestionFabric\\Questions.txt')
list_case=Parse('C:\\telegram_bot\\QuestionFabric\\do.txt')
#list_users=list()
index_user=0

@dp.message_handler(commands=['start','help'])
async def commands_start(message : types.Message):
		await bot.send_message(message.from_user.id, 'Введите имена игроков через запятую, да начнется игра!', reply_markup=skb.Startkeyboard)
		await message.delete()




@dp.message_handler((Text(equals="Добавить игроков")))
async def commands_start(message : types.Message):
		await bot.send_message(message.from_user.id, 'Отлично, Начинаем игру Правда или действие!',reply_markup=gkb.Gamekeyboard)
#		list_users=(message.text).split(',')
#		await bot.send_message(message.from_user.id,list_users[index_user]+' Твой ход братик', reply_markup=gkb.Gamekeyboard)
		#index_user+=1
		#if(index_user>len(list_users)-1):
	#		index_user=0;


@dp.message_handler(Text(equals="Правда😜"))
async def Trueth_Command(message : types.Message):
	digit=GetRandDigit(0,len(list_questions))
	question_cash=list()
	if CheckRepeats(list_questions[digit],question_cash):
		digit=GetRandDigit(0,len(list_questions))
	await message.answer(list_questions[digit])
#	await bot.send_message(message.from_user.id,list_users[index_user]+' Твой ход братик', reply_markup=gkb.Gamekeyboard)
	#index_user+=1
	#if(index_user>len(list_users)-1):
	#	index_user=0;



@dp.message_handler(Text(equals="Действие😉"))
async def Do_Command(message : types.Message):
	digit=GetRandDigit(0,len(list_case))
	cash=list()
	if CheckRepeats(list_case[digit],cash):
		digit=GetRandDigit(0,len(list_case))
	await message.answer(list_case[digit])
#	await bot.send_message(message.from_user.id,list_users[index_user]+' Твой ход братик', reply_markup=gkb.Gamekeyboard)
	#index_user+=1
	#if(index_user>len(list_users)-1):
	#	index_user=0;


def register_handlers_client(dp : Dispatcher):
	dp.register_message_handler(commands_start, commands=['start','help'])
	

