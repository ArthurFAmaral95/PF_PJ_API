from unittest import mock
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
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

def test_list_all_clients():
  mock_connection = MockConnection()
  repo = PessoaFisicaRepository(mock_connection)
  response = repo.list_all_clients()
  first_client = response[0]


  assert first_client.id == 1
  assert first_client.nome_completo == 'Fulano de Tal'
  assert first_client.idade == 30
  assert first_client.email == 'fulanodetal@example.com'
  assert first_client.celular == '1234-5678'
  assert first_client.categoria == 'Categoria A'
  assert first_client.renda_mensal == 1000
  assert first_client.saldo == 100

def test_list_specific_client():
  mock_connection = MockConnection()
  repo = PessoaFisicaRepository(mock_connection)
  response = repo.list_specific_client(1)

  assert response.id == 1
  assert response.nome_completo == 'Fulano de Tal'
  assert response.idade == 30
  assert response.email == 'fulanodetal@example.com'
  assert response.celular == '1234-5678'
  assert response.categoria == 'Categoria A'
  assert response.renda_mensal == 1000
  assert response.saldo == 100