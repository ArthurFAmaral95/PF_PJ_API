import pytest
from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pessoa_fisica_repository import PessoaFisicaRepository
from src.models.sqlite.repositories.pessoa_juridica_repository import PessoaJuridicaRepository

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
  deposit_value = 500
  repo = PessoaFisicaRepository(db_connection_handler)
  current_balance = repo.get_balance(5)
  repo.deposit(id=5, deposit_value=deposit_value)
  balance_after_deposit = repo.get_balance(5)

  assert balance_after_deposit == current_balance + deposit_value

def test_withdraw_pessoas_fisica():
  withdraw_value = 500
  repo = PessoaFisicaRepository(db_connection_handler)
  current_balance = repo.get_balance(5)
  repo.withdraw(id=5, withdraw_value=withdraw_value)
  balance_after_withdraw = repo.get_balance(5)

  assert balance_after_withdraw == current_balance - withdraw_value

def test_list_all_pessoa_juridica_clients():
  repo = PessoaJuridicaRepository(db_connection_handler)
  response = repo.list_all_clients()
  first_client = response[0]

  assert first_client.id == 1
  assert first_client.nome_fantasia == 'Empresa XYZ'
  assert first_client.idade == 10
  assert first_client.email_corporativo == 'contato@empresa.com'
  assert first_client.celular == '1111-2222'
  assert first_client.categoria == 'Categoria A'
  assert first_client.faturamento == 100000
  assert first_client.saldo == 70000

def test_list_specific_pessoa_juridica_client():
  repo = PessoaJuridicaRepository(db_connection_handler)
  response = repo.list_specific_client(id=1)

  assert response.id == 1
  assert response.nome_fantasia == 'Empresa XYZ'
  assert response.idade == 10
  assert response.email_corporativo == 'contato@empresa.com'
  assert response.celular == '1111-2222'
  assert response.categoria == 'Categoria A'
  assert response.faturamento == 100000
  assert response.saldo == 70000

@pytest.mark.skip(reason='adição de cliente no banco')
def test_insert_client_pessoa_juridica():
  faturamento = 500000
  idade = 20
  nome_fantasia = 'Empresa Top Top'
  celular = '9876-5432'
  email_corporativo = 'empresatoptop@email.com'
  categoria = 'Categoria Z'
  saldo = 10000

  repo = PessoaJuridicaRepository(db_connection_handler)
  repo.insert_client(faturamento=faturamento, idade=idade, nome_fantasia=nome_fantasia, celular=celular, email_corporativo=email_corporativo, categoria=categoria, saldo=saldo)

def test_get_balance_pessoa_juridica():
  repo = PessoaJuridicaRepository(db_connection_handler)
  response = repo.get_balance(1)

  assert response == 70000

def test_deposit_pessoa_juridica():
  deposit_value = 10000
  repo = PessoaJuridicaRepository(db_connection_handler)
  current_balance = repo.get_balance(4)
  repo.deposit(id=4, deposit_value=deposit_value)
  balance_after_deposit = repo.get_balance(4)
  
  assert balance_after_deposit == current_balance + deposit_value