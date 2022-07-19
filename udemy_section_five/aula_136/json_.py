import json
from dados import *

lista = ['a', 'b', 'c', 'd', 'e']
dados_json = json.dumps(lista)  # converte o tipo do dado para uma string que contém dados json
print(type(dados_json))  # // <class 'str'> | É uma string que contém dados json

object_json = json.dumps(clientes_dicionario, indent=4)
print(object_json)  # mesmo sendo idêntico a um dicionário, é uma string que contém dados json no
# formato de um object


object_to_dict = json.loads(clientes_json)

for k, v in object_to_dict.items():
    print(k, v)

with open('arquivo.json', 'w') as file:
    json.dump(clientes_dicionario, file, indent=4)


with open('arquivo.json', 'r') as file:
    dados = json.load(file)

print(dados, type(dados))

for k, v in dados.items():
    print(k)
    print(v)
