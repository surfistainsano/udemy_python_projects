# anonymous = lambda x, y: f'{x} {y}'
#
# print(anonymous('Olá', 'Leonardo'))

lista = [['P1', 13], ['P2', 5], ['P3', 7], ['P4', 20], ['P5', 14]]
# lista.sort()  # como há array dentro de array, o python não "sabe" como ordenar

# lista.sort(key=lambda item: item[1], reverse=False)
# # desse modo, é possível mostrar ao python a partir de que array filha queremos ordenar
# print(lista)

# Other way:

print(sorted(lista, key=lambda i: i[1], reverse=True))
print(lista)

# sort altera a array original
# sorted não altera a array original
