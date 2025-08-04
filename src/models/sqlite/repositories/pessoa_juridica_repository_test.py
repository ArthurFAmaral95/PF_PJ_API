from unittest import mock
import pytest
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.pessoa_juridica import PessoaJuridicaTable
from src.models.sqlite.repositories.pessoa_juridica_repository import PessoaJuridicaRepository

class MockConnection:
  def __init__(self) -> None:
    self.session = UnifiedAlchemyMagicMock(
      data = [
        (
          [mock.call.query(PessoaJuridicaTable)],
          [
            PessoaJuridicaTable(
              id = 1,
              faturamento = 5000000,
              idade = 2,
              nome_fantasia = 'Empresa Top',
              celular = '1234-5678',
              email_corporativo = 'empresatop@email.com',
              categoria = 'Categoria Z',
              saldo = 600000
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
    self.session.query.side_effect = self._raise_no_result_found

  def _raise_no_result_found(self, *args, **kwargs):
    raise NoResultFound('No result found')
  
  def __enter__(self): return self
  def __exit__(self, exc_type, exc_val, exc_tb): pass

def test_list_all_clients():
  mock_connection = MockConnection()
  repo = PessoaJuridicaRepository(mock_connection)
  response = repo.list_all_clients()
  first_client = response[0]
  
  mock_connection.session.query.assert_called_once_with(PessoaJuridicaTable)
  mock_connection.session.all.assert_called_once()
  mock_connection.session.fitler.assert_not_called()

  assert first_client.id == 1
  assert first_client.faturamento == 5000000
  assert first_client.idade == 2
  assert first_client.nome_fantasia == 'Empresa Top'
  assert first_client.celular == '1234-5678'
  assert first_client.email_corporativo == 'empresatop@email.com'
  assert first_client.categoria == 'Categoria Z'
  assert first_client.saldo == 600000

def test_list_all_clients_no_result():
  mock_connection = MockConnectionNoResult()
  repo = PessoaJuridicaRepository(mock_connection)
  response = repo.list_all_clients()

  mock_connection.session.query.assert_called_once_with(PessoaJuridicaTable)
  mock_connection.session.all.assert_not_called()
  mock_connection.session.filter.assert_not_called()

  assert response == []

def test_list_specific_client():
  mock_connection = MockConnection()
  repo = PessoaJuridicaRepository(mock_connection)
  response = repo.list_specific_client(1)

  mock_connection.session.query.assert_called_once_with(PessoaJuridicaTable)
  mock_connection.session.filter.assert_called_once_with(PessoaJuridicaTable.id == 1)
  mock_connection.session.all.assert_not_called()
  mock_connection.session.first.assert_called_once()
  
  assert response.id == 1
  assert response.faturamento == 5000000
  assert response.idade == 2
  assert response.nome_fantasia == 'Empresa Top'
  assert response.celular == '1234-5678'
  assert response.email_corporativo == 'empresatop@email.com'
  assert response.categoria == 'Categoria Z'
  assert response.saldo == 600000

def test_list_specific_client_no_result():
  mock_connection = MockConnectionNoResult()
  repo = PessoaJuridicaRepository(mock_connection)
  response = repo.list_specific_client(1)

  mock_connection.session.query.assert_called_once_with(PessoaJuridicaTable)
  mock_connection.session.filter.assert_not_called()
  mock_connection.session.first.assert_not_called()

  assert response == []
