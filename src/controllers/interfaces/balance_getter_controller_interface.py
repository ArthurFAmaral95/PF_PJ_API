from typing import Dict
from abc import ABC, abstractmethod

class BalanceGetterControllerInterface(ABC):
  @abstractmethod
  def get_client_balance(self, id: int) -> Dict:
    pass
