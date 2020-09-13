from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from ..db.db import set_quest_start_time
from ..states import QuestState
from ..templates import *


async def get_four_buttons_markup(answers):
    markup = InlineKeyboardMarkup(row_width=2)
    markup.row(InlineKeyboardButton(answers[0]["text"], callback_data=answers[0]["callback_data"]),
               InlineKeyboardButton(answers[1]["text"], callback_data=answers[1]["callback_data"]))
    markup.row(InlineKeyboardButton(answers[2]["text"], callback_data=answers[2]["callback_data"]),
               InlineKeyboardButton(answers[3]["text"], callback_data=answers[3]["callback_data"]))
    return markup


async def process_quest_start(callback_query: types.CallbackQuery, state: FSMContext):
    await QuestState.first_test.set()
    set_quest_start_time(callback_query.from_user.id)
    markup = (await get_four_buttons_markup(quest_data()[0]["answers"]))
    await callback_query.message.edit_text(quest_data()[0]["question"], parse_mode="markdown", reply_markup=markup)
    await callback_query.answer()


async def answer_wrong_callback(callback_query: types.CallbackQuery):
    await callback_query.answer(wrong_answer()["text"], show_alert=True)


async def correct_answer_first_test(callback_query: types.CallbackQuery):
    await QuestState.first_question.set()
    await callback_query.message.edit_text(quest_data()[0]["task"])
