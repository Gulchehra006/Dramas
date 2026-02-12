import datetime
from aiogram import Bot,Dispatcher
from aiogram.filters import Command
import asyncio
TOKEN = '8507338761:AAG8RB35RRkCdEBw5gAV58p6QMxABn7cPcI'

bot = Bot(token = TOKEN)
dp = Dispatcher()

@dp.message(Command('start'))
async def salomlash(message):
    await message.answer('Assalomu alaykum.Botimizga Xush kelibsiz')

@dp.message(Command('help'))
async def yordamlashish(message):
    await message.answer('Yordam bolimiga Xush kelibsiz 🆘')

@dp.message(Command('bugun'))
async def bugun(message):
    await message.answer(f'Hozirgi Uzbekistan vaqti: {datetime.datetime.now()}')

@dp.message()
async def echo(message):
    await message.send_copy(chat_id = message.chat.id)

async def bot_start():
    print('Bot ishga tushdi!!!')

    await dp.start_polling(bot)


asyncio.run(bot_start())