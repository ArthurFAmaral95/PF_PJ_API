from typing import Dict
from src.views.creator_view import CreatorView
from src.views.http_types.http_request import HttpRequest

class MockCreatorController:
  def create(self, client_info: Dict) -> Dict:
    return {
    'data': {
      'type': 'Pessoa Jurídica', 
      'count': 1, 
      'attributes': {
        'faturamento': 123456789, 
        'idade': 30, 
        'nome_fantasia': 
        'Empresa Teste', 
        'celular': '1234-5678', 
        'email_corporativo': 'email@exemplo.com', 
        'categoria': 'Categoria teste', 
        'saldo': 987654321
      }
    }
  }

def test_handle():
  http_request = HttpRequest(
    {
      'faturamento': 123456789,
      'idade': 30,
      'nome_fantasia': 'Empresa Teste',
      'celular': '1234-5678',
      'email_corporativo': 'email@exemplo.com',
      'categoria': 'Categoria teste',
      'saldo': 987654321
    }
  )
  view = CreatorView(MockCreatorController())
  response = view.handle(http_request=http_request)

  assert response.status_code == 201
  assert response.body == {
    'data': {
      'type': 'Pessoa Jurídica', 
      'count': 1, 
      'attributes': {
        'faturamento': 123456789, 
        'idade': 30, 
        'nome_fantasia': 
        'Empresa Teste', 
        'celular': '1234-5678', 
        'email_corporativo': 'email@exemplo.com', 
        'categoria': 'Categoria teste', 
        'saldo': 987654321
      }
    }
  }
