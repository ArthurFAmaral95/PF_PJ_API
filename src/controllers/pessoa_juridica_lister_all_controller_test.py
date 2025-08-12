from src.controllers.pessoa_juridica_lister_all_controller import PessoaJuridicaListerAllController
from src.models.sqlite.entities.pessoa_juridica import PessoaJuridicaTable

class MockPessoaJuridicaRepository:
  def list_all_clients(self):
    return [
      PessoaJuridicaTable(
        faturamento=100000,
        idade=10,
        nome_fantasia='Empresa Teste',
        celular='1234-5678',
        email_corporativo='teste@email.com',
        categoria='Categoria Teste',
        saldo=1000000
      ),
      PessoaJuridicaTable(
        faturamento=500000,
        idade=30,
        nome_fantasia='Empresa Teste2',
        celular='9876-5432',
        email_corporativo='mock2@email.com',
        categoria='Categoria Mock',
        saldo=100000
      )
    ]
  
class MockPessoaJuridicaRepositoryNoReturn:
  def list_all_clients(self):
    return []
  
def test_list_all():
  controller = PessoaJuridicaListerAllController(MockPessoaJuridicaRepository())

  response = controller.list_all()

  expected_response = {
    'data': {
      'type': 'Pessoa Jurídica', 
      'count': 2, 
      'attributes': [
        {
          'id': None, 
          'nome_fantasia': 'Empresa Teste', 
          'idade': 10, 
          'celular': '1234-5678', 
          'email_corporativo': 
          'teste@email.com', 
          'categoria': 'Categoria Teste'
        }, 
        {
          'id': None, 
          'nome_fantasia': 'Empresa Teste2', 
          'idade': 30, 
          'celular': '9876-5432', 
          'email_corporativo': 'mock2@email.com', 
          'categoria': 'Categoria Mock'
        }
      ]
    }
  }
  
  assert response == expected_response

def test_list_all_no_result():
  controller = PessoaJuridicaListerAllController(MockPessoaJuridicaRepositoryNoReturn())
  response = controller.list_all()

  expected_response = {
    'data': {
      'type': 'Pessoa Jurídica', 
      'count': 0, 
      'attributes': []
    }
  }

  assert response == expected_response
