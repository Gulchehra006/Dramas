from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command
import asyncio
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


bot = Bot(token="")
dp = Dispatcher()


@dp.message(Command('start'))
async def start(message: types.Message):
    keyboards = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='Kanalga obuna bolish ✅', url='https://t.me/tursunaliyev_umar'),
            InlineKeyboardButton(text='Kanalga obuna bolish ✅', url='https://t.me/iteachstudy')
        ],
        [InlineKeyboardButton(text='Kanalga obuna bolish ✅', url='https://youtu.be/ahS8S8A4H4c?si=fLmaItRPBmOtBMij')],
    ]
    )
    await message.answer("ℹ️ Botimizdan ma'lumot olish uchun kanalimizga a'zo bo'ling.", reply_markup = keyboards)


@dp.message(Command('menu'))
async def menu(message: types.Message):
    keyboards = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='Osh 🍛', callback_data='osh'),
            InlineKeyboardButton(text='Shorva 🌯', callback_data='shorva')
        ],
        [
            InlineKeyboardButton(text='Kocha 🌮', callback_data='kocha'),
            InlineKeyboardButton(text='Lagmon 🍔', callback_data='lagmon')

        ],
    ]
    )
    await message.answer("ℹ️ Botimizdan ma'lumot olish uchun kanalimizga a'zo bo'ling.", reply_markup = keyboards)


@dp.callback_query(F.data == 'osh')
async def about_osh(callback: types.CallbackQuery):
    text = """
    Markaziy Osiyo, ayniqsa Oʻzbekistonning milliy taomi, 
u goʻsht (koʻpincha qoʻy yoki mol goʻshti), sabzi, piyoz, 
guruch, yogʻ va ziravorlar (masalan, zira) aralashmasidan 
tayyorlanadigan mashhur guruchli taomdir
    """
    await callback.message.answer(text)
    await callback.answer()


@dp.callback_query(F.data == 'shorva')
async def about_shorva(callback: types.CallbackQuery):
    text = """
    Markaziy Osiyo, ayniqsa Oʻzbekistonning milliy taomi, 
u goʻsht (koʻpincha qoʻy yoki mol goʻshti), sabzi, piyoz, 
guruch, yogʻ va ziravorlar (masalan, zira) aralashmasidan 
tayyorlanadigan mashhur guruchli taomdir
    """
    await callback.message.answer(text)
    await callback.answer()


@dp.callback_query(F.data == 'kocha')
async def about_kocha(callback: types.CallbackQuery):
    text = """
    Markaziy Osiyo, ayniqsa Oʻzbekistonning milliy taomi, 
u goʻsht (koʻpincha qoʻy yoki mol goʻshti), sabzi, piyoz, 
guruch, yogʻ va ziravorlar (masalan, zira) aralashmasidan 
tayyorlanadigan mashhur guruchli taomdir
    """
    await callback.message.answer(text)
    await callback.answer()


@dp.callback_query(F.data == 'lagmon')
async def about_lagmon(callback: types.CallbackQuery):
    text = """
    Markaziy Osiyo, ayniqsa Oʻzbekistonning milliy taomi, 
u goʻsht (koʻpincha qoʻy yoki mol goʻshti), sabzi, piyoz, 
guruch, yogʻ va ziravorlar (masalan, zira) aralashmasidan 
tayyorlanadigan mashhur guruchli taomdir(https://youtu.be/pufTbtFYP5Y?si=1PgqF_humiYMk7th)
    """
    await callback.message.answer(text)
    await callback.answer()


async def start_bot():
    print('Bot starting...')
    await dp.start_polling(bot)


asyncio.run(start_bot())