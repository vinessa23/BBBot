from abc import ABC, abstractmethod


class Game(ABC):

  def __init__(self):
    self.is_running = True

  @abstractmethod
  def init_msg(self):
    pass

  @abstractmethod
  def prompt(self):
    pass

  @abstractmethod
  def is_correct(self, input):
    pass

  @abstractmethod
  def reset(self):
    pass

  @abstractmethod
  def end(self):
    pass
