import csv

with open('clientes.csv', 'r') as file:
    # dados = csv.reader(file)  # rtype: list
    # print(dados)  # // <_csv.reader object at 0x000001F0A3F4D300> ou seja, é um ITERADOR
    # next(dados)  # primeiro item consumido (cabeçalho)

    # dados = csv.DictReader(file)
    # fazendo um for é possível acessar por chaves, pois é um dict
    # como ->dados<- é um gerador, não é possível fazer um laço de repetição fora do context manager ->with<-, pois
    # o arquivo fora fechado. Logo, é possível fazer uma list comprehension para subir, de vereda, os dados na memória

    dados = [x for x in csv.DictReader(file)]

with open('clientes002.csv', 'w') as file:
    escreve = csv.writer(
        file,
        delimiter=',',  # delimitador de tabelas do arquivo
        quotechar='"',  # é definido o caracter de aspas do arquivo (evita que arquivos com aspas gerem erros)
        quoting=csv.QUOTE_ALL  # é definido que todos os valores do arquivos estejam entre aspas duplas
    )

    head = dados[0].keys()
    head = list(head)

    escreve.writerow(
        [
            head[0],
            head[1],
            head[2],
            head[3]
        ]
    )

    for dado in dados:
        escreve.writerow(
            [
                dado['Nome'],
                dado['Sobrenome'],
                dado['E-mail'],
                dado['Telefone']
            ]
        )
