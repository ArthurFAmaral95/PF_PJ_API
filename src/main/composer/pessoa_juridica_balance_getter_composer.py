from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pessoa_juridica_repository import PessoaJuridicaRepository
from src.controllers.pessoa_juridica_balance_getter_controller import PessoaJuridicaBalanceGetterController
from src.views.balance_getter_view import BalanceGetterView

def pessoa_juridica_balance_getter_composer():
  model = PessoaJuridicaRepository(db_connection=db_connection_handler)
  controller = PessoaJuridicaBalanceGetterController(model)
  view = BalanceGetterView(controller)

  return view
  