from typing import Dict
import re
from src.models.sqlite.interfaces.client_interface import ClientInterface
from src.controllers.interfaces.creator_controller_interface import CreatorControllerInterface

class PessoaJuridicaCreatorController(CreatorControllerInterface):
  def __init__(self, pessoa_juridica_repository: ClientInterface):
    self.__pessoa_juridica_repository = pessoa_juridica_repository

  def create(self, client_info: Dict) -> Dict:
    faturamento = client_info['faturamento']
    idade = client_info['idade']
    nome_fantasia = client_info['nome_fantasia']
    celular = client_info['celular']
    email_corporativo = client_info['email_corporativo']
    categoria = client_info['categoria']
    saldo = client_info['saldo']

    self.__validate_faturamento(faturamento=faturamento)
    self.__validate_idade(idade=idade)
    self.__validate_nome_fantasia(nome_fantasia=nome_fantasia)
    self.__validate_celular(celular=celular)
    self.__validate_email_corporativo(email_corporativo=email_corporativo)
    self.__validate_categoria(categoria=categoria)
    self.__validate_saldo(saldo=saldo)

    self.__insert_client_in_db(faturamento=faturamento, idade=idade, nome_fantasia=nome_fantasia, celular=celular, email_corporativo=email_corporativo, categoria=categoria, saldo=saldo)

    formatted_response = self.__format_response(client_info=client_info)

    return formatted_response

  def __validate_faturamento(self, faturamento: float):
    if not isinstance(faturamento, (int, float)):
      raise ValueError('Faturamento deve ser um número.')

  def __validate_idade(self, idade: int):
    if not isinstance(idade, (int)):
      raise ValueError('Idade deve ser um número.')

  def __validate_nome_fantasia(self, nome_fantasia: str):
    if not isinstance(nome_fantasia, (str)):
      raise ValueError('Nome fantasia deve ser um texto.')

  def __validate_celular(self, celular: str):
    non_valid_characters = re.compile(r'[^0-9-]')
    if non_valid_characters.search(celular):
      raise ValueError('Celular deve conter apenas números e "-".')
  
  def __validate_email_corporativo(self, email_corporativo: str):
    regex_valid_email = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')
    if not re.fullmatch(regex_valid_email, email_corporativo):
      raise ValueError('E-mail inválido. Formato válido: exemplo@exemplo.com')
    
  def __validate_categoria(self, categoria: str):
    non_valid_characters = re.compile(r'[^a-zA-ZÀ-ÿ ]')
    if non_valid_characters.search(categoria):
      raise ValueError('Categoria deve conter apenas letras.')

  def __validate_saldo(self, saldo: float):
    if not isinstance(saldo, (int, float)):
      raise ValueError('Saldo deve ser um número.')
    
  def __insert_client_in_db(self, faturamento: float, idade: int, nome_fantasia: str, celular: str, email_corporativo: str, categoria: str, saldo: float):
    self.__pessoa_juridica_repository.insert_client(faturamento=faturamento, idade=idade, nome_fantasia=nome_fantasia, celular=celular, email_corporativo=email_corporativo, categoria=categoria, saldo=saldo)

  def __format_response(self, client_info: Dict) -> Dict:
    return {
      'data': {
        'type': 'Pessoa Jurídica',
        'count': 1,
        'attributes': client_info
      }
    }
  