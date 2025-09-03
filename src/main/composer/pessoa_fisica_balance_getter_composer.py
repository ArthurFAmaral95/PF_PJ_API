from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pessoa_fisica_repository import PessoaFisicaRepository
from src.controllers.pessoa_fisica_balance_getter_controller import PessoaFisicaBalanceGetterController
from src.views.balance_getter_view import BalanceGetterView

def pessoa_fisica_balance_getter_composer():
  model = PessoaFisicaRepository(db_connection=db_connection_handler)
  controller = PessoaFisicaBalanceGetterController(model)
  view = BalanceGetterView(controller)

  return view
