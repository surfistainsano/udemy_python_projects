import openpyxl

pedidos = openpyxl.load_workbook('pedidos.xlsx')  # A variável herda os métodos e propriedades do WorkBook
nome_planilhas = pedidos.sheetnames  # É exibido o nome das planilhas existentes no arquivo
planilha1 = pedidos['Página1']  # É possível selecionar a planilha como se fosse um dict

"""
É importante notar que o pycharm não dá sugestões para a variável ->planilha1<- ao fazer um acesso com o dot.
Por isso é importante ler a documentação, para ter conhecimento do que esse módulo é capaz de fazer.
Essa variável retorna um object Worksheet.
"""

# Para acessar a célula B4 da planilha:
# print(planilha1['b4'])  # // object Cell

cell_b4_value = planilha1['b4'].value  # retorna o valor da célula b4

column_b = planilha1['b']  # Retorna uma tupla; cada item é um object Cell representando uma linha.

"""
# Para consultar um range (intervalo) de células:
for linha in planilha1['a1:c2']:  # planilha1['a1:c2'] Retorna uma tupla contendo as células daquela linha
    # em outra tupla | // ((<Cell 'Página1'.A1>, <Cell 'Página1'.B1>, <Cell 'Página1'.C1>),
    # (<Cell 'Página1'.A2>, <Cell 'Página1'.B2>, <Cell 'Página1'.C2>))
    for coluna in linha:
        print(coluna.value)
"""

# É possível percorrer a planilha inteira:
for linha in planilha1:
    # len(linha) Para saber a quantidade de colunas na linha
    if linha[0].value is not None:
        print(linha[0].value, end=" ")
    if linha[1].value is not None:
        print(linha[1].value, end=" ")
    if linha[2].value is not None:
        print(linha[2].value)
