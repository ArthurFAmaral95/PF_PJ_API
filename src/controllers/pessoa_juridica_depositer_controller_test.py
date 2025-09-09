import pytest
from src.models.sqlite.entities.pessoa_juridica import PessoaJuridicaTable
from src.controllers.pessoa_juridica_depositer_controller import PessoaJuridicaDepositerController

class MockPessoaJuridicaRepository:
  def deposit(self, id: int, deposit_value: float):
    pass

  def list_specific_client(self, id: int):
    return PessoaJuridicaTable(
        faturamento=100000,
        idade=10,
        nome_fantasia='Empresa Teste',
        celular='1234-5678',
        email_corporativo='teste@email.com',
        categoria='Categoria Teste',
        saldo=1000000
      )

def test_make_deposit():
  controller = PessoaJuridicaDepositerController(MockPessoaJuridicaRepository())

  response = controller.make_deposit(id=1, deposit_value=100)

  expected_response = {
    'data':{
      'type': 'Pessoa Jurídica', 
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
  controller = PessoaJuridicaDepositerController(MockPessoaJuridicaRepository())

  with pytest.raises(Exception):
    controller.make_deposit(id=1, deposit_value='abc')

def test_make_deposit_negative_value_error():
  controller = PessoaJuridicaDepositerController(MockPessoaJuridicaRepository())

  with pytest.raises(Exception):
    controller.make_deposit(id=1, deposit_value=-100)
