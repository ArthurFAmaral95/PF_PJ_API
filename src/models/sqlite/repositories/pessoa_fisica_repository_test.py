from unittest import mock
import pytest
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.pessoa_fisica import PessoaFisicaTable
from src.models.sqlite.repositories.pessoa_fisica_repository import PessoaFisicaRepository

class MockConnection:
  def __init__(self) -> None:
    self.session = UnifiedAlchemyMagicMock(
      data=[
        (
          [mock.call.query(PessoaFisicaTable)],
          [
            PessoaFisicaTable(
              id=1,
              renda_mensal=1000,
              idade=30,
              nome_completo='Fulano de Tal',
              celular='1234-5678',
              email='fulanodetal@example.com',
              categoria='Categoria A',
              saldo=100
            )
          ]
        )
      ]
    )

  def __enter__(self): return self
  def __exit__(self, exc_type, exc_val, exc_tb): pass

class MockConnectionNoResult:
  def __init__(self):
    self.session = UnifiedAlchemyMagicMock()
    self.session.query.side_effect = self.__raise_no_result_found

  def __raise_no_result_found(self, *args, **kwargs):
    raise NoResultFound('No result found')

  def __enter__(self): return self
  def __exit__(self, exc_type, exc_val, exc_tb): pass

class MockConnectionNoInsertion:
  def __init__(self):
    self.session = UnifiedAlchemyMagicMock()
    self.session.add.side_effect = self.__raise_no_insertion

  def __raise_no_insertion(self, *args, **kwargs):
    raise Exception('No insertion made')
  
  def __enter__(self): return self
  def __exit__(self, exc_type, exc_val, exc_tb): pass

def test_list_all_clients():
  mock_connection = MockConnection()
  repo = PessoaFisicaRepository(mock_connection)
  response = repo.list_all_clients()
  first_client = response[0]

  mock_connection.session.query.assert_called_once_with(PessoaFisicaTable)
  mock_connection.session.all.assert_called_once()
  mock_connection.session.filter.assert_not_called()

  assert first_client.id == 1
  assert first_client.nome_completo == 'Fulano de Tal'
  assert first_client.idade == 30
  assert first_client.email == 'fulanodetal@example.com'
  assert first_client.celular == '1234-5678'
  assert first_client.categoria == 'Categoria A'
  assert first_client.renda_mensal == 1000
  assert first_client.saldo == 100

def test_list_all_clients_no_result():
  mock_connection = MockConnectionNoResult()
  repo = PessoaFisicaRepository(mock_connection)
  response = repo.list_all_clients()

  mock_connection.session.query.assert_called_once_with(PessoaFisicaTable)
  mock_connection.session.all.assert_not_called()
  mock_connection.session.filter.assert_not_called()

  assert response == []

def test_list_specific_client():
  mock_connection = MockConnection()
  repo = PessoaFisicaRepository(mock_connection)
  response = repo.list_specific_client(1)

  mock_connection.session.query.assert_called_once_with(PessoaFisicaTable)
  mock_connection.session.all.assert_not_called()
  mock_connection.session.filter.assert_called_once_with(PessoaFisicaTable.id == 1)
  mock_connection.session.first.assert_called_once()

  assert response.id == 1
  assert response.nome_completo == 'Fulano de Tal'
  assert response.idade == 30
  assert response.email == 'fulanodetal@example.com'
  assert response.celular == '1234-5678'
  assert response.categoria == 'Categoria A'
  assert response.renda_mensal == 1000
  assert response.saldo == 100

def test_list_specific_client_no_result():
  mock_connection = MockConnectionNoResult()
  repo = PessoaFisicaRepository(mock_connection)
  response = repo.list_specific_client(1)

  mock_connection.session.query.assert_called_once_with(PessoaFisicaTable)
  mock_connection.session.filter.assert_not_called()
  mock_connection.session.all.assert_not_called()
  mock_connection.session.first.assert_not_called()

  assert response == []

def test_insert_client():
  renda_mensal = 1000
  idade = 30
  nome_completo = 'Ciclano de Tal'
  celular = '7536-9514'
  email = 'ciclanodetal@example.com'
  categoria = 'Categoria B'
  saldo = 456

  mock_connection = MockConnection()
  repo = PessoaFisicaRepository(mock_connection)

  repo.insert_client(renda_mensal=renda_mensal, idade=idade, nome_completo=nome_completo,celular=celular, email=email, categoria=categoria, saldo=saldo)

  mock_connection.session.add.assert_called_once()

def test_insert_client_error():
  renda_mensal = 1000
  idade = 30
  nome_completo = 'Ciclano de Tal'
  celular = '7536-9514'
  email = 'ciclanodetal@example.com'
  categoria = 'Categoria B'
  saldo = 456

  mock_connection = MockConnectionNoInsertion()
  repo = PessoaFisicaRepository(mock_connection)

  with pytest.raises(Exception):
    repo.insert_client(renda_mensal=renda_mensal, idade=idade, nome_completo=nome_completo,celular=celular, email=email, categoria=categoria, saldo=saldo)
  
  mock_connection.session.add.assert_called_once()
  mock_connection.session.rollback.assert_called_once()

def test_get_balance():
  mock_connection = MockConnection()
  repo = PessoaFisicaRepository(mock_connection)
  response = repo.get_balance(1)

  assert response == 100

def test_get_balance_no_result():
  mock_connection = MockConnectionNoResult()
  repo = PessoaFisicaRepository(mock_connection)
  response = repo.get_balance(1)

  assert response is None
  
def test_deposit():
  mock_connection = MockConnection()
  repo = PessoaFisicaRepository(mock_connection)
  repo.deposit(id=1, deposit_value=50)

  mock_connection.session.query.assert_called_once_with(PessoaFisicaTable)
  mock_connection.session.all.assert_not_called()
  mock_connection.session.filter.assert_called_once_with(PessoaFisicaTable.id == 1)
  mock_connection.session.first.assert_called_once()
  mock_connection.session.commit.assert_called_once()

def test_deposit_error():
  mock_connection = MockConnectionNoResult()
  repo = PessoaFisicaRepository(mock_connection)

  with pytest.raises(Exception):
    repo.deposit(id=1, deposit_value=50)

  mock_connection.session.rollback.assert_called_once()
