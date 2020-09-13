from aiogram.dispatcher.filters.state import StatesGroup, State


class QuestState(StatesGroup):
    first_test = State()
    first_question = State()
    second_test = State()
    second_question = State()
    third_test = State()
    third_question = State()
    completed = State()


class CrossletteringState(StatesGroup):
    waiting_for_info = State()
    sent = State()
