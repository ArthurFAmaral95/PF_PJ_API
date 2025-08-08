from typing import Dict
import re
from src.models.sqlite.interfaces.client_interface import ClientInterface

class PessoaFisicaCreatorController:
  def __init__(self, pessoa_fisica_repository: ClientInterface):
    self.__pessoa_fisica_repository = pessoa_fisica_repository

  def create(self, client_info: Dict) -> Dict:
    renda_mensal = client_info['renda_mensal']
    idade = client_info['idade']
    nome_completo = client_info['nome_completo']
    celular = client_info['celular']
    email = client_info['email']
    categoria = client_info['categoria']
    saldo = client_info['saldo']

    self.__validade_renda_mensal(renda_mensal=renda_mensal)
    self.__validate_idade(idade=idade)
    self.__validate_nome_completo(nome_completo=nome_completo)
    self.__validate_celular(celular=celular)
    self.__validate_email(email=email)
    self.__validate_categoria(categoria=categoria)
    self.__validate_saldo(saldo=saldo)

    self.__insert_client_in_db(renda_mensal=renda_mensal, idade=idade, nome_completo=nome_completo, celular=celular, email=email, categoria=categoria, saldo=saldo)
    formatted_response = self.__format_response(client_info=client_info)
    return formatted_response

  def __validade_renda_mensal(self, renda_mensal: float) -> None:
    if not isinstance(renda_mensal, (int, float)):
      raise ValueError('Renda mensal deve ser um número.')
    
  def __validate_idade(self, idade: int) -> None:
    if not isinstance(idade, (int, float)):
      raise ValueError('Idade deve ser um número.')
    
  def __validate_saldo(self, saldo: float) -> None:
    if not isinstance(saldo, (int, float)):
      raise ValueError('Saldo deve ser um número.')

  def __validate_nome_completo(self, nome_completo: str) -> None:
    non_valid_characters = re.compile(r'[^a-zA-ZÀ-ÿ ]')
    if non_valid_characters.search(nome_completo):
      raise ValueError('Nome deve conter apenas letras.')
    
  def __validate_categoria(self, categoria: str) -> None:
    non_valid_characters = re.compile(r'[^a-zA-ZÀ-ÿ ]')
    if non_valid_characters.search(categoria):
      raise ValueError('Categoria deve conter apenas letras.')
  
  def __validate_celular(self, celular: str) -> None:
    non_valid_characters = re.compile(r'[^0-9-]')
    if non_valid_characters.search(celular):
      raise ValueError('Celular deve conter apenas números e "-".')
    
  def __validate_email(self, email: str) -> None:
    regex_valid_email = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')
    if not re.fullmatch(regex_valid_email, email):
      raise ValueError('E-mail inválido. Formato válido: exemplo@exemplo.com')

  def __insert_client_in_db(self, renda_mensal: float, idade: int, nome_completo: str, celular: str, email: str, categoria: str, saldo: float) -> None:
    self.__pessoa_fisica_repository.insert_client(renda_mensal=renda_mensal, idade=idade, nome_completo=nome_completo, celular=celular, email=email, categoria=categoria, saldo=saldo)

  def __format_response(self, client_info: Dict) -> Dict:
    return {
      'data': {
        'type': 'Pessoa Física',
        'count': 1,
        'attributes': client_info
      }
    }