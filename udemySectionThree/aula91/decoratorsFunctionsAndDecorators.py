# def master(funcao):
#     def slave(*args, **kwargs):
#         print('Agora estou decorada.')
#         funcao(*args, **kwargs)
#     return slave
#
#
# @master  # agora, a função falaOi() está decorada (passa pela função MASTER)
# def falaOi():
#     print('Oi')
#
#
# @master
# def showMsg(msg):  # foi usado *args e **kwargs para resolver o erro de parâmetro, assim a função SLAVE replica a função decorada
#     print(msg)
#
#
# falaOi()  # nota-se que a função falaOi() é SLAVE da função MASTER
#
# # falaOi = master(falaOi)  # nesse momento, a funcão falaOi() está DECORADA
#
# showMsg('Olá, eu sou o Leonardo.')

print('#' * 22)

# a função decoradora é usada para adicionar um recurso a uma função
# por exemplo, gerar um log após a execução de uma função

# função decoradora para calcular o tempo de uma função:

from time import time
from time import sleep


def velocidade(funcao):
    def interna(*args, **kwargs):
        startTime = time()
        resultado = funcao(*args, **kwargs)
        endTime = time()
        tempo = (endTime - startTime) * 1000
        print(f'\nA função {funcao.__name__} levou o tempo de {tempo:.2f}ms para executar.')

    return interna


@velocidade
def demora():
    for i in range(10000):
        print(i, end='')


demora()
