# A herança funciona de cima para baixo (hierarquia)

class Pessoa:  # SUPER CLASSE
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nome_da_classe = self.__class__.__name__  # para saber o nome da classe responsável por instanciar

    def falar(self):
        print(f'{self.nome_da_classe} falando...')


class Cliente(Pessoa):  # SUB CLASSE  # nesse momento, a classe Cliente HERDA os métodos e propriedades da classe Pessoa
    def comprar(self):  # método exclusivo da sub classe
        print(f'{self.nome_da_classe} comprando...')


class Aluno(Pessoa):  # SUB CLASSE
    def estudar(self):  # método exclusivo da sub classe
        print(f'{self.nome_da_classe} estudando...')

# nota-se que as sub classes são ESPECIFICAÇÕES da super classe, ou seja, utiliza-se atributos "genéricos" da super
# classe que são comuns nas sub classes e essas podem possuir seus próprios métodos e propriedades, assim especializan-
# do-se.
