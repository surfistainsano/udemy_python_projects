import geradorCNPJ

cnpj = '01.511.659/0001-75'

for i in range(100):
    print(geradorCNPJ.formata(geradorCNPJ.gera()))

if geradorCNPJ.valida(cnpj):
    print(f'{cnpj} é válido')
else:
    print(f'{cnpj} é inválido')
