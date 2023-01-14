from src.fib import Fib
from src.phi import Phi
from src.game import Game


class Parser:

  def __init__(self):
    pass

  def parse_game(self, game_name):
    if game_name == "/fib":
      return Fib()
    elif game_name == "/phi":
      return Phi()

  def parse_ans(self, ans, chosen_game):
    if ans == "/end":
      chosen_game.is_running = False
      return
    elif ans == "/restart":
      chosen_game.reset()
      return
    elif chosen_game.is_correct(ans):
      return
    else:
      chosen_game.is_running = False
      return
