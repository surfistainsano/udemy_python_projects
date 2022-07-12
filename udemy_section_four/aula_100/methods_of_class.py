class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_birth_year(self):  # os métodos de INSTÂNCIA tem relação com o objeto instanciado.
        print(self.ano_atual - self.idade)

    @classmethod  # decorador
    def por_ano_nascimento(cls, nome, ano_nascimento):  # os métodos de CLASSE independem de objetos instanciados.
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)


p1 = Pessoa.por_ano_nascimento('Leonardo', 1999)
print(p1.nome)
print(p1.idade)
p1.get_birth_year()
