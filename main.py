from telebot import TeleBot
from telebot.types import Message
from models.text2text_model import generate_text
from config import TELEGRAM_BOT_TOKEN
from models.text_translation_model import translate_text

if TELEGRAM_BOT_TOKEN is None:
    raise FileNotFoundError("TELEGRAM_BOT_TOKEN is None\nYou should create .env.local file, and set variable "
                            "TELEGRAM_BOT_TOKEN")

bot = TeleBot(TELEGRAM_BOT_TOKEN)


@bot.message_handler(commands=['start', 'help'])
def start(message: Message):
    bot.reply_to(message, text='Привет. Я бот для вашего чата.')


@bot.message_handler(content_types=['text'])
def text_handler(message: Message):
    text = message.text

    bot.send_chat_action(message.chat.id, 'typing')
    english_text = translate_text(text, 'en')
    new_message = bot.send_message(message.chat.id, english_text, reply_to_message_id=message.message_id)

    bot.send_chat_action(message.chat.id, 'typing')
    generated_text = generate_text(english_text)
    bot.edit_message_text(generated_text, message.chat.id, new_message.message_id)

    bot.send_chat_action(message.chat.id, 'typing')
    russian_text = translate_text(generated_text, 'ru')
    bot.edit_message_text(russian_text, message.chat.id, new_message.message_id)


bot.polling(non_stop=True, skip_pending=True)
