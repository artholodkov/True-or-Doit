import sqlite3 as sq 
from create_bot import bot

def sql_start():
	global base, cur
	base = sq.connect('players.db')
	cur = base.cursor()
	if base:
		print('Data base connected OK!')
	base.execute('CREATE TABLE IF NOT EXISTS menu(player_1 TEXT, player_2 TEXT, player_3 TEXT, player_4 TEXT)')
	base.commit()

async def sql_add_command(state):
	async with state.proxy() as data:
		cur.execute('UPDATE menu SET  player_1=?, player_2=?, player_3=?, player_4=?', tuple(data.values()))
		base.commit()


async def sql_read(message,index):
	for ret in cur.execute('SELECT * FROM menu').fetchall():
		await bot.send_message(message.from_user.id, ret[index])
		return len(ret)
		

async def sql_read2():
	return cur.execute('SELECT * FROM menu').fetchall()

async def sql_delete_command(data):
	cur.execute('DELETE FROM menu WHERE name == ?', (data,))
	base.commit()
