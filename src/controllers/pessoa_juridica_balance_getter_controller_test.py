import pytest
from src.controllers.pessoa_juridica_balance_getter_controller import PessoaJuridicaBalanceGetterController

class MockPessoaJuridicaRepository:
  def get_balance(self, id: int) -> float:
    return 100
  
class MockPessoaJuridicaRepositoryError:
  def get_balance(self, id: int) -> None:
    pass

def test_get_balance():
  controller = PessoaJuridicaBalanceGetterController(MockPessoaJuridicaRepository())

  response = controller.get_client_balance(id=1)

  expected_response = {
    'data': {
      'type': 'Pessoa Jurídica', 
      'count': 1, 
      'attributes': {
        'id': 1, 
        'balance': 100
      }
    }
  }

  assert response == expected_response

def test_get_balance_error():
  controller = PessoaJuridicaBalanceGetterController(MockPessoaJuridicaRepositoryError())

  with pytest.raises(Exception):
    controller.get_client_balance(id=123)
    