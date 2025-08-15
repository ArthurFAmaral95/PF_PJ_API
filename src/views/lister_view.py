from src.controllers.interfaces.lister_controller_interface import ListerControllerInterface
from src.views.http_types.http_request import HttpRequest 
from src.views.http_types.http_response import HttpResponse
from src.views.interfaces.view_interface import ViewInterface

class ListerView(ViewInterface):
  def __init__(self, controller: ListerControllerInterface) -> None:
    self.__controller = controller

  def handle(self, http_request: HttpRequest) -> HttpResponse:
    client_id = http_request.param['client_id']
    body_response = self.__controller.list_client(client_id)
    return HttpResponse(status_code=200, body=body_response)
