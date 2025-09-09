import pytest
from src.models.sqlite.entities.pessoa_fisica import PessoaFisicaTable
from src.controllers.pessoa_fisica_depositer_controller import PessoaFisicaDepositerController

class MockPessoaFisicaRepository:
  def deposit(self, id: int, deposit_value: float):
    pass

  def list_specific_client(self, id: int):
    return PessoaFisicaTable(renda_mensal=100, idade=20, nome_completo='José da Silva', celular='4444-9999', email='zezinho@email.com', categoria='Categoria S', saldo=50)

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

def test_make_deposit_not_number_error():
  controller = PessoaFisicaDepositerController(MockPessoaFisicaRepository())

  with pytest.raises(Exception):
    controller.make_deposit(id=1, deposit_value='abc')
    
def test_make_deposit_negative_value_error():
  controller = PessoaFisicaDepositerController(MockPessoaFisicaRepository())

  with pytest.raises(Exception):
    controller.make_deposit(id=1, deposit_value=-100)
