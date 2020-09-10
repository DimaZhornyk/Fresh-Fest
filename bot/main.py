import asyncio
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor

import app

# Not supported on Windows
# try:
#     import uvloop
#
#     asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
# except ImportError:
#     logging.warning('Cannot import uvloop, using asyncio event loop instead')


loop = asyncio.get_event_loop()
bot = Bot(token=app.BOT_TOKEN, loop=loop)

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

if __name__ == '__main__':
    app.setup_logging()

    # to clear previous run logs
    open('log.txt', 'w').close()

    app.setup_handlers(dp)
    executor.start_polling(dp, skip_updates=True, timeout=None)
