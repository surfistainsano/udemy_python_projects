# contadores infinitos

from types import GeneratorType
from itertools import count

# variavel = zip('Arroz', 'Feijão')
# print(list(variavel))  # saída: [('A', 'F'), ('r', 'e'), ('r', 'i'), ('o', 'j'), ('z', 'ã')]
# print(next(variavel))  # saída: ('A', 'F')
# nota-se que o tipo de dado sendo ITERADOR retorna UM VALOR DE CADA VEZ
# pode-se usar o next() nesse tipo de dado

# print(isinstance(variavel, GeneratorType))  # false, pois não é um gerador

# para transformar em generator:

genVar = ((x, y) for x, y in zip('Arroz', 'Feijão'))

# print(isinstance(genVar, GeneratorType))  # True, pois é um generator de fato

# A função count() retorna um ITERADOR | Itertools - count

# contador = count()  # é um contador infinito

# contar progressivamente:

# contador = count(start=5, step=0.05)  # count(start=  , step=  )
#
# for n in contador:
#     print(round(n, 2))
#
#     if n >= 10:
#         break

# contar regressivamente:

contador = count(start=-1, step=-1)  # count(start=  , step=  )

for n in contador:
    print(round(n, 2))

    if n >= 10 or n <= -10:
        break

# Abaixo, uma dica para indexar valores de uma array

contador2 = count()

lista = ['Leonardo', 'Lidiane', 'Nicole', 'Rodrigo', 'Eduarda']

numeredList = zip(contador2, lista)

print(list(numeredList))
