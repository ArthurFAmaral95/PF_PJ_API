import pytest
from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pessoa_fisica_repository import PessoaFisicaRepository

db_connection_handler.connect_to_db()

def test_list_all_pessoa_fisica_clients():
  repo = PessoaFisicaRepository(db_connection_handler)
  response = repo.list_all_clients()
  first_client = response[0]
  
  assert first_client.id == 1
  assert first_client.nome_completo == 'João da Silva'
  assert first_client.idade == 35
  assert first_client.email == 'joao@example.com'
  assert first_client.celular == '9999-8888'
  assert first_client.categoria == 'Categoria A'
  assert first_client.renda_mensal == 5000
  
def test_list_specific_pessoa_fisica_client():
  repo = PessoaFisicaRepository(db_connection_handler)
  response = repo.list_specific_client(1)

  assert response.id == 1
  assert response.nome_completo == 'João da Silva'
  assert response.idade == 35
  assert response.email == 'joao@example.com'
  assert response.celular == '9999-8888'
  assert response.categoria == 'Categoria A'
  assert response.renda_mensal == 5000

@pytest.mark.skip(reason='adição de cliente no banco')
def test_insert_client_pessoa_fisica():
  renda_mensal = 10000
  idade = 35
  nome_completo = 'Nome Completo'
  celular = '8765-4321'
  email = 'email@example.com'
  categoria = 'Categoria B'
  saldo = 6000

  repo = PessoaFisicaRepository(db_connection_handler)
  repo.insert_client(renda_mensal=renda_mensal, idade=idade, nome_completo=nome_completo, celular=celular, email=email, categoria=categoria, saldo=saldo)

def test_get_balance_pessoa_fisica():
  repo = PessoaFisicaRepository(db_connection_handler)
  response = repo.get_balance(1)

  assert response == 10000

def test_deposit_pessoa_fisica():
  repo = PessoaFisicaRepository(db_connection_handler)
  repo.deposit(id=5, deposit_value=500)

def test_withdraw_pessoas_fisica():
  repo = PessoaFisicaRepository(db_connection_handler)
  repo.withdraw(id=5, withdraw_value=500)
