from typing import Dict
from src.models.sqlite.interfaces.client_interface import ClientInterface

class PessoaJuridicaDepositerController:
  def __init__(self, pessoa_juridica_repository: ClientInterface):
    self.__pessoa_juridica_repository = pessoa_juridica_repository

  def make_deposit(self, id: int, deposit_value: float) -> Dict:
    self.__validate_deposit_value(deposit_value=deposit_value)
    self.__make_deposit_in_db(id=id, deposit_value=deposit_value)
    formatted_response = self.__format_response(id=id, deposit_value=deposit_value)

    return formatted_response

  def __validate_deposit_value(self, deposit_value) -> None:
    if not isinstance(deposit_value, (int, float)):
      raise ValueError('Valor do depósito deve ser um número.')

    if deposit_value <= 0:
      raise ValueError('Valor do depósito deve ser um número maior do que zero.')

  def __make_deposit_in_db(self, id: int, deposit_value: float) -> None:
    self.__pessoa_juridica_repository.deposit(id=id, deposit_value=deposit_value)

  def __format_response(self, id: int, deposit_value) -> Dict:
    return {
      'data': {
        'type': 'Pessoa Jurídica',
        'count': 1,
        'attributes': {
          'status': 'success',
          'id': id,
          'deposit_value': deposit_value
        }
      }
    }
  