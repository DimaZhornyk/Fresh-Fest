from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from ..__main__ import IS_STARTED
from ..templates import *
from ..db.db_setup import users


async def start(message: types.Message):
    if IS_STARTED:
        await message.answer("Introduction")
        if await users.find_one({"tg_id": message.from_user.id}) is None:
            await users.insert_one({"tg_id": message.from_user.id, "username": message.from_user.username})
    else:
        await message.answer("Всьому свій час, володаре...")


async def get_id(message: types.Message):
    await message.answer(message.from_user.id)


async def quest(message: types.Message):
    await message.answer(start_msg()["text"], reply_markup=InlineKeyboardMarkup().add(
        InlineKeyboardButton("Почати!", callback_data="start_quest")), parse_mode="markdown")


async def crosslettering(message: types.Message):
    await message.answer(crslt_info()["text"], reply_markup=InlineKeyboardMarkup().add(
        InlineKeyboardButton("ХАЧЮ НАПИСАТИ КОМУСЬ ЛИСТ", callback_data="init_crosslettering")), parse_mode="markdown")


async def info(message: types.Message):
    await message.answer(info_msg()["text"])
