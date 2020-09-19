from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from ..templates import *
from ..utilities import get_basic_games_msg_template, get_server_link_markup


async def handle_give_server_link_callback(callback_query: types.CallbackQuery):
    markup = InlineKeyboardMarkup(row_width=2)
    markup.insert(InlineKeyboardButton("Інструкція з Discord",
                                       "https://telegra.ph/%D0%86nstrukc%D1%96ya-z-koristuvannya-Discord-09-17"))
    markup.insert(InlineKeyboardButton("Список ігор", callback_data="get_games_list"))
    markup.insert(InlineKeyboardButton("Назад", callback_data="back_to_games_basic_menu"))
    await callback_query.message.answer(discord_link_msg()["text"], reply_markup=markup, parse_mode="markdown")
    await callback_query.message.delete()
    await callback_query.answer()


async def back_to_games_default_menu(callback_query: types.CallbackQuery):
    await callback_query.message.answer_photo(games_msg()["photo"], games_msg()["text"],
                                              reply_markup=get_basic_games_msg_template(), parse_mode="markdown")
    await callback_query.message.delete()
    await callback_query.answer()


async def handle_get_games_list_callback(callback_query: types.CallbackQuery):
    markup = InlineKeyboardMarkup(row_width=1)
    markup.insert(InlineKeyboardButton("Jackbox", callback_data="get_game_description|0|True"))
    markup.insert(InlineKeyboardButton("Крокодил", callback_data="get_game_description|1|True"))
    markup.insert(InlineKeyboardButton("Keep Talking and Nobody Explodes", callback_data="get_game_description|2|True"))
    markup.insert(InlineKeyboardButton("Minecraft", callback_data="get_game_description|3|True"))
    markup.insert(InlineKeyboardButton("Мафія", callback_data="get_game_description|4|True"))
    markup.insert(InlineKeyboardButton("Назад", callback_data="back_to_games_basic_menu"))
    await callback_query.message.answer(
        f"Загальна інструкція {link('тут', 'https://telegra.ph/%D0%86nstrukc%D1%96ya-po-%D1%96grah-09-18')}, "
        "щоб переглянути інструкцію конкретної гри, натискай на одну з кнопок:",
        reply_markup=markup, parse_mode="markdown")
    await callback_query.message.delete()
    await callback_query.answer()


async def handle_get_game_description(callback_query: types.CallbackQuery):
    game_id = int(callback_query.data.split("|")[1])
    delete_prev = callback_query.data.split("|")[2]
    if len(games_descriptions()[game_id]["photos"]) > 1:
        media = types.MediaGroup()
        for photo in games_descriptions()[game_id]["photos"]:
            media.attach_photo(photo)
        await callback_query.message.answer_media_group(media)
        await callback_query.message.answer(games_descriptions()[game_id]["text"],
                                            reply_markup=get_server_link_markup(), parse_mode="markdown")
    elif len(games_descriptions()[game_id]["photos"]) == 1:
        await callback_query.message.answer_photo(games_descriptions()[game_id]["photos"][0])
        await callback_query.message.answer(games_descriptions()[game_id]["text"],
                                            reply_markup=get_server_link_markup(), parse_mode="markdown")
    else:
        await callback_query.message.answer(games_descriptions()[game_id]["text"],
                                            reply_markup=get_server_link_markup(), parse_mode="markdown")
    if delete_prev == "True":
        await callback_query.message.delete()
    await callback_query.answer()
