from sqlalchemy import Column, String, BIGINT
from src.models.sqlite.settings.base import Base

class PessoaFisicaTable(Base):
  __tablename__ = 'pessoa_fisica'

  id = Column(BIGINT, primary_key=True)
  renda_mensal = Column(BIGINT, nullable=False)
  idade = Column(BIGINT, nullable=False)
  nome_completo = Column(String, nullable=False)
  celular = Column(String, nullable=False, unique=True)
  email = Column(String, nullable=False, unique=True)
  categoria = Column(String, nullable=False)
  saldo = Column(BIGINT, nullable=False)

  def __repr__(self):
    return f"Pessoa Fisica [id={self.id}, nome_completo={self.nome_completo}, idade={self.idade}, email={self.email}, celular={self.celular}, categoria={self.categoria}, renda_mensal={self.renda_mensal}, saldo={self.saldo}]"