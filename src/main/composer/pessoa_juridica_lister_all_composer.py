from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pessoa_juridica_repository import PessoaJuridicaRepository
from src.controllers.pessoa_juridica_lister_all_controller import PessoaJuridicaListerAllController
from src.views.lister_all_view import ListerAllView

def pessoa_juridica_lister_all_composer():
  model = PessoaJuridicaRepository(db_connection=db_connection_handler)
  controller = PessoaJuridicaListerAllController(model)
  view = ListerAllView(controller=controller)

  return view
