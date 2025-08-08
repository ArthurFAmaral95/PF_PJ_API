import pytest
from src.controllers.pessoa_fisica_depositer_controller import PessoaFisicaDepositerController

class MockPessoaFisicaRepository:
  def deposit(self, id: int, deposit_value: float):
    pass

def test_make_deposit():
  controller = PessoaFisicaDepositerController(MockPessoaFisicaRepository())
  response = controller.make_deposit(id=1, deposit_value=100)

  expected_response = {
    'data':{
      'type': 'Pessoa Física', 
      'count': 1, 
      'attributes': {
        'status': 'success', 
        'id': 1, 
        'deposit_value': 100
      }
    }
  }

  assert response == expected_response

def test_make_deposit_error():
  controller = PessoaFisicaDepositerController(MockPessoaFisicaRepository())

  with pytest.raises(Exception):
    controller.make_deposit(id=1, deposit_value='abc')
    