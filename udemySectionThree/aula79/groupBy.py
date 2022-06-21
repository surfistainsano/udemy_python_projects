from itertools import groupby, tee

alunos = [
    {'aluno': 'Leonardo', 'nota': 'A'},
    {'aluno': 'Laura', 'nota': 'B'},
    {'aluno': 'Lennon', 'nota': 'C'},
    {'aluno': 'Leona', 'nota': 'C'},
    {'aluno': 'Leticia', 'nota': 'B'},
    {'aluno': 'Lewandovisk', 'nota': 'A'},
    {'aluno': 'Luiza', 'nota': 'B'},
    {'aluno': 'Lucas', 'nota': 'C'},
    {'aluno': 'Lidiane', 'nota': 'A'},
    {'aluno': 'Lummertz', 'nota': 'B'},
    {'aluno': 'Koko', 'nota': 'D'},
    {'aluno': 'Banri', 'nota': 'D'},
]

# o método groupby() só funciona se os item estiverem já na ordem desejada

ordena = lambda item: item['nota']
alunos.sort(key=ordena)
alunosAgrupados = groupby(alunos, ordena)

# para ver o NOME e NOTA dos alunos:

# for v1, v2 in alunosAgrupados:
#     print(f'Agrupamento: {v1}')
#
#     for aluno in v2:
#         print(aluno)
#     print()

# para ver a QUANTIDADE de alunos que tiraram tal nota:

for v1, v2 in alunosAgrupados:
    va1, va2 = tee(v2)  # duas cópias do objeto groupby que contém os alunos e suas notas
    print(f'Agrupamento: {v1}')

    for aluno in va1:
        print(aluno)

    quantidade = len(list(va2))
    print(f'\t{quantidade} alunos tiraram a nota {v1}')
    print()
