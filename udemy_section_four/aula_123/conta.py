from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    @property
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)):
            raise TypeError("Valor != de int, float")
        self._saldo += valor

    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise TypeError("Valor != de int, float")
        self._saldo += valor
        self.detalhes()

    def detalhes(self):
        print(f'Agência: {self._agencia}.')
        print(f'Conta: {self._conta}.')
        print(f'Saldo: {self._saldo}.')

    @abstractmethod
    def sacar(self, valor):
        pass


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):
        super().__init__(agencia, conta, saldo)
        self._limite = limite

    @property
    def limite(self):
        return self._limite

    def sacar(self, valor):
        if not isinstance(valor, (int, float)):
            raise TypeError("Valor != de int, float")
        if (self._saldo + self._limite) < valor:
            raise InsufficientFoundsError("Valor é maior do que a soma do saldo e limite.")
        self._saldo -= valor
        self.detalhes()


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self._saldo < valor:
            raise InsufficientFoundsError("Valor é maior do que a soma do saldo e limite.")
        self._saldo -= valor
        self.detalhes()


class InsufficientFoundsError(Exception):
    pass
