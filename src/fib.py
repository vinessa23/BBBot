from src.game import Game


class Fib(Game):

  def __init__(self):
    super().__init__()
    self.n = 0
    self.m = 1
    self.counter = 0

  def init_msg(self):
    return "Welcome to Fibonacci game! \nHow to play? \nJus enter the next fibonacci number :p\nThe first 2 fibonacci number are \n0 \n1 \nI start first!"

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
    return "Game over! You got " + str(
      self.counter) + " correct answer(s)!"

  def is_correct(self, input):
    if not self.is_integer(input):
      return False

    input = int(input)

    if self.correct_ans() == input:
      self.update_num()
      self.counter += 1
      return True
    return False


# test = Fib()
# print(test.is_correct(2))
# print(test.prompt())
# print(test.is_correct("5"))
# print(test.prompt())
# print(test.is_correct(8))
# def game(self, user_ans):
#   correct_ans = True

#   while(correct_ans)
#     if user_ans == (self.n + self.m)
#       self.counter = self.counter + 1
#       self.n = self.m
#       self.m = self.m + user_ans
#       self.counter = self.counter + 1
#     else
#       correct_ans = False
#       msg = "You get a grand total of " + counter + "fibonacci number!"
