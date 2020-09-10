from .handlers.command_handlers import *


def setup_handlers(dp):
    dp.register_message_handler(start, commands=['start'], state="*")
