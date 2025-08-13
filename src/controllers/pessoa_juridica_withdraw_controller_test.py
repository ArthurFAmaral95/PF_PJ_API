import pytest
from src.controllers.pessoa_juridica_withdraw_controller import PessoaJuridicaWithdrawController

class MockPessoaJuridicaRepository:
  def withdraw(self, id: int, withdraw_value: float) -> None:
    pass

  def get_balance(self, id: int) -> float:
    return 100

def test_make_withdrawal():
  controller = PessoaJuridicaWithdrawController(MockPessoaJuridicaRepository())

  response = controller.make_withdrawal(id=1, withdraw_value=100)

  expected_response = {
    'data': {
      'type': 'Pessoa Jurídica', 
      'count': 1, 
      'attributes': {
        'status': 'success', 
        'id': 1, 
        'withdraw_value': 100
     }
    }
  }

  assert response == expected_response

def test_make_withdrawal_not_number_error():
  controller = PessoaJuridicaWithdrawController(MockPessoaJuridicaRepository())

  with pytest.raises(Exception):
    controller.make_withdrawal(id=1, withdraw_value='abc')

def test_make_withdrawal_negative_value_error():
  controller = PessoaJuridicaWithdrawController(MockPessoaJuridicaRepository())

  with pytest.raises(Exception):
    controller.make_withdrawal(id=1, withdraw_value=-100)

def test_make_withdrawal_over_the_limit_error():
  controller = PessoaJuridicaWithdrawController(MockPessoaJuridicaRepository())

  with pytest.raises(Exception):
    controller.make_withdrawal(id=1, withdraw_value=10000000)

def test_make_withdrawal_not_enough_balance():
  controller = PessoaJuridicaWithdrawController(MockPessoaJuridicaRepository())

  with pytest.raises(Exception):
    controller.make_withdrawal(id=1, withdraw_value=1000)
