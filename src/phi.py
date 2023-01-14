import math


class Phi:

  def __init__(self):
    self.number_left = (math.pi - 3) * 10
    self.curr_number = "3."

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
    if num > 9 or num < 0:
      return False
    if self.get_first_digit(self.number_left) != self.get_first_digit(num):
      return False
    self.curr_number += str(num)
    self.number_left = (self.number_left - num) * 10
    return True

  def prompt(self):
    return "Current progress: " + self.curr_number + "_" + "\nPlease enter the next number!"


# test = Phi()
# print(test.is_correct(1))
# print(test.prompt())
# print(test.is_correct(4))
# print(test.prompt())
# print(test.is_correct(1))
# print(test.prompt())
# print(test.is_correct(5))
# print(test.prompt())
# print(test.is_correct(1))
# print(test.prompt())
