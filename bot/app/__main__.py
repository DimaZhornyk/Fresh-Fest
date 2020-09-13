import asyncio
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import app

IS_STARTED = True
MAIN_ADMIN = 403316002

loop = asyncio.get_event_loop()
bot = Bot(token=app.BOT_TOKEN, loop=loop)

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
