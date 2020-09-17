from .handlers.command_handlers import *
from .handlers.quest_callback_handlers import *
from .handlers.quest_message_handlers import *
from .handlers.crosslettering_handlers import *


def setup_handlers(dp):
    """
        Initialize message handlers here
    """
    dp.register_message_handler(start, commands=['start'], state="*")
    dp.register_message_handler(get_id, commands=['get_id'], state="*")
    dp.register_message_handler(quest, commands=['quest'], state="*")
    dp.register_message_handler(get_help, commands=['help'], state="*")
    dp.register_message_handler(get_info, commands=['info'], state="*")
    dp.register_message_handler(crosslettering, commands=['crosslettering'], state="*")
    dp.register_message_handler(exchange_crslt_info, commands=['crslt'], state="*")
    dp.register_message_handler(games, commands=['games'], state="*")
    dp.register_message_handler(letter_in_future, commands=['letter_in_future'], state="*")
    dp.register_message_handler(quarantynnyk, commands=['quarantynnyk'], state="*")
    dp.register_message_handler(memes, commands=['memes'], state="*")
    dp.register_message_handler(faculty_test, commands=['faculty_test'], state="*")
    dp.register_message_handler(change_global_state, commands=['change_state'], state="*")

    """
            Crosslettering handlers
    """
    dp.register_callback_query_handler(handle_crslt_init, lambda c: c.data == "init_crosslettering", state="*")
    dp.register_message_handler(handle_crslt_info, state=CrossletteringState.waiting_for_info,
                                content_types=types.ContentTypes.TEXT)

    """
            Quest message handlers
    """
    dp.register_message_handler(process_user_input_first_question, state=QuestState.first_question,
                                content_types=types.ContentTypes.TEXT)
    dp.register_message_handler(process_user_input_second_question, state=QuestState.second_question,
                                content_types=types.ContentTypes.TEXT)
    dp.register_message_handler(process_user_input_third_question, state=QuestState.third_question,
                                content_types=types.ContentTypes.TEXT)
    dp.register_message_handler(process_user_input_fourth_question, state=QuestState.fourth_question,
                                content_types=types.ContentTypes.TEXT)

    """
            Initialize message handlers here
    """
    dp.register_callback_query_handler(give_quest_rules, lambda c: c.data == "get_quest_rules", state="*")
    dp.register_callback_query_handler(process_quest_start, lambda c: c.data == "start_quest", state="*")
    dp.register_callback_query_handler(answer_wrong_callback, lambda c: c.data.startswith("wrong_answer"), state="*")
    dp.register_callback_query_handler(correct_answer_test, lambda c: c.data.startswith("correct_answer"),
                                       state=QuestState)
    dp.register_callback_query_handler(check_locations, lambda c: c.data == "check_locations", state="*")
