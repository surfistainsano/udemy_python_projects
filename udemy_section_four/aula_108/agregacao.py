# Agregação: Uma classe precisa de outra classe, porém as duas existem separadamente

class CarrinhoDeCompras:

    def __init__(self):
        self.produtos = []

    def inserir_produtos(self, produto):
        self.produtos.append(produto)

    def lista_produtos(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)

    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return total


class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

# nota-se que a classe CarrinhoDeCompras pode existir sozinha, porém depende de produtos para funcionar corretamente
# igualmente, a classe Produto pode existir sozinha e associar-se com outras classes do programa
