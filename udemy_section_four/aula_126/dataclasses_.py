from dataclasses import dataclass


# o dataclass é um decorador que cria os métodos __init__ | __repr__ | __eq__ (etc) automaticamente
@dataclass(eq=True, repr=True, order=False, frozen=False, init=True)  # é possível negar a criação de tal magicmethod
class Pessoa:
    nome: str
    sobrenome: str

    def __post_init__(self):  # é executado depois do __init__
        self.nome_completo = f'{self.nome} {self.sobrenome}'


p1 = Pessoa('Leonardo', 'Luders')
p6 = Pessoa('Leonardo', 'Luders')
p2 = Pessoa('Lidiane', 'Correa')
p3 = Pessoa('Luana', 'Oliveira')
p4 = Pessoa('Lilian', 'Paulino')
p5 = Pessoa('Igor', 'Cunha')

# order=True
pessoas = [p1, p2, p3, p4, p5]
pessoas = sorted(pessoas, key=lambda pessoa: pessoa.sobrenome)
print(pessoas)

print(p1)  # // Pessoa(nome='Leonardo', sobrenome='Luders')
print(p1 == p6)  # // True, pois os dados são iguais. Ora, o método __eq__ já foi criado.

# @dataclass(eq=True, repr=True, order=False, frozen=False, init=True)
# init=False | será necessário criar o método __init__
# frozen=True | não será possível editar qualquer valor na classe, ou seja, acima, será levantada uma exceção.
# Torna a classe imutável.
# order=True | permite que funções como sorted() possam ser utilizadas para organizar classes em uma array, por exemplo
# é possível ocultar um atributo de aparecer no __repr__

from dataclasses import field
from dataclasses import asdict, astuple


@dataclass
class Carro:
    marca: str
    modelo: str = field(repr=False)


c1 = Carro('Mitsubishi', 'Lancer')
c2 = Carro('Toyota', 'Corolla')

# para converter class em dict ou tuple
print(asdict(c1))
print(astuple(c2))
# dataclass não funciona tão bem com herança como classes normais
