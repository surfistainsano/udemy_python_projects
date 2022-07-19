class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade


class Cliente(Pessoa):
    def inserir_conta(self, conta):
        self._conta_cliente = conta

    @property
    def conta_cliente(self):
        return self._conta_cliente
