from src.fib import Fib
from src.phi import Phi

class Parser:
  def __init__(self) :
    pass
    
  def parse(self, game_name) :
    if game_name == "/fib" :
      return Fib()
    elif game_name == "/phi" :
      return Phi()

    