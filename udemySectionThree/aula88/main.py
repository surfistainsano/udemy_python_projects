from vendas.calculaPrecos import aumento, desconto
from vendas.formata.preco import real

valor = 49.90
valorAumentado = aumento(valor, 40, True)
valorDiminuido = desconto(valor, 40, True)
print(valorAumentado)
print(valorDiminuido)
print(real(valor))
