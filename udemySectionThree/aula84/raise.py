#  raise = levantar

# def divisao(n1, n2):
#     try:
#         n1 / n2
#     except ZeroDivisionError as erro:
#         print('Log:', erro)
#         raise  # com a kw raise, o programador pode levantar exceções mesmo que já estejam sendo tratadas
#
#
# try:
#     divisao(2, 0)
# except ZeroDivisionError as erro:
#     print(erro)


# Personalized Exception

def divide(n1, n2):
    if n2 == 0:
        raise ValueError("o segundo parâmetro não pode ser zero.")  # lançamento da exceção
    return n1 / n2


try:
    print(divide(4, 0))
except ValueError as erro:
    print('Você está tentando dividir por zero.')  # relançamento da exceção
    print('Log:', erro)
