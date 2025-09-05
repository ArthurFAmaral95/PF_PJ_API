from pydantic import BaseModel, constr, ValidationError
from src.views.http_types.http_request import HttpRequest
from src.errors.errors_types.http_unprocessable_entity import HttpUnprocessableEntityError

def pessoa_fisica_creator_validator(http_request: HttpRequest) -> None:
  class BodyData(BaseModel):
    renda_mensal: float
    idade: int
    nome_completo: constr(min_length=1) # type: ignore
    celular: constr(min_length=1) # type: ignore
    email: constr(min_length=1) # type: ignore
    categoria: constr(min_length=1) # type: ignore
    saldo: float

  try:
    BodyData(**http_request.body)
  except ValidationError as e:
    raise HttpUnprocessableEntityError(e.errors()) from e
  