from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pessoa_fisica_repository import PessoaFisicaRepository
from src.controllers.pessoa_fisica_depositer_controller import PessoaFisicaDepositerController
from src.views.depositer_view import DepositerView

def pessoa_fisica_depositer_composer():
  model = PessoaFisicaRepository(db_connection=db_connection_handler)
  controller = PessoaFisicaDepositerController(model)
  view = DepositerView(controller)

  return view
