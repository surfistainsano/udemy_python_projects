"""
:s - str
:d - int
:f - float
:.2f - o número float fica com 2 casas decimais
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

> - left
< - right
^ - center
"""

num_1 = 1
# print(f'{num_1:$<20}')  # // 1$$$$$$$$$$$$$$$$$$$

num_int = 1132
num_to_float = f'{num_int:&^11.2f}'  # // &&1132.00&&

name = 'Leonardinger'
name_formated = '{:Ç^30}'.format(name)  # // ÇÇÇÇÇÇÇÇÇLeonardingerÇÇÇÇÇÇÇÇÇ

for n in range(-1, -100, -2):
    print(n)
