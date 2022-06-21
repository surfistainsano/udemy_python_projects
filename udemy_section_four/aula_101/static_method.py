from random import randint


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

    @staticmethod  # decorador
    def gera_id():  # os métodos ESTÁTICOS independem da CLASSE e do OBJETO. Logo, não é possível acessar outras variá-
        # veis. As variáveis criadas, limitam-se ao escopo do static method.
        rand = randint(10000, 19999)
        return rand


p1 = Pessoa('Leonardo', 23)

print(Pessoa.gera_id())
print(p1.gera_id())
# nota-se que é possível ter acesso ao static method pela Class e pelo Object (por estar dentro da classe)
# o método get_birth_year, por ser um método de instância, precisa do parâmetro SELF
# o método por_ano_nascimento, por ser um método de classe, precisa do parâmetro CLS e, do decorador @classmethod
# SELF é a instância em si
# CLS é a classe em si
