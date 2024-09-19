import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

import asyncio

from config import *
from keyboards import *
import texts


logging.basicConfig(level=logging.INFO)
bot = Bot(token=API)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands='start')
async def start(message):
    await message.answer(text=texts.start, reply_markup=start_kb)


@dp.message_handler(text='О нас')
async def about(message):
    await message.answer(text=texts.about, reply_markup=start_kb)


@dp.message_handler(text='Стоимость')
async def price(message):
    await message.answer(text='Что вас интересует?', reply_markup=catalog_kb)


@dp.callback_query_handler(text='prod_first')
async def buy_p1(call):
    await call.message.answer(texts.product1, reply_markup=buy_kb)
    await call.answer()


@dp.callback_query_handler(text='prod_second')
async def buy_p2(call):
    await call.message.answer(texts.product2, reply_markup=buy_kb)
    await call.answer()


@dp.callback_query_handler(text='prod_third')
async def buy_p3(call):
    await call.message.answer(texts.product3, reply_markup=buy_kb)
    await call.answer()


@dp.callback_query_handler(text='serv_first')
async def buy_s1(call):
    await call.message.answer(texts.service1, reply_markup=buy_kb)
    await call.answer()


@dp.callback_query_handler(text='serv_second')
async def buy_s2(call):
    await call.message.answer(texts.service2, reply_markup=buy_kb)
    await call.answer()


@dp.callback_query_handler(text='serv_third')
async def buy_s3(call):
    await call.message.answer(texts.service3, reply_markup=buy_kb)
    await call.answer()


@dp.callback_query_handler(text='other')
async def buy_other(call):
    await call.message.answer(texts.other, reply_markup=buy_kb)
    await call.answer()


@dp.message_handler()
async def all_massages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
