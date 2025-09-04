from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pessoa_juridica_repository import PessoaJuridicaRepository
from src.controllers.pessoa_juridica_lister_controller import PessoaJuridicaListerController
from src.views.lister_view import ListerView

def pessoa_juridica_lister_composer():
  model = PessoaJuridicaRepository(db_connection=db_connection_handler)
  controller = PessoaJuridicaListerController(model)
  view = ListerView(controller)

  return view
