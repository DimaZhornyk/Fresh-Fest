import asyncio
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import app

started = False
quest_is_active = True
stream_link = ""

MAIN_ADMIN = 403316002
ADMINS = [403316002, 189284169, 330644315]

sniffers = [241629528, 403316002]

loop = asyncio.get_event_loop()
bot = Bot(token=app.BOT_TOKEN, loop=loop)

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
