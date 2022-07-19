class Retangulo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_area(self):
        return self.x * self.y

    def __repr__(self):  # modifica a exibição do objeto instanciado ->r3 = r1 + r2<- (fins didáticos)
        return f"<class 'Retangulo({self.x}, {self.y})'>"

    def __add__(self, other):  # assim, é ensinado ao interpretador o que o sinal operador + deve fazer
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Retangulo(novo_x, novo_y)

    def __lt__(self, other):  # < (less than)
        a1 = self.get_area()
        a2 = other.get_area()
        if a1 < a2:
            return True
        else:
            return False

    def __gt__(self, other):  # > (grand than)
        a1 = self.get_area()
        a2 = other.get_area()
        if a1 > a2:
            return True
        else:
            return False

    def __eq__(self, other):  # == (equals)
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False


r1 = Retangulo(10, 20)
r2 = Retangulo(10, 20)

# print(r1 == r2)  # sem ensinar o que o sinal operador == deve retornar, dará como resultado False, pois ele,
# no momento, está comparando o endereço da memória do objeto, ou seja, são diferentes.

print(r1 == r2)
