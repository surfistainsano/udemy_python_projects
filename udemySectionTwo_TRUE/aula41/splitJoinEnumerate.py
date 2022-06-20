frase = 'O Brasil é o país do futebol, o Brasil é penta campeão.'

arrayFrase = frase.split(' ')
arrayFrase1 = frase.split(',')

# for item in arrayFrase:
#     print(f'A palavra {item} apareceu {arrayFrase.count(item)}x na frase.')

# palavra = ''
# contador = 0
#
# for item in arrayFrase:
#     qtdVezes = arrayFrase.count(item)
#
#     if qtdVezes > contador:
#         contador = qtdVezes
#         palavra = item
#
# print(f'A palavra que apareceu mais vezes é {palavra} ({contador}x)')

# for item in arrayFrase1:
#     print(item.strip())  # elimina espaços de ambas as extremidades da String

# string = 'O Brasil é penta'
# # string = string.title()
# lista = string.split(' ')
# string1 = '_'.join(lista)
# print(string1)

# lista = ['Leonardo', 'Laura', 'Maria']
#
# # for v1, v2 in enumerate(lista):
# #     print(v1, v2)
#
# n1, n2, n3 = lista  # desempacotamento de array
#
# print(n3)

array = [['Leonardo', 'Maria', 'Laura'], ['Nicole', 'Duda', 'Luana'], ['Jeferson', 'Alessandro', 'Jorge']]

enumerated = list(enumerate(array))
print(f'enumerated: {enumerated} nota-se que é uma tupla')
# print(enumerated[2][1][-1][-1].upper())

for v1 in enumerate(array, 100):  # o segundo parâmetro define o algarismo inicial da contagem
    valor1, valor2 = v1
    nome1, nome2, nome3 = valor2
    print(nome1, nome2, nome3)
