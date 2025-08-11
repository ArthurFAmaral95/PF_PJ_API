import pytest
from src.controllers.pessoa_fisica_withdraw_controller import PessoaFisicaWithdrawController

class MockPessoaFisicaRepository():
  def withdraw(self, id: int, withdraw_value: float):
    pass

def test_make_withdrawal():
  controller = PessoaFisicaWithdrawController(MockPessoaFisicaRepository())

  response = controller.make_withdrawal(id=1, withdraw_value=100)

  expected_response = {
    'data': {
      'type': 'Pessoa Física', 
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
  controller = PessoaFisicaWithdrawController(MockPessoaFisicaRepository())

  with pytest.raises(Exception):
    controller.make_withdrawal(id=1, withdraw_value='abc')

def test_make_withdrawal_negative_value_error():
  controller = PessoaFisicaWithdrawController(MockPessoaFisicaRepository())

  with pytest.raises(Exception):
    controller.make_withdrawal(id=1, withdraw_value=-100)

def test_make_withdrawal_over_limit_error():
  controller = PessoaFisicaWithdrawController(MockPessoaFisicaRepository())
  
  with pytest.raises(Exception):
    controller.make_withdrawal(id=1, withdraw_value=100000)
