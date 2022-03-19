from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
import os


from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton 

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)


answ = dict()

#Кнопка ссылка
urlkb = InlineKeyboardMarkup(row_width=2)
urlButton = InlineKeyboardButton(text='Ссылка', url='https://youtube.com')
urlButton2 = InlineKeyboardButton(text='Ссылка2', url='https://google.com')
x = [InlineKeyboardButton(text='Ссылка3', url='https://google.com'),\
	InlineKeyboardButton(text='Ссылка4', url='https://google.com'), InlineKeyboardButton(text='Ссылка5', url='https://google.com')]
urlkb.add(urlButton,urlButton2).row(*x).insert(InlineKeyboardButton(text='Ссылка6', url='https://google.com'))


@dp.message_handler(commands='ссылки')
async def url_command(message : types.Message):
	await message.answer('Ссылочки:', reply_markup=urlkb)

inkb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Like', callback_data='like_1'),\
											InlineKeyboardButton(text='Dislike', callback_data='like_-1'))

@dp.message_handler(commands='test')
async def test_command(message : types.Message):
	await message.answer('Против войны', reply_markup=inkb)

@dp.callback_query_handler(Text(startswith='like_'))
async def www_call(callback : types.CallbackQuery):
	res = int(callback.data.split('_')[1])
	if f'{callback.from_user.id}' not in answ:
		answ[f'{callback.from_user.id}'] = res
		await callback.answer('Вы проголосовали')
	else:
		await callback.answer('Вы уже проголосовали', show_alert=True)

executor.start_polling(dp, skip_updates=True)