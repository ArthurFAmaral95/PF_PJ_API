import pytest
from src.controllers.pessoa_fisica_lister_controller import PessoaFisicaListerController
from src.models.sqlite.entities.pessoa_fisica import PessoaFisicaTable

class MockPessoaFisicaRepository:
  def list_specific_client(self, id: int):
    return PessoaFisicaTable(renda_mensal=100, idade=20, nome_completo='José da Silva', celular='4444-9999', email='zezinho@email.com', categoria='Categoria S', saldo=50)
  
class MockPessoaFisicaRepositoryError:
  def ist_specific_client(self, id: int):
    pass
    
def test_list_client():
  controller = PessoaFisicaListerController(MockPessoaFisicaRepository())
  response = controller.list_client(id=1)

  expected_response = {
    'data': {
      'type': 'Pessoa Física',
      'count': 1, 
      'attributes': {
        'id': None, 
        'nome_completo': 'José da Silva',
        'idade': 20, 
        'e-mail': 'zezinho@email.com', 
        'celular': '4444-9999', 
        'categoria': 'Categoria S'
      }
    }
  }

  assert response == expected_response

def test_list_client_error():
  controller = PessoaFisicaListerController(MockPessoaFisicaRepositoryError())

  with pytest.raises(Exception):
    controller.list_client(id=1)
