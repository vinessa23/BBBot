import math
from src.game import Game


class Phi(Game):

  def __init__(self):
    super().__init__()
    self.number_left = (math.pi - 3) * 10
    self.curr_number = "3."
    self.score = 0

  def reset(self):
    self.number_left = (math.pi - 3) * 10
    self.curr_number = "3."
    self.score = 0

  def init_msg(self):
    return "Do you know your Phi?" + "\nSee how many digits you can recall!" + "\nLet's start!" + "\n\nNotes:" + "\n/restart - to restart the game" + "\n/end - to exit the game"

  def get_first_digit(self, num):
    len = int(math.log10(num))
    return num // (10**len)

  def is_integer(self, num):
    try:
      float(num)
    except ValueError:
      return False
    return float(num).is_integer()

  def is_correct(self, num):
    if not self.is_integer(num):
      return False

    num = int(num)

    if num > 9 or num < 0:
      return False

    if self.get_first_digit(self.number_left) != self.get_first_digit(num):
      return False

    self.curr_number += str(num)
    self.number_left = (self.number_left - num) * 10
    self.score += 1
    return True

  def prompt(self):
    return "Current progress: " + self.curr_number + "_" + "\nPlease enter the next number!"

  def end(self):
    if self.score == 0:
      comment = "Do you know how to play the game? :\")"
    elif self.score < 5:
      comment = "Mid."
    elif self.score < 10:
      comment = "Not bad."
    elif self.score < 50:
      comment = "Tryhard, huh."
    else:
      comment = "Congrats, I guess. Maybe, touch grass sometimes."
    return "Game over :( \nYou got " + str(
      self.score) + " digit(s) correct!" + "\n" + comment
