from typing import Dict
from src.models.sqlite.interfaces.client_interface import ClientInterface

class PessoaJuridicaListerController:
  def __init__(self, pessoa_juridica_repository: ClientInterface):
    self.__pessoa_juridica_repository = pessoa_juridica_repository

  def list_client(self, id: int) -> Dict:
    client = self.__get_client_in_db(id=id)
    response = self.__format_response(client=client)
    return response

  def __get_client_in_db(self, id: int):
    client = self.__pessoa_juridica_repository.list_specific_client(id=id)
    if not client:
      raise Exception('Cliente não encontrado.')
    
    return client
  
  def __format_response(self, client) -> Dict:
    return {
      'data': {
        'type': 'Pessoa Jurídica',
        'count': 1,
        'attributes': {
          'id': client.id,
          'nome_fantasia': client.nome_fantasia,
          'idade': client.idade,
          'celular': client.celular,
          'email_corporativo': client.email_corporativo,
          'categoria': client.categoria
        }
      }
    }