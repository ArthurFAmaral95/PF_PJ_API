from typing import List
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.pessoa_juridica import PessoaJuridicaTable
from src.models.sqlite.interfaces.client_interface import ClientInterface

class PessoaJuridicaRepository(ClientInterface):
  def __init__(self, db_connection) -> None:
    self.__db_connection = db_connection
  
  def list_all_clients(self) -> List:
    with self.__db_connection as database:
      try:
        clients = (
          database.session
          .query(PessoaJuridicaTable)
          .all()
        )
        return clients
      except NoResultFound:
        return []

  def list_specific_client(self, id: int) -> List:
    with self.__db_connection as database:
      try:
        client = (
          database.session
          .query(PessoaJuridicaTable)
          .filter(PessoaJuridicaTable.id == id)
          .first()
        )
        return client
      except NoResultFound:
        return []

  def insert_client(self, faturamento: int, idade: int, nome_fantasia: str, celular: str, email_corporativo: str, categoria: str, saldo: int = 0) -> None:
    with self.__db_connection as database:
      try:
        new_client_data = PessoaJuridicaTable(
          faturamento = faturamento,
          idade = idade,
          nome_fantasia = nome_fantasia,
          celular = celular,
          email_corporativo = email_corporativo,
          categoria = categoria,
          saldo = saldo
        )
        database.session.add(new_client_data)
        database.session.commit()
      except Exception as exception:
        database.session.rollback()
        raise exception

  def get_balance(self, id: int) -> None:
    try:
      balance = self.list_specific_client(id).saldo
      return balance
    except Exception:
      return None

  def deposit(self, id: int, deposit_value: int) -> None:
    with self.__db_connection as database:
      try:
        client = (
          database.session
          .query(PessoaJuridicaTable)
          .filter(PessoaJuridicaTable.id == id)
          .first()
        )
        client.saldo += deposit_value
        database.session.commit()
      except Exception as exception:
        database.session.rollback()
        raise exception

  def withdraw(self, id: int, withdraw_value: int) -> None:
    pass
