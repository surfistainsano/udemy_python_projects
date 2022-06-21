from itertools import zip_longest, count

# Some code

cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo', 'Blumenau']

# More some code

estados = ['SP', 'MG', 'BA']

# cidadesEstados = zip(estados, cidades)  # cria um ITERADOR (é um zip, porém se pode usar o método next())

indice = count()  # método que conta infinitamente (parâmetro vazio)

# a função zip() somente une arrays com base na MENOR

# cidadesEstados = zip_longest(indice, estados, cidades, fillvalue='Estado')  # LOOP INFINITO!

cidadesEstados = zip(indice, estados, cidades)

for i, s, c in cidadesEstados:
    print(i * i, s.lower(), c.upper())
