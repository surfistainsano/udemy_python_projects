cpfCliente = '168.995.350-09'

newCpf = cpfCliente.split('.')
newCpf += newCpf[2].split('-')
del(newCpf[2:3])
firstDigitClient = newCpf[3][0]
secondDigitClient = newCpf[3][1]
cpfFormated = ''.join(newCpf)
cpfFinalFormated = cpfFormated
cpfFormated = cpfFormated[:9]
lista = list(range(10, 1, -1))
lista2 = list(range(11, 1, -1))

acumulador1 = 0
acumulador2 = 0
digito1 = ''
digito2 = ''

for v1, v2 in enumerate(cpfFormated):
    v2 = int(v2)
    soma = v2 * lista[v1]
    acumulador1 += soma

calcFirstDigit = 11 - (acumulador1 % 11)

if calcFirstDigit > 9:
    digito1 = 0
else:
    digito1 = calcFirstDigit

cpfWithFirstDigit = cpfFormated + firstDigitClient

for v1, v2 in enumerate(cpfWithFirstDigit):
    v2 = int(v2)
    soma = v2 * lista2[v1]
    acumulador2 += soma

calcSecondDigit = 11 - (acumulador2 % 11)

digito2 = calcSecondDigit
digito1 = str(digito1)
digito2 = str(digito2)

cpfValided = cpfFormated + digito1 + digito2

if cpfFinalFormated == cpfValided:
    print(f'O CPF {cpfCliente} é válido!')
else:
    print(f'O CPF {cpfCliente} não é válido')

# À MODA DE LUIZ OTÁVIO SENPAI

# while True:
#     # cpf = '08177991922'
#     cpf = input('Digite um CPF: ')
#     novoCpf = cpf[:-2]
#     reverso = 10
#     total = 0
#     for index in range(19):
#         if index > 8:
#             index -= 9
#
#         total += int(novoCpf[index]) * reverso
#
#         reverso -= 1
#         if reverso < 2:
#             reverso = 11
#             d = 11 - (total % 11)
#
#             if d > 9:
#                 d = 0
#             total = 0
#             novoCpf += str(d)
#
#     sequencia = novoCpf == str(novoCpf[0] * 11)
#
#     if cpf == novoCpf and not sequencia:
#         print('Válido!')
#     else:
#         print('Inválido!')


# Gerador de CPF

from random import randint

numero = str(randint(100000000, 999999999))

novoCpf = numero
reverso = 10
total = 0
for index in range(19):
    if index > 8:
        index -= 9

    total += int(novoCpf[index]) * reverso

    reverso -= 1
    if reverso < 2:
        reverso = 11
        d = 11 - (total % 11)

        if d > 9:
            d = 0
        total = 0
        novoCpf += str(d)

print(novoCpf)
