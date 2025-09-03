from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pessoa_fisica_repository import PessoaFisicaRepository
from src.controllers.pessoa_fisica_creator_controller import PessoaFisicaCreatorController
from src.views.creator_view import CreatorView

def pessoa_fisica_creator_composer():
  model = PessoaFisicaRepository(db_connection=db_connection_handler)
  controller = PessoaFisicaCreatorController(model)
  view = CreatorView(controller)

  return view
