import pytest
from src.controllers.pessoa_fisica_balance_getter_controller import PessoaFisicaBalanceGetterController

class MockPessoaFisicaReporitory:
  def get_balance(self, id: int) -> float:
    return 100
  
class MockPessoaFisicaRepositoryError:
  def get_balance(self, id: int):
    pass
  
def test_get_client_balance():
  controller = PessoaFisicaBalanceGetterController(MockPessoaFisicaReporitory())
  response = controller.get_client_balance(1)

  expected_response = {
    'data': {
      'type': 'Pessoa Física', 
      'count': 1, 
      'attributes': {
        'id': 1, 
        'balance': 100
      }
    }
  }

  assert response == expected_response
  
def test_get_client_balance_error():
  controller = PessoaFisicaBalanceGetterController(MockPessoaFisicaRepositoryError())
  
  with pytest.raises(Exception):
    controller.get_client_balance(123)
