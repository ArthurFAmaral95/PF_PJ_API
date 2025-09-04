from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pessoa_juridica_repository import PessoaJuridicaRepository
from src.controllers.pessoa_juridica_depositer_controller import PessoaJuridicaDepositerController
from src.views.depositer_view import DepositerView

def pessoa_juridica_depositer_composer():
  model = PessoaJuridicaRepository(db_connection=db_connection_handler)
  controller = PessoaJuridicaDepositerController(model)
  view = DepositerView(controller)

  return view
  