def funcao(*args, **kwargs):  # a função irá "empacotar" os argumentos em uma tupla
    # a comunidade pytohn recomenda o nome 'args' ou 'kwargs'
    # kwargs "empacota" em {} e pode-se acessar por meio da keyword
    # print(args)  # acessa-se por meio de index (por ser tupla)
    # print(kwargs['Nacionalidade'])  # acessa-se por meio de brackets informando a kw
    cor = kwargs.get('cor')
    nacionalidade = kwargs.get('nacionalidade')

    # sexo = kwargs['sexo']  # ocorre um erro

    sexo = kwargs.get('sexo')  # é exibido None (sem erro)

    if sexo:
        print('Possui.')
    else:
        print('Não possui.')

    print(sexo)
    print(cor)
    print(nacionalidade)


lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]

funcao(*lista, *lista2, cor='Branca', nacionalidade='Brasileiro', sexo='Masculino')  # passando a lista desempacotada
# os valores posteriores ficarão na mesma tupla
