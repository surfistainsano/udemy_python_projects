# 1


# def funcao1(arg):
#     return arg()
#
#
# def funcao2():
#     return 'Valor da função 2.'
#
#
# resultado = funcao1(funcao2)
#
# print(resultado)


# 2


# def funcao1(arg, **kwargs):
#     print(arg)
#     func3 = kwargs.get('func3')
#     func4 = kwargs.get('func4')
#     print(func3)
#     print(func4)
#
#
# def funcao2():
#     texto = 'Valor da função 2.'
#     return texto
#
#
# varFuncao2 = funcao2()
#
#
# def funcao3(estado, cidade):
#     return f'Estado: {estado} e Cidade: {cidade}'
#
#
# def funcao4(carro, marca, ano):
#     return f'Carro: {carro}, Marca: {marca} e Ano: {ano}'
#
#
# funcao1(varFuncao2, func3=funcao3('Santa Catarina', 'Balneário Gaivota'),
#         func4=funcao4('Lancer', 'Mitsubishi', '2009'))


# CORREÇÃO


def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def funcao1(cidade, estado):
    return f'Cidade: {cidade} e Estado: {estado}'


def funcao2(carro, marca, ano):
    return f'Carro: {carro}, Marca: {marca} e Ano: {ano}'


executando = mestre(funcao1, 'Gaivota', estado='Santa Catarina')
executando2 = mestre(funcao2, 'Lancer', 'Mitsubishi', ano='2009')
print(executando)
print(executando2)
