from banco import Banco
from cliente import Cliente
from conta import ContaPoupanca, ContaCorrente, InsufficientFoundsError


if __name__ == '__main__':
    cliente1 = Cliente('Leonardo', 23)
    cliente2 = Cliente('Laura', 26)
    cliente3 = Cliente('Luana', 36)

    conta1 = ContaCorrente(3070, 4444, 0)
    conta2 = ContaCorrente(9966, 3333, 100)
    conta3 = ContaPoupanca(6666, 5555, 200)

    cliente1.inserir_conta(conta1)
    cliente2.inserir_conta(conta2)
    cliente3.inserir_conta(conta3)

    banco = Banco()

    banco.inserir_conta(conta1)
    banco.inserir_conta(conta2)
    banco.inserir_conta(conta3)

    banco.inserir_cliente(cliente1)
    banco.inserir_cliente(cliente2)
    banco.inserir_cliente(cliente3)

    if banco.autenticar(cliente1):
        try:
            conta1.sacar(100)
        except InsufficientFoundsError as e:
            print('Saldo insuficiente.')
            print(e)
    else:
        print('Aconteceu algo inesperado.')
