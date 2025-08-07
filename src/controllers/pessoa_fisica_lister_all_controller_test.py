from src.controllers.pessoa_fisica_lister_all_controller import PessoaFisicaListerAllController
from src.models.sqlite.entities.pessoa_fisica import PessoaFisicaTable

class MockPessoaFisicaRepository:
  def list_all_clients(self):
    return [
      PessoaFisicaTable(renda_mensal=100, idade=20, nome_completo='José da Silva', celular='4444-9999', email='zezinho@email.com', categoria='Categoria S', saldo=50),
      PessoaFisicaTable(renda_mensal=1000, idade=200, nome_completo='João Babão', celular='7777-7777', email='joaozao@email.com', categoria='Categoria S', saldo=5)
    ]
  
class MockPessoaFisicaRepositoryError:
  def list_all_clients(self):
    return []

def test_list_all():
  controller = PessoaFisicaListerAllController(MockPessoaFisicaRepository())
  response = controller.list_all()
  expected_response = {
    'data': {
      'type': 'Pessoa Fisica', 
      'count': 2, 
      'attributes': [
        {'id': None, 'nome_completo': 'José da Silva', 'idade': 20, 'e-mail': 'zezinho@email.com', 'celular': '4444-9999', 'categoria': 'Categoria S'}, 
        {'id': None, 'nome_completo': 'João Babão', 'idade': 200, 'e-mail': 'joaozao@email.com', 'celular': '7777-7777', 'categoria': 'Categoria S'}
        ]
    }
  }

  assert response == expected_response

def test_list_all_error():
  controller = PessoaFisicaListerAllController(MockPessoaFisicaRepositoryError())
  response = controller.list_all()

  expected_response = {
    'data': {
      'type': 'Pessoa Fisica', 
      'count': 0, 
      'attributes': []
    }
  }

  assert response == expected_response