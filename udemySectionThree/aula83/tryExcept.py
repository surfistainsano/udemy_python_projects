try:
    a = []
    ar = 1 / 0
    # print(ar[1])
except NameError as erro:
    print('Algo inesperado aconteceu.')
except IndexError as erro:
    print('Erro de Índice.')
except ZeroDivisionError as erro:
    print('Não se pode dividir um número por 0 (zero)!')
else:  # o else só será executado caso NÃO haja nenhum "levantamento" de EXCEPTION
    print('Hello World!')
finally:  # sempre será executado ao final. Serve para corrigir exceções que "já foram tratadas" (caso abaixo)
    print(a)
    ar = []  # isso evita que a Exception NameError não seja "levantada", evitando assim, o travamento do código

print('Bora continuar')
print(ar)
