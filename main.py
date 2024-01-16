from time import sleep

import telebot
import settings


bot = telebot.TeleBot(settings.BOT_TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    if str(message.chat.id).startswith('-'):
        bot.reply_to(message, "🧼")
    if message.from_user.is_bot:
        return None
    bot.reply_to(message, "🧼")


@bot.message_handler(content_types=['text'])
def check_mesage(message):
    block_id = int(settings.block_id) if settings.block_id.isdigit() else None
    stop_word = settings.stop_word
    if message.from_user.id == block_id and message.text.find(stop_word) != -1:
        bot.delete_message(message.chat.id, message.message_id)
    else: pass


if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as err:
            sleep(5)