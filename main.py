import os
import telebot

API_KEY = os.environ['API_KEY']
bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['start', 'help'])
def start(message):
  bot.reply_to(
    message,
    "Hi there! Welcome to BB Bot :) \nThis should start in a new line")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
  bot.reply_to(message, message.text)


bot.polling()
