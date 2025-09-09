from typing import Dict, List
from src.models.sqlite.interfaces.client_interface import ClientInterface
from src.controllers.interfaces.depositer_controller_interface import DepositerControllerInterface
from src.errors.errors_types.http_bad_request import HttpBadRequestError
from src.errors.errors_types.http_not_found import HttpNotFoundError

class PessoaFisicaDepositerController(DepositerControllerInterface):
  def __init__(self, pessoa_fisica_repository: ClientInterface):
    self.__pessoa_fisica_repository = pessoa_fisica_repository

  def make_deposit(self, id: int, deposit_value: float) -> Dict:
    self.__validate_client_exists(id=id)
    self.__validate_deposit_value(deposit_value=deposit_value)
    self.__make_deposit_in_db(id=id, deposit_value=deposit_value)
    formatted_response = self.__format_response(id=id, deposit_value=deposit_value)
    return formatted_response

  def __validate_client_exists(self, id: int) -> List:
    client = self.__pessoa_fisica_repository.list_specific_client(id=id)
    if not client:
      raise HttpNotFoundError('Cliente não encontrado.')
    
  def __validate_deposit_value(self, deposit_value):
    if not isinstance(deposit_value, (int, float)):
      raise HttpBadRequestError('Valor do depósito deve ser um número.')
    
    if deposit_value <= 0:
      raise HttpBadRequestError('Valor do depósito deve ser um número maior do que zero.')

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
  