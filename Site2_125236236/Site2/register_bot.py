import logging

from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.dispatcher import FSMContext
from aiogram.types import ParseMode
import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, executor, types


import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Site2.settings")

import django
django.setup()

from django.contrib.auth.models import User
from asgiref.sync import sync_to_async

API_TOKEN = '5568828558:AAF7XfAkIFxfMoC-ljVLZLppR0xXlZWFA1g'

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

b1 = types.KeyboardButton('/Yes')
b2 = types.KeyboardButton('/No')
b3 = types.KeyboardButton('/Login')
b4 = types.KeyboardButton('/Password')
b5 = types.KeyboardButton('/Cancel')

key_client_1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
key_client_1.row(b1, b2)
key_client_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
key_client_2.row(b3, b4)
key_client_3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
key_client_3.add(b5)

class RegistrationForm(StatesGroup):
    login = State()
    password = State()


@dp.message_handler(commands=['Start', 'Help'])
async def command_start(message: types.Message):
    if message.text == '/start':
        await message.answer(
            'Hi %s!\nlm register bot.\nAre yor ready' % message.from_user.full_name,
            reply_markup=key_client_1
        )
    elif message.text == '/help':
        await message.answer('Write /start')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

@dp.message_handler(commands=['Yes', 'No'])
async def check_answer(message: types.Message):
    if message.text == '/Yes':
        await RegistrationForm.login.set()
        await message.reply('Write login')
    elif message.text == '/No':
        await message.answer('Are you want register?')
    else:
        markup = types.ReplyKeyboardRemove()
        await message.answer('You have account')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
