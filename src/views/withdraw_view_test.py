from typing import Dict
from src.views.withdraw_view import WithdrawView
from src.views.http_types.http_request import HttpRequest

class MockWithdrawController:
    def make_withdrawal(self, id: int, withdraw_value: float) -> Dict:
        return {
      'data': {
        'type': 'Pessoa Jurídica',
        'count': 1,
        'attributes': {
          'status': 'success',
          'id': id,
          'withdraw_value': withdraw_value
        }
      }
    }
  

def test_handle():
  http_request = HttpRequest(
      body={'withdraw_value': 100},
      param={'client_id': 1}
    )

  view = WithdrawView(MockWithdrawController())
  response = view.handle(http_request=http_request)

  assert response.status_code == 201
  assert response.body == {
      'data': {
        'type': 'Pessoa Jurídica',
        'count': 1,
        'attributes': {
          'status': 'success',
          'id': 1,
          'withdraw_value': 100
        }
      }
    }
  
