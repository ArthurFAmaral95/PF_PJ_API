from src.controllers.interfaces.balance_getter_controller_interface import BalanceGetterControllerInterface
from src.views.interfaces.view_interface import ViewInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class BalanceGetterView(ViewInterface):
  def __init__(self, controller: BalanceGetterControllerInterface):
    self.__controller = controller

  def handle(self, http_request: HttpRequest) -> HttpResponse:
    client_id = http_request.param['client_id']
    body_response = self.__controller.get_client_balance(id=client_id)

    return HttpResponse(status_code=200, body=body_response)
  