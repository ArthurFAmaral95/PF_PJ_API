from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pessoa_fisica_repository import PessoaFisicaRepository
from src.controllers.pessoa_fisica_withdraw_controller import PessoaFisicaWithdrawController
from src.views.withdraw_view import WithdrawView

def pessoa_fisica_withdraw_composer():
  model = PessoaFisicaRepository(db_connection=db_connection_handler)
  controller = PessoaFisicaWithdrawController(model)
  view = WithdrawView(controller)

  return view
