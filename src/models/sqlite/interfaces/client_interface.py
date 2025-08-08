from abc import ABC, abstractmethod
from typing import List

class ClientInterface(ABC):
  @abstractmethod
  def list_all_clients(self) -> List:
    pass

  @abstractmethod
  def list_specific_client(self, id: int) -> List:
    pass

  @abstractmethod
  def insert_client(self) -> None:
    pass

  @abstractmethod
  def get_balance(self, id: int) -> int:
    pass

  @abstractmethod
  def deposit(self, id: int, deposit_value: float) -> None:
    pass

  @abstractmethod
  def withdraw(self, id: int, withdraw_value: float) -> None:
    pass
  