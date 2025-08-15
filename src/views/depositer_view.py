from src.controllers.interfaces.depositer_controller_interface import DepositerControllerInterface
from src.views.interfaces.view_interface import ViewInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class DepositerView(ViewInterface):
  def __init__(self, controller: DepositerControllerInterface):
    self.__controller = controller

  def handle(self, http_request: HttpRequest) -> HttpResponse:
    client_id = http_request.param['client_id']
    deposit_value = http_request.body['deposit_value']

    body_response = self.__controller.make_deposit(id=client_id, deposit_value=deposit_value)

    return HttpResponse(status_code=201, body=body_response)
    