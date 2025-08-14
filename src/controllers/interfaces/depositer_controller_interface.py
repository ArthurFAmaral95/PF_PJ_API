from typing import Dict
from abc import ABC, abstractmethod

class DepositerControllerInterface(ABC):
  @abstractmethod
  def make_deposit(self, id: int, deposit_value: float) -> Dict:
    pass
  