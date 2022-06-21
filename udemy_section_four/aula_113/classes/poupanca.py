from udemy_section_four.aula_113.classes.conta import Conta


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo < valor:
            print('Saldo Insuficiente.')
            return

        self.saldo -= valor
        self.detalhes()
