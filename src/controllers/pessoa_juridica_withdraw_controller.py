from typing import Dict
from src.models.sqlite.interfaces.client_interface import ClientInterface
from src.controllers.interfaces.withdraw_controller_interface import WithdrawControllerInterface
from src.errors.errors_types.http_bad_request import HttpBadRequestError

class PessoaJuridicaWithdrawController(WithdrawControllerInterface):
  def __init__(self, pessoa_juridica_repository: ClientInterface):
    self.__pessoa_juridica_repository = pessoa_juridica_repository

  def make_withdrawal(self, id: int, withdraw_value: float) -> Dict:
    self.__validate_withdrawal_value(withdraw_value=withdraw_value)
    self.__validate_balance_after_withdrawal(id=id, withdraw_value=withdraw_value)
    self.__make_withdrawal_in_db(id=id, withdraw_value=withdraw_value)
    formatted_response = self.__format_response(id=id, withdraw_value=withdraw_value)

    return formatted_response

  def __validate_withdrawal_value(self, withdraw_value: float) -> None:
    if not isinstance(withdraw_value, (int, float)):
      raise HttpBadRequestError('Valor de saque deve ser um número.')

    if withdraw_value <= 0:
      raise HttpBadRequestError('Valor do saque deve ser um número maior do que zero.')

    if withdraw_value > 200000:
      raise HttpBadRequestError('Limite máximo de saque permitido para pessoa jurídica de $200.000')
    
  def __validate_balance_after_withdrawal(self, id: int, withdraw_value: float) -> None:
    current_balance = self.__pessoa_juridica_repository.get_balance(id=id)

    if current_balance - withdraw_value < 0:
      raise Exception(f'Saldo em conta insuficiente para realizar saque desejado. Saldo atual: {current_balance}')
    
  def __make_withdrawal_in_db(self, id: int, withdraw_value: float) -> None:
    self.__pessoa_juridica_repository.withdraw(id=id, withdraw_value=withdraw_value)

  def __format_response(self, id: int, withdraw_value: float) -> Dict:
    return {
      'data': {
        'type': 'Pessoa Jurídica',
        'count': 1,
        'attributes': {
          'status': 'success',
          'id': id,
          'withdraw_value': withdraw_value
        }
      }
    }
  