from dados import lista, produtos, pessoas

# usando LAMBDA

# novaLista = filter(lambda p: p['preco'] < 30, produtos)
#
# for preco in novaLista:
#     print(preco)

# usando FUNCTION
# a vantagem é que se pode usar a mesma função em outros lugares


# def lessThirty(p):
#     if p['preco'] <= 30:
#         p['barato'] = True  # uma má pratica, pois se deve utilizar o map()
#     return True             # incorreto usar o filter() para retornar True sempre
#
#
# precos = filter(lessThirty, produtos)  # o filter irá retornar APENAS os valores TRUE
#
# for preco in precos:
#     print(preco)

def filterpeople(p):
    if p['idade'] >= 18:
        return True
    else:
        return False


newPeoples = filter(filterpeople, pessoas)  # o filter irá retornar APENAS os valores TRUE

for pessoa in newPeoples:
    print(pessoa)
