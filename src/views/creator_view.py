from src.controllers.interfaces.creator_controller_interface import CreatorControllerInterface
from src.views.interfaces.view_interface import ViewInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.pessoa_fisica_creator_controller import PessoaFisicaCreatorController
from src.controllers.pessoa_juridica_creator_controller import PessoaJuridicaCreatorController
from src.validators.pessoa_fisica_creator_validator import pessoa_fisica_creator_validator
from src.validators.pessoa_juridica_creator_validator import pessoa_juridica_creator_validator

class CreatorView(ViewInterface):
  def __init__(self, controller: CreatorControllerInterface) -> None:
    self.__controller = controller

  def handle(self, http_request: HttpRequest) -> HttpResponse:
    if isinstance(self.__controller, PessoaFisicaCreatorController):
      pessoa_fisica_creator_validator(http_request=http_request)

    if isinstance(self.__controller, PessoaJuridicaCreatorController):
      pessoa_juridica_creator_validator(http_request=http_request)

    client_info = http_request.body
    body_response = self.__controller.create(client_info=client_info)
    return HttpResponse(status_code=201, body=body_response)
    