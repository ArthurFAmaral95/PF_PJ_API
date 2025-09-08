from src.validators.pessoa_juridica_creator_validator import pessoa_juridica_creator_validator

class MockRequest:
  def __init__(self, body) -> None:
    self.body = body

def test_pessoa_juridica_creator_validator():
  request = MockRequest({
    'faturamento': 1000,
    'idade': 10,
    'nome_fantasia': 'Empresa teste unitario',
    'celular': '1234-5678',
    'email_corporativo': 'testeunitario@email.com',
    'categoria': 'Categoria Teste',
    'saldo': 10000
  })

  pessoa_juridica_creator_validator(request)
