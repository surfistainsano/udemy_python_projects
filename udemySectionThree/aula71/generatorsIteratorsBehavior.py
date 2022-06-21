
nome = 'Leonardo Lüders'

gerador = (letra for letra in nome)

print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))

print()
print('O for consumirá o resto')

for letra in gerador:
    print(letra)

# ao usar dois for, o segundo não retornará valor, pois o primeiro já terá o "consumido" o iterador
# geradores e iteradores são feitos para consumirem seus valores, ou seja, depois de iterados por completo, esvaziam-se.
