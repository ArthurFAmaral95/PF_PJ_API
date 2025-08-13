from typing import Dict
from src.models.sqlite.interfaces.client_interface import ClientInterface

class PessoaJuridicaBalanceGetterController:
  def __init__(self, pessoa_juridica_repository: ClientInterface):
    self.__pessoa_juridica_repository = pessoa_juridica_repository

  def get_client_balance(self, id: int) -> Dict:
    balance = self.__get_balance_in_db(id=id)
    formatted_response = self.__format_response(id=id, balance=balance)

    return formatted_response

  def __get_balance_in_db(self, id: int) -> float:
    balance = self.__pessoa_juridica_repository.get_balance(id=id)

    if not balance:
      raise Exception('Saldo não disponível.')
    
    return balance
  
  def __format_response(self, id: int, balance: float) -> Dict:
    return {
      'data': {
        'type': 'Pessoa Jurídica',
        'count': 1,
        'attributes': {
          'id': id,
          'balance': balance
        }
      }
    }
  