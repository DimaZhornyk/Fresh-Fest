import logging

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from .config import LOG_FILE


def setup_logging():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                        filename=LOG_FILE,
                        filemode='a')


def get_basic_games_msg_template():
    markup = InlineKeyboardMarkup(row_width=2)
    markup.insert(InlineKeyboardButton("Сервер в діскорді", "https://discord.gg/9fYEw4"))
    markup.insert(InlineKeyboardButton("Список ігор", callback_data="get_games_list"))
    markup.insert(InlineKeyboardButton("Інструкція з Discord",
                                       "https://telegra.ph/%D0%86nstrukc%D1%96ya-z-koristuvannya-Discord-09-17"))
    return markup


def get_server_link_markup():
    markup = InlineKeyboardMarkup()
    markup.insert(InlineKeyboardButton("Jackbox", callback_data="get_game_description|0|False"))
    markup.insert(InlineKeyboardButton("Крокодил", callback_data="get_game_description|1|False"))
    markup.insert(
        InlineKeyboardButton("Keep Talking and Nobody Explodes", callback_data="get_game_description|2|False"))
    markup.insert(InlineKeyboardButton("Minecraft", callback_data="get_game_description|3|False"))
    markup.insert(InlineKeyboardButton("Мафія", callback_data="get_game_description|4|False"))
    markup.insert(InlineKeyboardButton("Сервер в діскорді", "https://discord.gg/9fYEw4"))
    markup.insert(InlineKeyboardButton("Назад", callback_data="back_to_games_basic_menu"))
    return markup
