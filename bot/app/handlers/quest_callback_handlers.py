import time

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from ..states import QuestState
from ..templates import *
from ..db.db_setup import users
from ..__main__ import bot


async def give_quest_rules(callback_query: types.CallbackQuery):
    await callback_query.message.answer(quest_rules()['text'], reply_markup=InlineKeyboardMarkup().add(
        InlineKeyboardButton("Так!", callback_data="start_quest")))
    await callback_query.message.delete()
    await callback_query.answer()


async def check_locations(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer(info_msg()["text"])


async def get_four_buttons_markup(answers):
    markup = InlineKeyboardMarkup(row_width=2)
    markup.row(InlineKeyboardButton(answers[0]["text"], callback_data=answers[0]["callback_data"]),
               InlineKeyboardButton(answers[1]["text"], callback_data=answers[1]["callback_data"]))
    markup.row(InlineKeyboardButton(answers[2]["text"], callback_data=answers[2]["callback_data"]),
               InlineKeyboardButton(answers[3]["text"], callback_data=answers[3]["callback_data"]))
    return markup


async def process_quest_start(callback_query: types.CallbackQuery):
    await QuestState.first_test.set()
    if await users.find_one({"tg_id": callback_query.from_user.id}) is None:
        await users.insert_one({"tg_id": callback_query.from_user.id, "username": callback_query.from_user.username,
                                "name": callback_query.from_user.full_name, "time": time.time(), "finished": False,
                                "quest_start": time.time()})
    else:
        await users.update_one({"tg_id": callback_query.from_user.id}, {"$set": {"quest_start": time.time()}})
    markup = (await get_four_buttons_markup(quest_data()[0]["answers"]))
    await callback_query.message.answer(quest_data()[0]["question"], parse_mode="markdown", reply_markup=markup)
    await callback_query.message.delete()
    await callback_query.answer()


async def answer_wrong_callback(callback_query: types.CallbackQuery):
    await callback_query.answer(callback_query.data.split("|")[1], show_alert=True)


async def correct_answer_test(callback_query: types.CallbackQuery):
    await QuestState.next()
    await callback_query.answer()
    state_num = int(callback_query.data.split('|')[1])
    await callback_query.message.answer(quest_data()[state_num]["task"],
                                        parse_mode="markdown",
                                        disable_web_page_preview=True)
    await callback_query.message.delete()
