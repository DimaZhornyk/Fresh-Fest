import os
import pathlib

from dotenv import load_dotenv

load_dotenv(dotenv_path=pathlib.Path(__file__).parent.parent / '.env')

BOT_TOKEN = os.getenv("BOT_TOKEN")

API_URL = os.getenv("API_URL")

LOG_FILE = os.getenv('LOG_FILE')
