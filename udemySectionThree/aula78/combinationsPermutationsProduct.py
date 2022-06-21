from itertools import combinations, permutations, product

lista = ['Leonardo', 'Nicole', 'Lidiane', 'Eduarda', 'Lilian', 'Mauro', 'Luana']

# for grupo in combinations(lista, 3):
#     print(grupo)
# nota-se que a ORDEM não importa

# for grupo in permutations(lista, 3):
#     print(grupo)
# # nota-se que a ORDEM importa

for grupo in product(lista, repeat=3):
    print(grupo)

# nota-se que o método considera valores únicos como diferentes
