from typing import Dict
from src.views.lister_all_view import ListerAllView
from src.views.http_types.http_request import HttpRequest

class MockListerAllController:
  def list_all(self) -> Dict:
    return {
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

def test_handle():
  http_request = HttpRequest()
  view = ListerAllView(MockListerAllController())
  response = view.handle(http_request=http_request)

  assert response.status_code == 200
  assert response.body == {
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