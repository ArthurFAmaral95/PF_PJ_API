import pytest
from src.controllers.pessoa_juridica_creator_controller import PessoaJuridicaCreatorController

class MockPessoaJuridicaRepository:
  def insert_client(self, faturamento, idade, nome_fantasia, celular, email_corporativo, categoria, saldo):
    pass

def test_create():
  client_info = {
    'faturamento': 123456789,
    'idade': 30,
    'nome_fantasia': 'Empresa Teste',
    'celular': '1234-5678',
    'email_corporativo': 'email@exemplo.com',
    'categoria': 'Categoria teste',
    'saldo': 987654321
  }

  controller = PessoaJuridicaCreatorController(MockPessoaJuridicaRepository())

  response = controller.create(client_info=client_info)
  expected_response = {
    'data': {
      'type': 'Pessoa Jurídica', 
      'count': 1, 
      'attributes': {
        'faturamento': 123456789, 
        'idade': 30, 
        'nome_fantasia': 
        'Empresa Teste', 
        'celular': '1234-5678', 
        'email_corporativo': 'email@exemplo.com', 
        'categoria': 'Categoria teste', 
        'saldo': 987654321
      }
    }
  }
  
  assert response == expected_response

def test_create_faturamento_error():
  client_info = {
    'faturamento': 'abc',
    'idade': 30,
    'nome_fantasia': 'Empresa Teste',
    'celular': '1234-5678',
    'email_corporativo': 'email@exemplo.com',
    'categoria': 'Categoria teste',
    'saldo': 987654321
  }

  controller = PessoaJuridicaCreatorController(MockPessoaJuridicaRepository())
  with pytest.raises(Exception):
    controller.create(client_info=client_info)

def test_create_idade_error():
  client_info = {
    'faturamento': 123456789,
    'idade': 'abc',
    'nome_fantasia': 'Empresa Teste',
    'celular': '1234-5678',
    'email_corporativo': 'email@exemplo.com',
    'categoria': 'Categoria teste',
    'saldo': 987654321
  }

  controller = PessoaJuridicaCreatorController(MockPessoaJuridicaRepository())
  with pytest.raises(Exception):
    controller.create(client_info=client_info)

def test_create_nome_fantasia_error():
  client_info = {
    'faturamento': 123456789,
    'idade': 30,
    'nome_fantasia': 123,
    'celular': '1234-5678',
    'email_corporativo': 'email@exemplo.com',
    'categoria': 'Categoria teste',
    'saldo': 987654321
  }

  controller = PessoaJuridicaCreatorController(MockPessoaJuridicaRepository())

  with pytest.raises(Exception):
    controller.create(client_info=client_info)

def test_create_celular_error():
  client_info = {
    'faturamento': 123456789,
    'idade': 30,
    'nome_fantasia': 'Empresa Teste',
    'celular': 'abc',
    'email_corporativo': 'email@exemplo.com',
    'categoria': 'Categoria teste',
    'saldo': 987654321
  }

  controller = PessoaJuridicaCreatorController(MockPessoaJuridicaRepository())
  with pytest.raises(Exception):
    controller.create(client_info=client_info)

def test_create_email_corporativo_error():
  client_info = {
    'faturamento': 123456789,
    'idade': 30,
    'nome_fantasia': 'Empresa Teste',
    'celular': '1234-5678',
    'email_corporativo': 'email',
    'categoria': 'Categoria teste',
    'saldo': 987654321
  }

  controller = PessoaJuridicaCreatorController(MockPessoaJuridicaRepository()) 

  with pytest.raises(Exception):
    controller.create(client_info=client_info)

def test_create_categoria_error():
  client_info = {
    'faturamento': 123456789,
    'idade': 30,
    'nome_fantasia': 'Empresa Teste',
    'celular': '1234-5678',
    'email_corporativo': 'email@exemplo.com',
    'categoria': 'Categoria 123',
    'saldo': 987654321
  }

  controller = PessoaJuridicaCreatorController(MockPessoaJuridicaRepository())

  with pytest.raises(Exception):
    controller.create(client_info=client_info)

def test_create_saldo_error():
  client_info = {
    'faturamento': 123456789,
    'idade': 30,
    'nome_fantasia': 'Empresa Teste',
    'celular': '1234-5678',
    'email_corporativo': 'email@exemplo.com',
    'categoria': 'Categoria teste',
    'saldo': 'abc'
  }

  controller = PessoaJuridicaCreatorController(MockPessoaJuridicaRepository())

  with pytest.raises(Exception):
    controller.create(client_info=client_info)
  