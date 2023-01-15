import os
import telebot
from src.game import Game
from src.parser import Parser

API_KEY = os.environ['API_KEY']
bot = telebot.TeleBot(API_KEY)
parser = Parser()


@bot.message_handler(commands=['start', 'help'])
def start(message):
  bot.send_message(
    message.chat.id,
    "Hi there! Welcome to BB Bot :)" + "\nYou must've been really bored, huh?"
    "\nHere are the list of games we have:" + "\n  /fib" + "\n  /phi")


@bot.message_handler(commands=['fib', 'phi'])
def game(message):
  chosen_game = parser.parse_game(message.text)
  bot.send_message(message.chat.id, chosen_game.init_msg())
  msg = bot.send_message(message.chat.id, chosen_game.prompt())
  bot.register_next_step_handler(msg, process_ans, chosen_game)


def process_ans(message, chosen_game):
  parser.parse_ans(message.text, chosen_game)
  if not chosen_game.is_running:
    bot.send_message(message.chat.id, chosen_game.end())
  else:
    msg = bot.send_message(message.chat.id, chosen_game.prompt())
    bot.register_next_step_handler(msg, process_ans, chosen_game)


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
