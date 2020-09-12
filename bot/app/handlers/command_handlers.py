from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from ..__main__ import IS_STARTED
from ..templates import *


async def start(message: types.Message):
    if IS_STARTED:
        await message.answer("Introduction")
    else:
        await message.answer("Всьому свій час, володаре...")


async def get_id(message: types.Message):
    await message.answer(message.from_user.id)


async def quest(message: types.Message):
    await message.answer(start_msg()["text"], reply_markup=InlineKeyboardMarkup().add(
        InlineKeyboardButton("Почати!", callback_data="start_quest")))


async def info(message: types.Message):
    await message.answer(info_msg()["text"])
