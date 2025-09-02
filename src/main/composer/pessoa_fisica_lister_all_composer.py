from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pessoa_fisica_repository import PessoaFisicaRepository
from src.controllers.pessoa_fisica_lister_all_controller import PessoaFisicaListerAllController
from src.views.lister_all_view import ListerAllView

def pessoa_fisica_lister_all_composer():
  model = PessoaFisicaRepository(db_connection=db_connection_handler)
  controller = PessoaFisicaListerAllController(model)
  view = ListerAllView(controller=controller)

  return view
