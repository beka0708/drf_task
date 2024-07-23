import os
import telebot
from django.conf import settings

# API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')
bot_token = settings.TELEGRAM_BOT_TOKEN
bot = telebot.TeleBot(bot_token)


@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    bot.reply_to(message, "Hello! This is your bot speaking.")


def main():
    bot.polling()


if __name__ == "__main__":
    main()
