from .handlers.command_handlers import *
from .handlers.quest_callback_handlers import *
from .handlers.quest_message_handlers import *


def setup_handlers(dp):
    """
        Initialize message handlers here
    """
    dp.register_message_handler(start, commands=['start'], state="*")
    dp.register_message_handler(get_id, commands=['get_id'], state="*")
    dp.register_message_handler(quest, commands=['quest'], state="*")

    """
        Quest message handlers
    """
    dp.register_message_handler(process_user_input_first_question, state=QuestState.first_question,
                                content_types=types.ContentTypes.TEXT)

    """
            Initialize message handlers here
    """
    dp.register_callback_query_handler(process_quest_start, lambda c: c.data == "start_quest", state="*")
    dp.register_callback_query_handler(answer_wrong_callback, lambda c: c.data == "wrong_answer", state="*")
    dp.register_callback_query_handler(correct_answer_first_test, lambda c: c.data == "correct_answer_1",
                                       state=QuestState.first_test)
