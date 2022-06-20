# 1

def saudacao(saudacao, nome):
    print(f'Olá {nome} {saudacao}')


# saudacao('seja bem vindo!', 'Leonardo')

# 2


def soma(n1, n2, n3):
    print(n1 + n2 + n3)


# soma(1, 2, 3)

# 3


def juros(n1, n2):
    n2 = n2/100
    return n1 + (n1 * n2)


# print(juros(30, 100))

# 4


def fizzBuzz(num):
    modulo3 = num % 3
    modulo5 = num % 5

    if modulo3 == 0 and modulo5 == 0:
        return f'FizzBuzz {num}'
    if modulo3 == 0:
        return f'fizz {num}'
    if modulo5 == 0:
        return f'buzz {num}'
    return num


from random import randint

for i in range(100):
    aleatorio = randint(0, 100)
    print(fizzBuzz(aleatorio))
