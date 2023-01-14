from src.game import Game

class Fib(Game):
  
  def __init__(self):
    self.n = 0
    self.m = 1
    self.counter = 2

  def init_msg(self):
    return "Welcome to Fibonacci game! \nHow to play? \nJus enter the next fibonacci number :p\nLet's start! \n0 \n1"

  def correct_ans(self):
    return self.n + self.m

  def update_num(self):
    temp = self.m
    self.m = self.correct_ans()
    self.n = temp
    self.counter = self.counter + 1

  def prompt(self):
    return str(self.m)

  def end(self):
    return "Game over! You get a grand total of " + str(self.counter) + " fibonacci number"
    
  def is_correct(self, input):
    if self.correct_ans() == input:
      self.counter = self.counter + 1
      self.update_num()
      return True
    return False



# test = Fib()
# print(test.is_correct(1))
# print(test.prompt())
# print(test.is_correct(2))
# print(test.prompt())
# print(test.is_correct(3))
    
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

  
  
        
    
    