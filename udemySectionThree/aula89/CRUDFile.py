#
# file = open('abc.txt', 'w+')  # o argumento w+ LIMPA o arquivo e ESCREVE tudo DE NOVO.
# file.write('Linha 1\nLinha 2\nLinha 3')
#
# file.seek(0, 0)  # seek(posição=0, relatividade=0) assim, o "cursor" vai para o começo do file permitindo a leitura
# print(file.read())  # após o read(), é preciso colocar o "cursor" de volta ao começo
#
# print('#' * 20)
#
# file.seek(0, 0)
# print(file.readline(), end='')
# print(file.readline(), end='')  # por padrão, o print() retorna uma quebra de linha no final. O end='string vazia' resolve.
# print(file.read())
#
# print('#' * 20)
#
# file.seek(0, 0)
# # print(file.readlines())  # retorna uma array
# for linha in file:
#     print(linha, end='')
#
# file.close()
#


# other way
# uma boa prática de programação é utilizar try: e finally: para garantir que o arquivo seja fechado

# try:
#     file = open('abc.txt', 'w+')
#     file.write('Arroz sempre é bom')
#     file.seek(0)
#     print(file.read())
# finally:
#     file.close()


# porém, a maneira mais pythonica de manipular arquivos (essa aula é voltada para ABERTURA de arquivos) é:

# with open('abc.txt', 'w+') as file:  # o ->with<- é atribuído ao file
#     file.write('Arroz é vida\nArroz é sucesso\nArroz sempre é bom\n')
#     file.seek(0)
#     print(file.read())

# o gerenciador de contexto ->with<- abre o file, executa o bloco de código e fecha o file após o término


# with open('abc.txt', 'r') as file:  # para ler arquivos
#     print(file.read())


# with open('abc.txt', 'a+') as file:  # APPEND mode
#     file.write('Arroz lixo Kappa\n')
#     file.seek(0)
#     print(file.read())

import json

d1 = {
    'Pessoa 1': {
        'Nome': 'Leonardo',
        'Idade': 23,
    },
    'Pessoa 2': {
        'Nome': 'Lidiane',
        'Idade': 40
    }
}

dictJson = json.dumps(d1, indent=True)

with open('dict.json', 'w+') as file:
    file.write(dictJson)
