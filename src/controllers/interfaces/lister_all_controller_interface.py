from typing import Dict
from abc import ABC, abstractmethod

class ListerAllControllerInterface(ABC):
  @abstractmethod
  def list_all(self) -> Dict:
    pass
  