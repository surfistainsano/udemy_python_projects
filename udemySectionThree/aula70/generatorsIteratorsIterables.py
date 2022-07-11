import sys
import time

lista = [1, 2, 3, 4, 5]

print(hasattr(lista, '__iter__'))

listaIter = iter(lista)

print(hasattr(listaIter, '__next__'))

# a lista é ITERÁVEL, mas não é do tipo ITERADOR
# o for transforma a lista em ITERADOR por conta da variável contadora

lista1 = list(range(100))  # desse modo, os valores são atribuidos ao mesmo tempo na lista, ou seja, exige muita memória
print(sys.getsizeof(lista1))


# por isso, utiliza-se generator, a fim de obter os valores somente quando necessário
# geradores são ITERÁVEIS e por serem ITERADORES possuem o método next e iter


# def gera():
#     r = []
#     for n in range(100):
#         yield n
#         time.sleep(0.1)
#
#
# g = gera()
#
# print(hasattr(g, '__next__'))  # True

def gera():
    variavel = 'Valor1'
    yield variavel
    variavel = 'Valor2'
    yield variavel
    variavel = 'Valor3'
    yield variavel


g = gera()

for v in g:
    print(v)

# mesmo não tendo um contador no método é exibido cada valor
# toda vez que desejar exibir o próximo retorno de um método, o gerador se mostra promissor

compList = [x for x in range(100000)]
# print(type(compList))
compGen = (x for x in range(100000))  # mudando para parênteses tem-se um generator
# print(type(compGen))

print(sys.getsizeof(compList))
print(sys.getsizeof(compGen))

# lista: retém t odo o valor e o joga na memória
# generator: retém t odo o valor e não o joga na memória, ou seja, somente é exibido quando solicitado tanto com a func
# next(), quanto com um for
