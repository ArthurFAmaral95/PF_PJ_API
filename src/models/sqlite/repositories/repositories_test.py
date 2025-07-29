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

  