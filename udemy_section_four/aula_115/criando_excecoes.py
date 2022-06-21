# por convenção, toda exceção termina com Error.

class TaErradoError(Exception):
    pass


def test():
    raise TaErradoError("Tá errado.")


try:
    test()
except TaErradoError as erro:
    print(f'Erro: {erro}.')

# é recomendado ler a documentação do python, para utilizar as exceções da linguagem. Caso não se encontre uma
# apropriada, pode-se criar exceções personalizadas.
