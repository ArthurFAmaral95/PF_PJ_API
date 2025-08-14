from typing import Dict
from abc import ABC, abstractmethod

class CreatorControllerInterface(ABC):
  @abstractmethod
  def create(self, client_info: Dict) -> Dict:
    pass
  