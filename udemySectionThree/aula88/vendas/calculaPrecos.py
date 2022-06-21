from udemySectionThree.aula88.vendas.formata import preco


def aumento(valor, porcentagem, formata=False):
    total = valor + (valor * (porcentagem / 100))

    if formata:
        return preco.real(total)
    else:
        return total


def desconto(valor, porcentagem, formata=False):
    total = valor - (valor * (porcentagem / 100))

    if formata:
        return preco.real(total)
    else:
        return total
