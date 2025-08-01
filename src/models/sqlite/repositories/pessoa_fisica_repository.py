from typing import List
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.pessoa_fisica import PessoaFisicaTable
from src.models.sqlite.interfaces.client_interface import ClientInterface

class PessoaFisicaRepository(ClientInterface):
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
      
  def insert_client(self, renda_mensal: int, idade: int, nome_completo: str, celular: str, email: str, categoria: str, saldo: int = 0) -> None:
    with self.__db_connection as database:
      try:
        new_client_data = PessoaFisicaTable(
          renda_mensal = renda_mensal,
          idade = idade,
          nome_completo = nome_completo,
          celular = celular,
          email = email,
          categoria = categoria,
          saldo = saldo
        )    
        database.session.add(new_client_data)
        database.session.commit()
      except Exception as execption:
        database.session.rollback()
        raise execption
      
  def get_balance(self, id: int) -> int:
    try:
      balance = self.list_specific_client(id=id).saldo
      return balance
    except Exception:
      return None

  def deposit(self, id: int, deposit_value: int) -> None:
    with self.__db_connection as database:
      try:
        client = (
          database.session
          .query(PessoaFisicaTable)
          .filter(PessoaFisicaTable.id == id)
          .first()
        )
        # if client is None:
        #   raise NoResultFound('Cliente não encontrado')
        client.saldo += deposit_value
        database.session.commit()
      except Exception as exception:
        database.session.rollback()
        raise exception


  def withdraw(self, id: int, withdraw_value: int) -> None:
    with self.__db_connection as database:
      try:
        client = (
          database.session
          .query(PessoaFisicaTable)
          .filter(PessoaFisicaTable.id == id)
          .first()
        )
        client.saldo -= withdraw_value
        database.session.commit()
      except Exception as exception:
        database.session.rollback()
        raise exception
