class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nome_da_classe = self.__class__.__name__

    def falar(self):
        print(f'{self.nome_da_classe} falando...')


class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nome_da_classe} comprando...')

    def falar(self):
        print('Falando da classe Clientes!')


class Aluno(Pessoa):  # SUB CLASSE
    def estudar(self):  # método exclusivo da sub classe
        print(f'{self.nome_da_classe} estudando...')


class ClienteVip(Cliente):  # ClienteVip HERDA de cliente que HERDA de Pessoa. Logo, ClienteVip HERDA de Pessoa.
    # para criar um método __init__ na sub classe, sem sobrescrever o método __init__ da super classe
    def __init__(self, nome, idade, favorite_color, sobrenome):
        # Pessoa.__init__(self, nome, idade)  # pode-se chamar o __init__ pelo nome da Classe também
        super().__init__(nome, idade)
        self.color = favorite_color
        self.sobrenome = sobrenome

    # para executar o método da super classe antes de ser sobrescrito:
    # def falar(self):
    #     # Pessoa.falar(self)  # pode-se chamar o método pelo nome da classe também
    #     super().falar()  # é executado o método da super classe (é seguido a lógica da herança)
    #     print('O código que se deseja executar.')

    def falar(self):
        Pessoa.falar(self)
        Cliente.falar(self)
        print(f'{self.nome} {self.sobrenome}')

    """
    def falar(self):  # nesse momento, o método é sobrescrito
        print('Outra coisa')
    """

# ao observar o módulo utils.py, nota-se após instanciar o objeto e chamar o método .falar(), o interpretador do python
# irá procurar tal método na classe que o chamou - ClienteVip. Não encontrando, irá subir pela lógica da herança, ou
# seja, irá procurar o método na classe Cliente. Não encontrando, irá procurar na super classe Pessoa. Encontrando-o,
# será executado. Por isso, deve-se ficar atento à sobreposição de membros.
