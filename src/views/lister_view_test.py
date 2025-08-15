from typing import Dict
from src.views.lister_view import ListerView
from src.views.http_types.http_request import HttpRequest

class MockListerController:
  def list_client(self, id: int) -> Dict:
    return {
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

def test_handle():
  http_request = HttpRequest(param={'client_id': 1})
  view = ListerView(MockListerController())
  response = view.handle(http_request=http_request)

  assert response.status_code == 200
  assert response.body == {
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
  