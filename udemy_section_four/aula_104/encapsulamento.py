"""
public, protected, private
"""


class BaseDeDados:

    def __init__(self):
        self.__dados = {}

    # caso seja preciso ter acesso aos VALORES do atributo encapsulado, pode-se fazer um GETTER

    @property
    def dados(self):
        return self.__dados

    def inserir_clientes(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def listar_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]


bd = BaseDeDados()
bd.inserir_clientes(1, 'Leo')
bd.inserir_clientes(2, 'Nicole')
bd.inserir_clientes(3, 'Lidiane')
bd.inserir_clientes(4, 'Lilian')
bd.__dados = 'Arroz'  # por causa do __ o python cria uma variável de nome __dados com o valor atribuído
# print(bd.__dados)  # // 'Arroz'
# para acessar o atributo "REAL":
# print(bd._BaseDeDados__dados)  # instancia.NomeDaClasse.__nome_do_atributo
# bd.listar_clientes()
print(bd.dados)

# o encapsulamento no python se dá por convenção
# pondo o _ antes da variável, recomenda-se que não seja acessado tal dado
# o atributo que contém o _ no início foi feito para ser acessado SOMENTE de dentro da classe
# pondo o __ antes da variável, recomenda-se FORTEMENTE que não seja acessado tal dado
# o atributo que contém o __ no início indica que o programador não quer DE MANEIRA ALGUMA que tal dado seja acessado
