class Banco:

    def __init__(self):
        self._agencias = [3070, 14109, 7822, 5548, 9966]
        self._contas = []
        self._clientes = []

    def inserir_conta(self, conta):
        self._contas.append(conta.conta)

    def inserir_cliente(self, cliente):
        self._clientes.append(cliente)

    def autenticar(self, _cliente):
        for cliente in self._clientes:
            if cliente.conta_cliente.agencia in self._agencias and \
                    cliente.conta_cliente.conta in self._contas and \
                    _cliente in self._clientes:
                return True
