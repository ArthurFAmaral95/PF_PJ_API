from typing import List
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.pessoa_fisica import PessoaFisicaTable

class PessoaFisicaRepository:
  def __init__(self, db_connection) -> None:
    self.__db_connection = db_connection

  def list_all_clients(self) -> List:
    with self.__db_connection as database:
      try:
        clients = database.session.query(PessoaFisicaTable).all()
        return clients
      except NoResultFound:
        return []

  def list_specific_client(self, id: int) -> List:
    with self.__db_connection as database:
      try:
        client = (
          database.session
          .query(PessoaFisicaTable)
          .filter(PessoaFisicaTable.id == id)
          .first()
          )
        return client
      except NoResultFound:
        return []
