import pytest
from src.controllers.pessoa_fisica_creator_controller import PessoaFisicaCreatorController

class MockPessoaFisicaRepository:
  def insert_client(self, renda_mensal, idade, nome_completo, celular, email, categoria, saldo):
    pass

def test_create():
  client_info = {
    'renda_mensal': 100,
    'idade': 30,
    'nome_completo': 'Nome Completo',
    'celular': '1234-5678',
    'email': 'email.@email.com',
    'categoria': 'Categoria A',
    'saldo': 100
  }

  controller = PessoaFisicaCreatorController(MockPessoaFisicaRepository())
  response = controller.create(client_info=client_info)

  expected_response = {
    'data': 
    {'type': 'Pessoa Física', 
     'count': 1, 
     'attributes': {
       'renda_mensal': 100, 
       'idade': 30, 
       'nome_completo': 'Nome Completo', 
       'celular': '1234-5678', 
       'email': 'email.@email.com', 
       'categoria': 'Categoria A', 
       'saldo': 100
       }
    }
  }
  assert response == expected_response

def test_create_renda_mensal_error():
  client_info = {
    'renda_mensal': 'abc',
    'idade': 30,
    'nome_completo': 'Nome Completo',
    'celular': '1234-5678',
    'email': 'email.@email.com',
    'categoria': 'Categoria A',
    'saldo': 100
  }

  controller = PessoaFisicaCreatorController(MockPessoaFisicaRepository())
  with pytest.raises(Exception):
    controller.create(client_info=client_info)

def test_create_idade_error():
  client_info = {
    'renda_mensal': 100,
    'idade': 'abc',
    'nome_completo': 'Nome Completo',
    'celular': '1234-5678',
    'email': 'email.@email.com',
    'categoria': 'Categoria A',
    'saldo': 100
  }

  controller = PessoaFisicaCreatorController(MockPessoaFisicaRepository())
  with pytest.raises(Exception):
    controller.create(client_info=client_info)

def test_create_nome_completo_error():
  client_info = {
    'renda_mensal': 100,
    'idade': 30,
    'nome_completo': 'Nome Completo1234',
    'celular': '1234-5678',
    'email': 'email.@email.com',
    'categoria': 'Categoria A',
    'saldo': 100
  }

  controller = PessoaFisicaCreatorController(MockPessoaFisicaRepository())
  with pytest.raises(Exception):
    controller.create(client_info=client_info)

def test_create_celular_error():
  client_info = {
    'renda_mensal': 100,
    'idade': 30,
    'nome_completo': 'Nome Completo',
    'celular': 'abc',
    'email': 'email.@email.com',
    'categoria': 'Categoria A',
    'saldo': 100
  }

  controller = PessoaFisicaCreatorController(MockPessoaFisicaRepository())
  with pytest.raises(Exception):
    controller.create(client_info=client_info)

def test_create_email_error():
  client_info = {
    'renda_mensal': 100,
    'idade': 30,
    'nome_completo': 'Nome Completo',
    'celular': '1234-5678',
    'email': 'email_sem_@',
    'categoria': 'Categoria A',
    'saldo': 100
  }

  controller = PessoaFisicaCreatorController(MockPessoaFisicaRepository())
  with pytest.raises(Exception):
    controller.create(client_info=client_info)

def test_create_categoria_error():
  client_info = {
    'renda_mensal': 100,
    'idade': 30,
    'nome_completo': 'Nome Completo',
    'celular': '1234-5678',
    'email': 'email.@email.com',
    'categoria': 'Categoria 1',
    'saldo': 100
  }

  controller = PessoaFisicaCreatorController(MockPessoaFisicaRepository())
  with pytest.raises(Exception):
    controller.create(client_info=client_info)

def test_create_saldo_error():
  client_info = {
    'renda_mensal': 100,
    'idade': 30,
    'nome_completo': 'Nome Completo',
    'celular': '1234-5678',
    'email': 'email.@email.com',
    'categoria': 'Categoria A',
    'saldo': 'abc'
  }

  controller = PessoaFisicaCreatorController(MockPessoaFisicaRepository())
  with pytest.raises(Exception):
    controller.create(client_info=client_info)