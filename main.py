import os
import telebot
from src.game import Game
from src.parser import Parser

API_KEY = os.environ['API_KEY']
bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['start', 'help'])
def start(message):
  bot.send_message(
    message.chat.id, "Hi there! Welcome to BB Bot :)" +
    "\nBelow are the list of games we have:" + "\n  /fib" + "\n  /phi")


@bot.message_handler(commands=['fib', 'phi'])
def game(message):
  chosen_game = Parser().parse(message.text)
  bot.send_message(message.chat.id, chosen_game.init_msg())
  bot.send_message(message.chat.id, chosen_game.prompt())


@bot.message_handler(func=lambda message: True)
def echo_all(message):
  bot.send_message(message.chat.id, message.text + " too")


bot.polling()

# @bot.message_handler(commands=['games'])
# def games(message):
#   markup = types.ReplyKeyboardMarkup(row_width = 1, one_time_keyboard = True)
#   game1 = types.KeyboardButton('Do I know my Phi?', callback_data = "phi")
#   game2 = types.KeyboardButton('Leonardo Bigollo Pisano game', callback_data = "fib")
#   markup.add(game1, game2)
#   bot.send_message(message.chat.id,
#                    "Choose what you want to play:",
#                    reply_markup=markup)
