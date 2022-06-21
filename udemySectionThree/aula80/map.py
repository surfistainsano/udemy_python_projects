from dados import produtos, pessoas, lista

# a função map() recebe uma function como primeiro argumento. Logo, o segundo é o iterável
# a função map() aplica a função posta no primeiro argumento em cada item do iterável (segundo argumento)

# mapList = map(lambda x: x * 2, lista)
# mapList = list(mapList)
# print(mapList)

# adicionar uma porcentagem sobre os precos que estão dentro de um dict


def aumentaPreco(p):
    p['preco'] = round(p['preco'] * 1.05, 2)
    return p


novosProdutos = map(aumentaPreco, produtos)

# for produto in novosProdutos:
#     print(produto)

# listar os nomes das pessoas do dict


def newAge(p):
    p['novaIdade'] = round(p['idade'] * 1.20)
    return p


nomesPessoas = map(newAge, pessoas)  # será retornado um objeto map (iterador)

for pessoa in nomesPessoas:
    print(pessoa)

# compNomes = [x['nome'] for x in pessoas]  # será retornado uma ARRAY (iterável)
