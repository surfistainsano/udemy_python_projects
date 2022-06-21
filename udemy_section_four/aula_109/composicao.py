# Composição: Uma classe é DONA de outros objetos. Logo, A classe sendo apagada os objetos que ela utilizou, serão
# apagados também

class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def inserir_enderecos(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))  # o objeto é instanciado como um item da array atribuida a
        # self.enderecos. Nesse momento, é feita a composição, pois a classe Cliente é responsável por instanciar a
        # classe Endereco

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)


class Endereco:  # a instancia da classe Endereco pertence à classe Cliente. Logo, apagando a instancia de Cliente, o
    # objeto da classe Endereco é apagado junto por pertencer a classe Cliente.
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado
