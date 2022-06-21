from vendas.calculaPrecos import aumento, desconto
from vendas.formata import preco as preco2

valor = 49.90
valorAumentado = aumento(valor, 40, True)
valorDiminuido = desconto(valor, 40, True)
print(valorAumentado)
print(valorDiminuido)
print(preco2.real(50))
