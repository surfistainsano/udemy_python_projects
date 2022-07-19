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
    def saldo(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Saldo precisa ser numérico.")
        self._saldo = value

    def depositar(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Valor do depósito precisa ser numérico.")

        self._saldo += value
        self.detalhes()

    def detalhes(self):
        print(f'Agência: {self._agencia}', end=' ')
        print(f'Conta: {self._conta}', end=' ')
        print(f'Saldo: {self._saldo}')

    @abstractmethod
    def sacar(self, valor):
        pass
