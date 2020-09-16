import time

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from ..__main__ import IS_STARTED
from ..templates import *
from ..db.db_setup import users


async def start(message: types.Message):
    await message.answer("Introduction")
    if await users.find_one({"tg_id": message.from_user.id}) is None:
        await users.insert_one({"tg_id": message.from_user.id, "username": message.from_user.username,
                                "name": message.from_user.full_name, "time": time.time(), "finished": False})


async def get_help(message: types.Message):
    await message.answer(help_msg()["text"])


async def get_id(message: types.Message):
    await message.answer(message.from_user.id)


async def quest(message: types.Message, state: FSMContext):
    if IS_STARTED:
        if (await users.find_one({"tg_id": message.from_user.id}))["finished"]:
            await message.answer(already_completed_msg()["text"], parse_mode="markdown")
        else:
            await message.answer(start_msg()["text"], reply_markup=InlineKeyboardMarkup().add(
                InlineKeyboardButton("Так!", callback_data="get_quest_rules")), parse_mode="markdown",
                                 disable_web_page_preview=True)
    else:
        await message.answer("Всьому свій час, володаре...")


async def crosslettering(message: types.Message):
    await message.answer(crslt_info()["text"], reply_markup=InlineKeyboardMarkup().add(
        InlineKeyboardButton("Хочу написати листа!", callback_data="init_crosslettering")))


async def get_info(message: types.Message):
    await message.answer(info_msg()["text"])


async def games(message: types.Message):
    await message.answer(games_msg()["text"], parse_mode="markdown", disable_web_page_preview=True)


async def letter_in_future(message: types.Message):
    await message.answer(letter_in_future_msg()["text"], parse_mode="markdown", disable_web_page_preview=True)


async def faculty_test(message: types.Message):
    await message.answer(faculty_test_msg()["text"], parse_mode="markdown", disable_web_page_preview=True)


async def quarantynnyk(message: types.Message):
    await message.answer(quarantynnyk_msg()["text"], parse_mode="markdown", disable_web_page_preview=True)


async def memes(message: types.Message):
    await message.answer(memes_msg()["text"], parse_mode="markdown", disable_web_page_preview=True)
