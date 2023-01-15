from src.game import Game


class Fib(Game):

  def __init__(self):
    super().__init__()
    self.n = 0
    self.m = 1
    self.counter = 0

  def init_msg(self):
    return "Welcome to the Leonardo Bigollo Pisano game! \n\nHow to play? \nJust enter the next fibonacci number :p\n\nThe first 2 fibonacci number are \n0 \n1 \n\nI will play with you and I will start first!" + "\n\nNotes:" + "\n/restart - to restart the game" + "\n/end - to exit the game"

  def reset(self):
    self.n = 0
    self.m = 1
    self.counter = 0
    
  def is_integer(self, num):
    try:
      float(num)
    except ValueError:
      return False
    return float(num).is_integer()

  def correct_ans(self):
    return self.n + self.m

  def update_num(self):
    temp = self.m
    self.m = self.correct_ans()
    self.n = temp

  def prompt(self):
    self.update_num()
    return self.m

  def end(self):
    score = "Game over! You got " + str(
      self.counter) + " correct answer(s). "
    if self.counter == 0:
      comment = "You got 0. Seriously? You want play or not?"
    elif self.counter <= 5:
      comment = "Decent, I guess."
    elif self.counter <= 10:
      comment = "Keep up the good work! You have potential."
    elif self.counter <= 50:
      comment = "Einstein much?"
    else:
      comment = "I think you should get a life."
    return score + comment + "\n\nPlay again? \n/fib"

  def is_correct(self, input):
    if not self.is_integer(input):
      return False

    input = int(input)

    if self.correct_ans() == input:
      self.update_num()
      self.counter += 1
      return True
    return False
