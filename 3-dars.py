from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command
import asyncio


bot = Bot(token='8507338761:AAG8RB35RRkCdEBw5gAV58p6QMxABn7cPcI')
dp = Dispatcher
ADMIN_ID= 6778858445
user_ids = set()


@dp.message(Command('start'))
async def start(message: types.Message):
    user_ids.add(message.from_user.id)
    await message.answer('✅Botga xuSh kelibsiz')

@dp.message()
async def xabar(message:types.Message):
    if message.from_user.id == ADMIN_ID:
        text = message.text.split('/')
        msg_id = int(text[-1])
        username = text[-2]
        for user_id in user_ids:
            await bot.copy_message(
                chat_id= user_id,
                from_chat_id= f"@{username}",
                message_id=msg_id
            )


    else:
        await message.answer("Xabarlarga ruxsat yo'q")

async def start_bot():
    print('Bot starting ... ')
    await dp.start_polling(bot)

