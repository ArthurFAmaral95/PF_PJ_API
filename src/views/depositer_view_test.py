from typing import Dict
from src.views.depositer_view import DepositerView
from src.views.http_types.http_request import HttpRequest

class MockDepositerController:
  def make_deposit(self, id: int, deposit_value: float) -> Dict:
    return {
      'data': {
        'type': 'Pessoa Jurídica',
        'count': 1,
        'attributes': {
          'status': 'success',
          'id': id,
          'deposit_value': deposit_value
        }
      }
    }
  
def test_handle():
  http_request = HttpRequest(
    body={'deposit_value': 100},
    param={'client_id': 1}
  )

  view = DepositerView(MockDepositerController())
  response = view.handle(http_request=http_request)

  assert response.status_code == 201
  assert response.body == {
      'data': {
        'type': 'Pessoa Jurídica',
        'count': 1,
        'attributes': {
          'status': 'success',
          'id': 1,
          'deposit_value': 100
        }
      }
    }
  