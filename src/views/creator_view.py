from src.controllers.interfaces.creator_controller_interface import CreatorControllerInterface
from src.views.interfaces.view_interface import ViewInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class CreatorView(ViewInterface):
  def __init__(self, controller: CreatorControllerInterface) -> None:
    self.__controller = controller

  def handle(self, http_request: HttpRequest) -> HttpResponse:
    client_info = http_request.body
    body_response = self.__controller.create(client_info=client_info)
    return HttpResponse(status_code=201, body=body_response)
    