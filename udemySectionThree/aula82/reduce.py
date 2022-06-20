from dados import produtos, pessoas, lista
from functools import reduce

# acumulador simples
# acumulador = 0
# for i in lista:
#     acumulador += i
#
# print(acumulador)

# somaLista = reduce(lambda ac, n: n + ac, lista, 0)  # reduce(function(acumulador, parameter), iterable, startValue)
# print(somaLista)

somaLista = round(reduce(lambda ac, n: n['preco'] + ac, produtos, 0), 2)
print(f'Total = {somaLista}. Logo, a média é {round(somaLista / len(produtos), 2)}')

# média de idades do dict pessoas:

somaIdades = reduce(lambda ac, idade: idade['idade'] + ac, pessoas, 0)
mediaIdade = round(somaIdades / len(pessoas), 2)

print(f'A média de idade das pessoas é {mediaIdade}')
