# def soma(n1=1, n2=1):  # serve para não ter exception por parâmetro vazio
#     print(n1 + n2)
#
#
# soma(n2=5, n1=99)  # serve para atribuir um valor somente no segundo parâmetro. Logo, pode-ser inverter a ordem.
# # isso é possível somente mandando valores nomeados
# soma(2, 2)
# soma(5, 5)

# Aula53
# functions002

# a função que não contiver 'return' retornará um valor do tipo None
# após a palavra chave 'return', as linhas abaixo são ignoradas

# def dividir(n1, n2):
#     if n2 == 0:
#         return
#
#     return n1 / n2
#
#
# divisao = dividir(8, 0.5)
#
# if divisao:
#     print(divisao)
# else:
#     print('Conta inválida')

def function1(a):
    print(a)


def function2():
    return function1


arroz = function2()
arroz('Deu boa hein')

# nota-se que é possível atribuir à variável o corpo de uma função
