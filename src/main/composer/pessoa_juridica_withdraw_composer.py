from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pessoa_juridica_repository import PessoaJuridicaRepository
from src.controllers.pessoa_juridica_withdraw_controller import PessoaJuridicaWithdrawController
from src.views.withdraw_view import WithdrawView

def pessoa_juridica_withdraw_composer():
  model = PessoaJuridicaRepository(db_connection=db_connection_handler)
  controller = PessoaJuridicaWithdrawController(model)
  view = WithdrawView(controller)

  return view
