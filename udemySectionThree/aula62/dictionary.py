# dicionários possuem chave e valor

# d1 = {'chave1': 'valor da chave 1'}  # um modo de criar dict

d1 = dict(chave1='valor da chave 1', chave2='valor da chave 2')  # outro modo de criar dict

d1['chave3'] = 'valor da chave 3'

# print(d1)

d2 = {'str': 'String', 123: 'Number', (1, 2, 3, 'Arroz'): 'Olá Marilene'}  # nota-se que os dicionários suportam
# NOMES de chaves do tipo IMUTÁVEIS

# print(d2[(1, 2, 3, 'Arroz')])

d2['naoexiste'] = 'Arroz'

if d2.get('naoexiste') is not None:  # com o .get é possível burlar uma exceção, para que o programa não pare na linha
    # do erro
    print(d2.get('naoexiste'))

d2.update({'arroz': 'Arroz de fato'})  # a func update recebe como argumento um dict {valor: chave}

# print(d2)

del d2['arroz']  # assim, exclui-se a chave de nome 'arroz'

# print(d2)

print('str' in d2)  # boolean result
print('str' in d2.keys())  # redundande, pois é verificada a chave por padrão
print('Olá Marilene' in d2.values())  # método para verificar se valor contém no dict
print(len(d2))  # exibe a quantidade de PARES do dict

# for k in d2:  # novamente, é verificada as chaves por padrão
#    print(k)

# for v in d2.values():  # Logo, pode-se iterar sobre os valores do dict
#     print(v)
#
# for k in d2.items():  # uma maneira de acessar chave/valor do dict separadamente no mesmo laço (POR INDEX)
#     print(k[0], k[1])

# for k, v in d2.items():  # desempacotando, pode-se ter 2 variáveis independentes
#    print(k, v)

d3 = {'cliente1': {'nome': 'Leonardo', 'sobrenome': 'Luders', 'profissao': 'programador'},
      'cliente2': {'nome': 'Leonardo', 'sobrenome': 'Luders', 'profissao': 'programador'},
      'cliente3': {'nome': 'Leonardo', 'sobrenome': 'Luders', 'profissao': 'programador'}}

# for cliente_k, cliente_v in d3.items():
#     print(cliente_k)
#     for dado_k, dado_v in cliente_v.items():
#         print(dado_k, dado_v)
#         # assim, é possível iterar um dict dentro de um dict

d4 = {1: 'a', 2: 'b', 3: 'c', 'd': ['Leonardo', 'Lüders']}
copyD4 = d4.copy()  # como o valor da chave d é MUTAVEL - por ser uma array - ao modificar o valor do primeiro item
# da array (como é exibido abaixo), o dicionário original é alterado também. .copy = shalowcopy (cópia rasa), ou seja,
# significa que é possível alterar os valores

copyD4['d'][1] = 'ARROZ'

# print(d4)
# print(copyD4)

# para copiar, de fato, o dicionário: (os dict's tornam-se independentes)

# import copy
#
# d5 = {1: 'a', 2: 'b', 3: 'c', 'd': ['Leonardo', 'Lüders']}
# deepCopyD5 = copy.deepcopy(d5)
#
# deepCopyD5['d'][1] = 'Kristian'
#
# print(d5)
# print(deepCopyD5)

d6 = {1: 'a', 2: 'b', 3: 'c', 'd': ('Leonardo', 'Lüders')}
copyD6 = d6.copy()

copyD6['d'] = ('Arroz', 'Doce')

# d6.pop()  # informar a chave para exclusão

d6.popitem()  # igual ao pop da array

d2.update(d6)  # "concatenar" dict's

print(d2)
