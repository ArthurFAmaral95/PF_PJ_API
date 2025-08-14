from typing import Dict
from abc import ABC, abstractmethod

class WithdrawControllerInterface(ABC):
  @abstractmethod
  def make_withdrawal(self, id: int, withdraw_value: float) -> Dict:
    pass
  