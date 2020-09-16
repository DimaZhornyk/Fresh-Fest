import time

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from .quest_callback_handlers import get_four_buttons_markup
from ..states import QuestState
from ..templates import *
from ..db.db_setup import users


async def process_user_input_first_question(message: types.Message, state: FSMContext):
    state_num = 0
    await process_user_input(state_num, message, state)


async def process_user_input_second_question(message: types.Message, state: FSMContext):
    state_num = 1
    await process_user_input(state_num, message, state)


async def process_user_input_third_question(message: types.Message, state: FSMContext):
    state_num = 2
    await process_user_input(state_num, message, state)


async def process_user_input_fourth_question(message: types.Message, state: FSMContext):
    state_num = 3
    await process_user_input(state_num, message, state)


async def process_user_input(state_num: int, message: types.Message, state: FSMContext):
    if message.text.lower() in quest_data()[state_num]["ans"]:
        if state_num == 3:
            await message.answer(finish_gratz()["text"], reply_markup=InlineKeyboardMarkup().add(
                InlineKeyboardButton("Подивитися локації", callback_data="check_locations")),
                                 parse_mode="markdown")
            user_data = await users.find_one({"tg_id": message.from_user.id})
            await users.update_one({"tg_id": message.from_user.id}, {"$set":
                                                                         {"quest_finish": time.time(), "finished": True,
                                                                          "quest_time": time.time() - user_data[
                                                                              "quest_start"]}})
        else:
            await state.update_data(wrong_answers=0)
            await QuestState.next()
            await message.answer(congratulations_msgs()[state_num]["text"])
            markup = (await get_four_buttons_markup(quest_data()[state_num + 1]["answers"]))
            await message.answer(quest_data()[state_num + 1]["question"], reply_markup=markup, parse_mode="markdown",
                                 disable_web_page_preview=True)
    else:
        data = await state.get_data()
        if "wrong_answers" in data.keys() and data["wrong_answers"] >= 1:
            await state.update_data(wrong_answers=data["wrong_answers"] + 1)
            await message.answer(second_tips()[state_num]["text"])
        else:
            await state.update_data(wrong_answers=1)
            await message.answer(wrong_answer_msg()["text"])
