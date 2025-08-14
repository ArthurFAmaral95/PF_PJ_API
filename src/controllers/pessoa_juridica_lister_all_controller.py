from typing import Dict, List
from src.models.sqlite.interfaces.client_interface import ClientInterface
from src.controllers.interfaces.lister_all_controller_interface import ListerAllControllerInterface

class PessoaJuridicaListerAllController(ListerAllControllerInterface):
  def __init__(self, pessoa_juridica_repository: ClientInterface) -> None:
    self.__pessoa_juridica_repository = pessoa_juridica_repository

  def list_all(self) -> Dict:
    clients = self.__get_clients_in_db()
    response = self.__format_response(clients=clients)
    return response

  def __get_clients_in_db(self) -> List:
    clients = self.__pessoa_juridica_repository.list_all_clients()
    return clients
  
  def __format_response(self, clients: List) -> Dict:
    formatted_clients = []

    for client in clients:
      formatted_clients.append({
        'id': client.id,
        'nome_fantasia': client.nome_fantasia,
        'idade': client.idade,
        'celular': client.celular,
        'email_corporativo': client.email_corporativo,
        'categoria': client.categoria
      })

    return {
      'data': {
        'type': 'Pessoa Jurídica',
        'count': len(formatted_clients),
        'attributes': formatted_clients
      }
    }