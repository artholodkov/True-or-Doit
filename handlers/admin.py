from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types,Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from data_base import sqlite_db
from keyboards import admin_kb
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton 


count_players=0
class FSMAdmin(StatesGroup):
	count_players=State()
	player_1 = State()
	player_2 = State()
	player_3 = State()
	player_4 = State()
	# player_5 = State()
	# player_6 = State()
	# player_7 = State()
	# player_8 = State()
	# player_9 = State()

#Получаем ID текущего модератора
# @dp.message_handler(commands=['moderator'], is_chat_admin=True)
async def make_changes_command(message: types.Message,state: FSMContext):
	await bot.send_message(message.from_user.id, 'Сколько человек будет играть?', reply_markup=admin_kb.button_case_admin)
	await FSMAdmin.count_players.set()
	async with state.proxy() as data:
		data['count_players'] = int(message.text)	
		
	await message.delete()


#Для начала диалога загрузки нового пункта меню
# @dp.message_handler(commads='Загрузить', state=None)
async def cm_start(message : types.Message):
	await FSMAdmin.next()
	await message.reply('Напишите имя первого игрока')

#Ловим первый ответ и пишем в словарь
# @dp.message_handler(content_types=['photo'], state=FSMAdmin.photo)
async def load_name_1(message: types.Message, state: FSMContext):
		async with state.proxy() as data:
			data['player_1'] = message.text
		await FSMAdmin.next()
		await message.reply("Напишите имя второго игрока")

#Ловим второй ответ
# @dp.message_handler(state=FSMAdmin.name)
async def load_name_2(message : types.Message, state: FSMContext):
		async with state.proxy() as data:
			data['player2'] = message.text
		await FSMAdmin.next()
		await message.reply("Напишите имя третьего игрока")

#Ловим третий ответ
# @dp.message_handler(state=FSMAdmin.description)
async def load_name_3(message: types.Message, state: FSMContext):
		async with state.proxy() as data:
			data['player_3'] = message.text
		await FSMAdmin.next()
		await message.reply("Напишите имя четвертого игрока")

#Ловим четвертый ответ
# @dp.message_handler(state=FSMAdmin.price)
async def load_name_4(message: types.Message, state: FSMContext):
		async with state.proxy() as data:
			data['player_4'] = message.text
	
		await sqlite_db.sql_add_command(state)
	
		await state.finish()

#Инлайн клавиатуры для удаления позиций
@dp.callback_query_handler(lambda x: x.data and x.data.startswith('del '))
async def del_callback_run(callback_query: types.CallbackQuery):
	await sqlite_db.sql_delete_command(callback_query.data.replace('del ', ''))
	await callback_query.answer(text=f'{callback_query.data.replace("del ", "")} удалена.', show_alert=True)

# @dp.message_handler(commands='Удалить')
async def delete_item(message: types.Message):
	if message.from_user.id == ID:
		read = await sqlite_db.sql_read2()
		for ret in read:
			await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')
			await bot.send_message(message.from_user.id, text='^^^', reply_markup=InlineKeyboardMarkup().\
				add(InlineKeyboardButton(f'Удалить {ret[1]}', callback_data=f'del {ret[1]}')))	

#Выход из состояний
# @dp.message_handler(state="*", commands='отмена')
# @dp.message_handler(Text(equals='отмена', ignore_case=True), state="*")
async def cancel_handler(message: types.Message, state= FSMContext):
	if message.from_user.id == ID:
		current_state = await state.get_state()
		if current_state is None:
			return
		await state.finish()
		await message.reply('OK')

#Регистрируем хендлеры
def register_handlers_admin(dp : Dispatcher):
	dp.register_message_handler(cm_start, commands=['Загрузить'], state=None)
	dp.register_message_handler(load_name_1, state=FSMAdmin.player_1)
	dp.register_message_handler(load_name_2, state=FSMAdmin.player_2)
	dp.register_message_handler(load_name_3,state=FSMAdmin.player_3)
	dp.register_message_handler(load_name_4, state=FSMAdmin.player_4)
	dp.register_message_handler(cancel_handler, state="*", commands=['отмена'])
	dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True),state="*")	
	dp.register_message_handler(make_changes_command, commands=['moderator'], is_chat_admin=True)
	dp.register_message_handler(delete_item, commands=['Удалить'])
