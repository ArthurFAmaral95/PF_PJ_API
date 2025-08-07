from typing import Dict, List
from src.models.sqlite.interfaces.client_interface import ClientInterface

class PessoaFisicaListerAllController:
  def __init__(self, pessoa_fisica_repository: ClientInterface) -> None:
    self.__pessoa_fisica_repository = pessoa_fisica_repository
    
  def list_all(self) -> Dict:
    clients = self.__get_clients_in_db()
    response = self.__format_response(clients=clients)
    return response

  def __get_clients_in_db(self) -> List:
    clients = self.__pessoa_fisica_repository.list_all_clients()
    return clients
  
  def __format_response(self, clients: List) -> Dict:
    formatted_clients = []

    for client in clients:
      formatted_clients.append({'id': client.id, 'nome_completo': client.nome_completo, 'idade': client.idade, 'e-mail': client.email, 'celular': client.celular, 'categoria': client.categoria})

    return {
      'data': {
        'type': 'Pessoa Fisica',
        'count': len(formatted_clients),
        'attributes': formatted_clients
      }
    }
