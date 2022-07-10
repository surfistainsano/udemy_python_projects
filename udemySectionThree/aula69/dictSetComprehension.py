l1 = [('Leonardo', 'Programador'), ('Lidiane', 'Tec. Enfermagem'), ('Nicole', 'Enfermeira')]

compDict = {f'chave{x}': x ** 2 for x in range(5)}
compDict1 = {f'{y}': x for x, y in l1}

print(compDict1)
