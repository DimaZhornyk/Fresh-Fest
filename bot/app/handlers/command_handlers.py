import csv
import time

from ..utilities import get_basic_games_msg_template
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from ..__main__ import started, quest_is_active, stream_link, MAIN_ADMIN, ADMINS, bot
from ..templates import *
from ..db.db_setup import users


async def start(message: types.Message):
    if not started:
        await forbid_message(message)
        if await users.find_one({"tg_id": message.from_user.id}) is None:
            await users.insert_one({"tg_id": message.from_user.id, "username": message.from_user.username,
                                    "name": message.from_user.full_name, "time": time.time(), "finished": False})
    else:
        await message.answer(start_msg()["text"], disable_web_page_preview=True)
        await message.answer("Хутчіш натискай /quest та починай свою подорож!")
        if await users.find_one({"tg_id": message.from_user.id}) is None:
            await users.insert_one({"tg_id": message.from_user.id, "username": message.from_user.username,
                                    "name": message.from_user.full_name, "time": time.time(), "finished": False})


async def get_help(message: types.Message):
    await message.answer(help_msg()["text"])


async def so(message: types.Message):
    if not started:
        await forbid_message(message)
    else:
        await message.answer(so_msg()["text"], parse_mode="markdown")


async def get_id(message: types.Message):
    if not started:
        await forbid_message(message)
    else:
        await message.answer(message.from_user.id)


async def quest(message: types.Message, state: FSMContext):
    if not started:
        await forbid_message(message)
    else:
        if await users.find_one({"tg_id": message.from_user.id}) is not None and \
                (await users.find_one({"tg_id": message.from_user.id}))["finished"]:
            await message.answer(already_completed_msg()["text"], parse_mode="markdown")
        else:
            if quest_is_active:
                await message.answer(start_quest_msg()["text"], reply_markup=InlineKeyboardMarkup().add(
                    InlineKeyboardButton("Так!", callback_data="get_quest_rules")), parse_mode="markdown",
                                     disable_web_page_preview=True)
            else:
                await message.answer("На жаль, квест уже закінчився(")


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
        await message.answer_photo(games_msg()["photo"], games_msg()["text"],
                                   reply_markup=get_basic_games_msg_template(), parse_mode="markdown")


async def letter_in_future(message: types.Message):
    if not started:
        await forbid_message(message)
    else:
        await message.answer_photo(letter_in_future_msg()["photo"], letter_in_future_msg()["text"],
                                   parse_mode="markdown")


async def tests(message: types.Message):
    if not started:
        await forbid_message(message)
    else:
        await message.answer_photo(tests_msg()["photo"], tests_msg()["text"], parse_mode="markdown")


async def quarantynnyk(message: types.Message):
    if not started:
        await forbid_message(message)
    else:
        await message.answer_photo(quarantynnyk_msg()["photo"], quarantynnyk_msg()["text"], parse_mode="markdown")


async def memes(message: types.Message):
    if not started:
        await forbid_message(message)
    else:
        await message.answer_photo(memes_msg()["photo"], memes_msg()["text"], parse_mode="markdown")


async def forbid_message(message: types.Message):
    await message.answer_photo(forbid_msg()["photo"], forbid_msg()["text"], parse_mode="markdown")


async def get_all_people_who_completed_quest(message: types.Message):
    if message.from_user.id in ADMINS:
        cursor = users.find({"finished": True})
        cursor.sort('quest_time', 1)
        with open('users.csv', 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            async for document in cursor:
                try:
                    spamwriter.writerow(
                        [document["tg_id"], "@" + document["username"], document["name"], document["quest_time"]])
                except Exception as e:
                    print(e)
                    pass
        await message.answer_document(types.InputFile("users.csv"))


async def giveaway_spam(message: types.Message):
    if message.from_user.id in ADMINS:
        async for document in users.find():
            try:
                await bot.send_photo(document["tg_id"], giveaway_spam_msg()["photo"],
                                     giveaway_spam_msg()["text"] + stream_link, parse_mode="markdown")
            except Exception as e:
                print(e)
                pass


async def karantinnik_spam(message: types.Message):
    if message.from_user.id in ADMINS:
        async for document in users.find():
            try:
                await bot.send_photo(document["tg_id"], karantinnik_spam_msg()["photo"],
                                     karantinnik_spam_msg()["text"] + stream_link,
                                     parse_mode="markdown")
            except Exception as e:
                print(e)
                pass


async def send_to_all(message: types.Message):
    if message.from_user.id in ADMINS:
        async for document in users.find():
            try:
                await bot.send_message(document["tg_id"], message.text.split("/all ")[1], parse_mode="markdown")
            except Exception as e:
                print(e)
                pass


async def end_quest(message: types.Message):
    if message.from_user.id in ADMINS:
        global quest_is_active
        quest_is_active = not quest_is_active
        await message.answer(str(quest_is_active))


async def ff_end(message: types.Message):
    if message.from_user.id in ADMINS:
        async for document in users.find():
            try:
                await bot.send_photo(document["tg_id"], ff_end_msg()["photo"], ff_end_msg()["text"],
                                     parse_mode="markdown")
            except Exception as e:
                print(e)
                pass


async def set_stream_link(message: types.Message):
    if message.from_user.id in ADMINS:
        global stream_link
        stream_link = message.text.split("/set_link ")[1]
        await message.answer(stream_link)


async def change_global_state(message: types.Message):
    if message.from_user.id in ADMINS:
        global started
        async for document in users.find():
            try:
                await bot.send_message(document["tg_id"], start_msg()["text"], disable_web_page_preview=True)
                await bot.send_message(document["tg_id"], "Хутчіш натискай /quest та починай свою подорож!")
            except Exception as e:
                print(e)
                pass

        started = not started
        await message.answer(str(started))
