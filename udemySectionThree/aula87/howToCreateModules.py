import math

PI = math.pi


def dobraLista(lista):
    return [x * 2 for x in lista]


def multiplicaLista(lista):
    r = 1
    for n in lista:
        r *= n
    return r


lista = [1, 2, 3, 4, 5]

if __name__ == '__main__':
    print(dobraLista(lista))
    print(multiplicaLista(lista))
    print(PI)
