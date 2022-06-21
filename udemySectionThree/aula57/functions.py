var = 'valor'


def function():
    print(var)


# def function2():
#     global var  # é possível modificar var globais por meio da kw 'global' NÃO É UMA BOA PRÁTICA
#     var = 'Feijão'
#     print(var)

def function2(arg=None):
    arg = arg.replace('v', 'c')
    return arg


function()
otherVar = function2(arg=var)
print(otherVar)


def func():
    var1 = 'Variável criada dentro de uma função.'
    return var1


def func2(arg):
    print(arg)


returnOfFunc = func()
func2(returnOfFunc)

# TRABALHAR COM VAR DE DENTRO DA FUNÇÃO É UMA BOA PRÁTICA. LOGO, NEM SEMPRE HÁ NECESSIDADE DE CRIAR VAR GLOBAIS.
