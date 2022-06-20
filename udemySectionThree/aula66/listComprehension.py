# é usado para otimizar o code
# escrever menos linhas de code

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

ex1 = [v * 7 for v in l1]
ex2 = [(v, v2) for v in l1 for v2 in range(3)]

l2 = ['Luiz', 'Micael', 'Maria']
ex3 = [v.replace('i', '1') for v in l2]

t1 = (('chave1', 'valor1'), ('chave2', 'valor2'))
ex5 = [(y, x) for x, y in t1]
ex5 = dict(ex5)

l3 = list(range(100))
ex6 = [v for v in l3 if v % 3 == 0 if v % 5 == 0]

ex7 = [v if v % 3 == 0 and v % 8 == 0 else 0 for v in l3]

print(ex7)
