from typing import Dict
from src.models.sqlite.interfaces.client_interface import ClientInterface

class PessoaFisicaBalanceGetterController:
  def __init__(self, pessoa_fisica_repository: ClientInterface):
    self.__pessoa_fisica_repository = pessoa_fisica_repository

  def get_client_balance(self, id: int) -> Dict:
    balance = self.__get_balance_in_db(id=id)
    response = self.__format_response(id=id, balance=balance)
    return response

  def __get_balance_in_db(self, id: int) -> float:
    balance = self.__pessoa_fisica_repository.get_balance(id=id)

    if not balance:
      raise Exception('Saldo indisponível.')
    
    return balance
  
  def __format_response(self, id: int, balance: float) -> Dict:
    return {
      'data': {
        'type': 'Pessoa Física',
        'count': 1,
        'attributes': {
          'id': id,
          'balance': balance
        }
      }
    }