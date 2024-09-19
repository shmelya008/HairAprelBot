from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Стоимость'),
         KeyboardButton(text='О нас')]
    ], resize_keyboard=True
)

catalog_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Товар_1', callback_data='prod_first')],
        [InlineKeyboardButton(text='Товар_2', callback_data='prod_second')],
        [InlineKeyboardButton(text='Товар_3', callback_data='prod_third')],
        [InlineKeyboardButton(text='Услуга_1', callback_data='serv_first')],
        [InlineKeyboardButton(text='Услуга_2', callback_data='serv_second')],
        [InlineKeyboardButton(text='Услуга_3', callback_data='serv_third')],
        [InlineKeyboardButton(text='Другие предложения', callback_data='other')]
    ]
)

buy_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Купить', url='http://ya.ru')]
    ]
)
