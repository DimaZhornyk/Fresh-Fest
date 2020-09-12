from aiogram import types

from ..states import QuestState
from ..templates import *


async def process_user_input_first_question(message: types.Message):
    if message.text == quest_data()[0]["answer"]:
        await QuestState.second_question.set()
        await message.answer(quest_data()[1]["question"])
    else:
        await message.answer(wrong_answer()["text"])
