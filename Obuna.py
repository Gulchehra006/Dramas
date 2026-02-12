from aiogram import Bot,Dispatcher,types,F
from aiogram.filters import Command
from aiogram.enums import ChatMemberStatus
import asyncio

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot(token = '8507338761:AAG8RB35RRkCdEBw5gAV58p6QMxABn7cPcI')
dp = Dispatcher()
GROUP_ID = -1003727432780

async def check_member(user_id):
    member = await bot.get_chat_member(GROUP_ID,user_id)
    return member.status !=  ChatMemberStatus.LEFT

keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Group', url = "https://t.me/+diTklkXLpmM4MjJi")],
        [InlineKeyboardButton(text='Tasdiqlash',callback_data='check')]
    ]
)


@dp.message(Command('start'))
async def start(message : types.Message):
    user_id = message.from_user.id
    if not await check_member(user_id):
        await message.answer("Siz obuna bo'lmagansiz❌ " , reply_markup=keyboard)
    else:
        await message.answer("Siz obuna bo'lgansiz✅")


@dp.callback_query(F.data == 'check')
async def checked_member(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    if not await check_member(user_id):
        await callback.answer("Siz hali obuna bo'lmagansiz ❌", show_alert=True)
    await callback.answer("Siz obuna bo'ldingiz✅")




async def start_bot():
    print("Bot starting...")
    await dp.start_polling(bot)


asyncio.run(start_bot())