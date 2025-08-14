from typing import Dict
from abc import ABC, abstractmethod

class ListerControllerInterface(ABC):
  @abstractmethod
  def list_client(self, id: int) -> Dict:
    pass
  