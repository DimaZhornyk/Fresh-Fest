import random

from aiogram import types

from ..__main__ import ADMINS, bot
from ..templates import *
from ..states import CrossletteringState
from ..db.db_setup import crslt


async def handle_crslt_init(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text(crslt_description()["text"], parse_mode="markdown")
    await CrossletteringState.waiting_for_info.set()


async def handle_crslt_info(message: types.Message):
    user_data = {"username": message.from_user.username, "full_name": message.from_user.full_name,
                 "tg_id": message.from_user.id, "about": message.text, "is_written_to": False}
    if await crslt.find_one({"tg_id": message.from_user.id}) is None:
        await crslt.insert_one(user_data)
    else:
        await crslt.replace_one({"tg_id": message.from_user.id}, {**user_data})

    await message.answer("Твої дані збережено:" + message.text + crslt_accepted()["text"])
    await CrossletteringState.sent.set()


async def exchange_crslt_info(message: types.Message):
    if message.from_user.id in ADMINS:
        users_data = await crslt.find().to_list(10000)
        length = len(users_data)
        pairs = []
        if length % 2 != 0:
            users_data.append({"_id": 1, "username": "bawovna",
                               "full_name": "sirna kosichka", "tg_id": 548978252,
                               "about": "Косинська Софія Марківна, вул. Незалежної України,"
                                        " +380953892787, 38 поштове відділення, м. Запоріжжя @bawowna",
                               "is_written_to": False})
            length += 1
        for user in users_data:
            send_to = random.randint(0, length - 1)
            while users_data[send_to]["tg_id"] == user["tg_id"] or users_data[send_to]["is_written_to"]:
                send_to = random.randint(0, length - 1)
            users_data[send_to]["is_written_to"] = True
            if user["tg_id"] != 1:
                try:
                    await bot.send_message(user["tg_id"],
                                           "Стій, не поспішай радіти завершенню ФФ-2020. Ти думав це все? А про листи не забув?\n"
                                           f"Інформація про людину, якій потрібно написати:\n{users_data[send_to]['about']}"
                                           f"\nНе забудь надіслати листа, бо хтось дуже чекає на нього!")
                    print(users_data[send_to]["username"])
                except:
                    pass
            pairs.append({"from": user, "to": users_data[send_to]})

        await crslt.insert_one({"data": pairs})
