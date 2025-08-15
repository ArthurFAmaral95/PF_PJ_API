from typing import Dict
from src.views.balance_getter_view import BalanceGetterView
from src.views.http_types.http_request import HttpRequest

class MockBalanceGetterController:
  def get_client_balance(self, id: int) -> Dict:
    return {
    'data': {
      'type': 'Pessoa Jurídica', 
      'count': 1, 
      'attributes': {
        'id': 1, 
        'balance': 100
      }
    }
  }

def test_handle():
  http_resquest = HttpRequest(param={'client_id': 1})
  view = BalanceGetterView(MockBalanceGetterController())
  response = view.handle(http_request=http_resquest)

  assert response.status_code == 200
  assert response.body == {
    'data': {
      'type': 'Pessoa Jurídica', 
      'count': 1, 
      'attributes': {
        'id': 1, 
        'balance': 100
      }
    }
  }
