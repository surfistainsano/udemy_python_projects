"""
Usando ->f strings<- é possível formatar desta maneira:
num = 3.333333
var = f'Número formatado: {num:.2f}' | // Número formatado: 3.33
"""

# Outra maneira:
nome = 'Leo'
idade = 23
altura = 1.85

print('Meu nome é {2} |{0}|{1}|{2}|, tenho {0} anos e meço {1} de altura.'.format(nome, idade, altura))
# Nota-se que a função .format() trabalha com index
# Para trabalhar com kw:
print('Meu nome é {c} |{a}|{b}|{c}|, tenho {a} anos e meço {b} de altura.'.format(a=nome, b=idade, c=altura))
