"""Descrição rápida e simples.


What is Lorem Ipsum?

Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's
standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a
type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting,
remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem
Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem
Ipsum.


What is Lorem Ipsum?

Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's
standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a
type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting,
remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem
Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem
Ipsum.
"""""

var = 'Arroz'


def func(x, y):
    """Soma de x e y

    :param x: Primeiro número
    :type x: int or float
    :param y: Segundo número
    :type y: int, float or None
    :return: a soma entre x e y
    :rtype: int or float
    """

    return x + y


def multiplica(x, y, z=None):
    """
    função de multiplicação que utiliza três parâmetros

    Os dois primeiros prâmetros são obrigatórios. Logo, o último é opcional com o valor de None por padrão.

    # abaixo, cada TIPO DE DOCSTRINGS tem sua própria estrutura

    :param x: Primeiro número
    :type x: int or float
    :param y: Segundo número
    :type y: int or float
    :param z: Terceiro número
    :type z: int or float

    :return: A multiplicação entre x, y e z
    :rtype: int or float
    """
    if z:
        return x * y * z
    else:
        return x * y


var1 = 'A'
var2 = 'B'
var3 = 'C'
