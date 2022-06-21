class Carro:

    def __init__(self, marca, modelo, ano, hp):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.hp = hp

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, valor):
        if isinstance(valor, str):
            valor = int(valor.replace('hp', ''))
        self._hp = valor

    def zero_a_cem(self, porcentagem):
        if self.hp >= 300:
            self.hp += self.hp * (porcentagem / 100)
            return 'é potente'
        else:
            self.hp += self.hp * (porcentagem / 100)
            return 'não tão potente'


c1 = Carro('Fiat', 'Argos', 2020, '350hp')
print(c1.zero_a_cem(20))
