from typing import Union

# pesquisar no site do python sobre Typing

variavel: int = 10
variavel1: float = 2.2
variavel2: str = 'Arroz'
variavel3: list = ['Olá', 'Tudo', 'Bem', '?']


# o typehint é apenas para informar


def function(p1: int, p2: float, p3: dict) -> float:  # para informar o retorno | -> type
    return 1.7


function(1, 1.1, {})


def func() -> Union[str, bool]:  # para informar tipos múltiplos que podem ser retornados | from typing import Union
    return {'Olá': 'Mundo'}


print(func())

# Nota-se que a IDE "reclama" sobre os tipos dos dados
