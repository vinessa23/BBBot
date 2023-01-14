class Fib:
  def __init__(self):
    self.n = 0
    self.m = 1
    self.counter = 2

  def init_msg(self):
    return "Welcome to Fibonacci game! \nHow to play? \nJus enter the next fibonacci number :p"

  def correct_ans(self):
    return self.n + self.m
    
  def is_correct(self, user_ans):
    if self.correct_ans() == user_ans
      self.counter = self.counter + 1
      update_num()
      return prompt()
    return end()

  def update_num(self):
    self.m = self.correct_ans()
    self.n = self.m
    self.counter = self.counter + 1

  def prompt(self):
    print(self.m)

  def end(self):
    print("Game over! You get a grand total of " + self.counter + " fibonacci number")

test = Fib()
print(test.is_correct(1))
print(test.is_correct(3))
    
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

  
  
        
    
    