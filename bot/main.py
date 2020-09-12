from aiogram.utils import executor

import app

# Not supported on Windows
# try:
#     import uvloop
#
#     asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
# except ImportError:
#     logging.warning('Cannot import uvloop, using asyncio event loop instead')


if __name__ == '__main__':
    app.setup_logging()

    # to clear previous run logs
    open('log.txt', 'w').close()

    app.setup_handlers(app.dp)
    executor.start_polling(app.dp, skip_updates=True, timeout=None)
