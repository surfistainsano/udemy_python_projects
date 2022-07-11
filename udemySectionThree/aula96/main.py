import geradorCNPJ

cnpj = '01.511.659/0001-75'

for i in range(100):
    a = geradorCNPJ.formata(geradorCNPJ.gera())

    if geradorCNPJ.valida(a):
        print(f'{a} é válido')
    else:
        print(f'{a} é inválido')
