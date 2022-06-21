# from sys import platform as arroz
# print(arroz)  # é exibido o OS
# # nota-se que é possível alterar o nome padrão da propriedade

import random

for i in range(10):
    print(random.randint(0, 50))


# from random import randint  # uma func com o mesmo nome sobrescreverá a do python
# from random import *  # fica mais ainda difícil de descobrir da onde vem a func (pode ser sobescrita)
# import random  # não é sobescrita, pois se acessa os métodos e propriedades por meio do dot

import pymysql
print(pymysql)
