from sqlalchemy import Column, String, BIGINT
from src.models.sqlite.settings.base import Base

class PessoaJuridicaTable(Base):
  __tablename__ = 'pessoa_juridica'

  id = Column(BIGINT, primary_key=True)
  faturamento = Column(BIGINT, nullable=False)
  idade = Column(BIGINT, nullable=False)
  nome_fantasia = Column(String, nullable=False, unique=True)
  celular = Column(String, nullable=False, unique=True)
  email_corporativo = Column(String, nullable=False, unique=True)
  categoria = Column(String, nullable=False)
  saldo = Column(BIGINT, default=0)

  def __repr__(self):
    return f"Pessoa Juridica [id={self.id}, nome_fantasia={self.nome_fantasia}, idade={self.idade}, email_corporativo={self.email_corporativo}, celular={self.celular}, categoria={self.categoria}, faturamento={self.faturamento}, saldo={self.saldo}]"
    