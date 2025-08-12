import pytest 
from src.controllers.pessoa_juridica_lister_controller import PessoaJuridicaListerController
from src.models.sqlite.entities.pessoa_juridica import PessoaJuridicaTable

class MockPessoaJuridicaRepository:
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
  
class MockPessoaJuridicaRepositoryError:
  def list_specific_client(self, id: int):
    pass

def test_list_client():
  controller = PessoaJuridicaListerController(MockPessoaJuridicaRepository())
  response = controller.list_client(id=1)

  expected_response = {
    'data': {
      'type': 'Pessoa Jurídica', 
      'count': 1, 
      'attributes': {
        'id': None, 
        'nome_fantasia': 'Empresa Teste', 
        'idade': 10, 
        'celular': '1234-5678', 
        'email_corporativo': 'teste@email.com', 
        'categoria': 'Categoria Teste'
      }
    }
  }

  assert response == expected_response

def test_list_client_error():
  controller = PessoaJuridicaListerController(MockPessoaJuridicaRepositoryError())
  
  with pytest.raises(Exception):
    controller.list_client(id=1)
