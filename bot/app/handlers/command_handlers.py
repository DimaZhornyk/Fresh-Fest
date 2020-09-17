import time

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from ..__main__ import started
from ..templates import *
from ..db.db_setup import users


async def start(message: types.Message):
    if not started:
        await forbid_message(message)
        if await users.find_one({"tg_id": message.from_user.id}) is None:
            await users.insert_one({"tg_id": message.from_user.id, "username": message.from_user.username,
                                    "name": message.from_user.full_name, "time": time.time(), "finished": False})
    else:
        await message.answer("Introduction")
        if await users.find_one({"tg_id": message.from_user.id}) is None:
            await users.insert_one({"tg_id": message.from_user.id, "username": message.from_user.username,
                                    "name": message.from_user.full_name, "time": time.time(), "finished": False})


async def get_help(message: types.Message):
    await message.answer(help_msg()["text"])


async def get_id(message: types.Message):
    if not started:
        await forbid_message(message)
    else:
        await message.answer(message.from_user.id)


async def quest(message: types.Message, state: FSMContext):
    if not started:
        await forbid_message(message)
    else:
        if (await users.find_one({"tg_id": message.from_user.id}))["finished"]:
            await message.answer(already_completed_msg()["text"], parse_mode="markdown")
        else:
            await message.answer(start_msg()["text"], reply_markup=InlineKeyboardMarkup().add(
                InlineKeyboardButton("Так!", callback_data="get_quest_rules")), parse_mode="markdown",
                                 disable_web_page_preview=True)


async def crosslettering(message: types.Message):
    if not started:
        await forbid_message(message)
    else:
        await message.answer_photo(crslt_info()["photo"])
        await message.answer(crslt_info()["text"], reply_markup=InlineKeyboardMarkup().add(
            InlineKeyboardButton("Хочу написати листа!", callback_data="init_crosslettering")))


async def get_info(message: types.Message):
    if not started:
        await forbid_message(message)
    else:
        await message.answer(info_msg()["text"])


async def games(message: types.Message):
    if not started:
        await forbid_message(message)
    else:
        await message.answer_photo(games_msg()["photo"], games_msg()["text"], parse_mode="markdown")


async def letter_in_future(message: types.Message):
    if not started:
        await forbid_message(message)
    else:
        await message.answer_photo(letter_in_future_msg()["photo"], letter_in_future_msg()["text"],
                                   parse_mode="markdown")


async def faculty_test(message: types.Message):
    if not started:
        await forbid_message(message)
    else:
        await message.answer_photo(faculty_test_msg()["photo"], faculty_test_msg()["text"], parse_mode="markdown")


async def quarantynnyk(message: types.Message):
    if not started:
        await forbid_message(message)
    else:
        await message.answer(quarantynnyk_msg()["text"], parse_mode="markdown", disable_web_page_preview=True)


async def memes(message: types.Message):
    if not started:
        await forbid_message(message)
    else:
        await message.answer_photo(memes_msg()["photo"], memes_msg()["text"], parse_mode="markdown")


async def forbid_message(message: types.Message):
    await message.answer_photo(forbid_msg()["photo"], forbid_msg()["text"], parse_mode="markdown")


async def change_global_state(message: types.Message):
    global started
    started = not started
    await message.answer("started now is: ")
