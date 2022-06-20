# toda função em python retorna NONE por padrão

def converteNumero(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass


numero = converteNumero(input('Digite um número: '))

if numero is not None:
    print(numero * 5)
else:
    print('Valor inválido.')




