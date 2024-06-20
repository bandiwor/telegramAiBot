import os

import dotenv

dotenv.load_dotenv(".env")
dotenv.load_dotenv(".env.local")


TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
TEXT_TO_TEXT_GENERATION_MODEL_NAME = os.environ.get('TEXT_TO_TEXT_GENERATION_MODEL_NAME')
TRANSLATION_MODEL_NAME = os.environ.get('TRANSLATION_MODEL_NAME')

