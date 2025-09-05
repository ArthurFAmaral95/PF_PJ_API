from src.validators.pessoa_fisica_creator_validator import pessoa_fisica_creator_validator

class MockRequest:
  def __init__(self, body) -> None:
    self.body = body

def test_pessoa_fisica_creator_validator():
  request = MockRequest({
    'renda_mensal': 1000,
    'idade': 20,
    'nome_completo': 'Fulano de Tal',
    'celular': '1234-5678',
    'email': 'fulanodetal@email.com',
    'categoria': 'Categoria A',
    'saldo': 100
  })
  
  pessoa_fisica_creator_validator(request)