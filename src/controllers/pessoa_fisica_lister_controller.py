from typing import Dict, List
from src.models.sqlite.interfaces.client_interface import ClientInterface
from src.controllers.interfaces.lister_controller_interface import ListerControllerInterface

class PessoaFisicaListerController(ListerControllerInterface):
  def __init__(self, pessoa_fisica_repository: ClientInterface):
    self.__pessoa_fisica_repository = pessoa_fisica_repository

  def list_client(self, id: int) -> Dict:
    client = self.__get_client_in_db(id=id)
    response = self.__format_response(client=client)
    return response

  def __get_client_in_db(self, id: int) -> List:
    client = self.__pessoa_fisica_repository.list_specific_client(id=id)
    if not client:
      raise Exception('Cliente não encontrado')
    
    return client
  
  def __format_response(self, client: List) -> Dict:
    return {
      'data': {
        'type': 'Pessoa Física',
        'count': 1,
        'attributes': {
          'id': client.id,
          'nome_completo': client.nome_completo,
          'idade': client.idade,
          'e-mail': client.email,
          'celular': client.celular,
          'categoria': client.categoria
        }
      }
    }