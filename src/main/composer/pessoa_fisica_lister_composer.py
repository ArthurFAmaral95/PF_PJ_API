from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pessoa_fisica_repository import PessoaFisicaRepository
from src.controllers.pessoa_fisica_lister_controller import PessoaFisicaListerController
from src.views.lister_view import ListerView

def pessoa_fisica_lister_composer():
  model = PessoaFisicaRepository(db_connection=db_connection_handler)
  controller = PessoaFisicaListerController(model)
  view = ListerView(controller=controller)

  return view
  