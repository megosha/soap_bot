import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.environ.get('BOT_TOKEN')
block_id = os.environ.get('block_id')
stop_word = os.environ.get('stop_word')