from typing import Dict
from src.models.sqlite.interfaces.client_interface import ClientInterface

class PessoaFisicaDepositerController:
  def __init__(self, pessoa_fisica_repository: ClientInterface):
    self.__pessoa_fisica_repository = pessoa_fisica_repository

  def make_deposit(self, id: int, deposit_value: float) -> Dict:
    self.__validate_deposit_value(deposit_value=deposit_value)
    self.__make_deposit_in_db(id=id, deposit_value=deposit_value)
    formatted_response = self.__format_response(id=id, deposit_value=deposit_value)
    return formatted_response

  def __validate_deposit_value(self, deposit_value):
    if not isinstance(deposit_value, (int, float)):
      raise ValueError('Valor do depósito deve ser um número.')

  def __make_deposit_in_db(self, id: int, deposit_value: float) -> None:
    self.__pessoa_fisica_repository.deposit(id=id, deposit_value=deposit_value)
  
  def __format_response(self, id: int, deposit_value: float) -> Dict:
    return {
      'data': {
        'type': 'Pessoa Física',
        'count': 1,
        'attributes': {
          'status': 'success',
          'id': id,
          'deposit_value': deposit_value
        }
      }
    }
  