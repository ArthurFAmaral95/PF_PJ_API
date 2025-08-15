from src.controllers.interfaces.withdraw_controller_interface import WithdrawControllerInterface
from src.views.interfaces.view_interface import ViewInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class WithdrawView(ViewInterface):
  def __init__(self, controller: WithdrawControllerInterface):
    self.__controller = controller

  def handle(self, http_request: HttpRequest) -> HttpResponse:
    client_id = http_request.param['client_id']
    withdraw_value = http_request.body['withdraw_value']

    body_response = self.__controller.make_withdrawal(id=client_id, withdraw_value=withdraw_value)

    return HttpResponse(status_code=201, body=body_response)
