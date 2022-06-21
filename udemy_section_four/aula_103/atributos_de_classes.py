class A:
    vc = 123


a1 = A()
a2 = A()

# A.vc = 321  # aqui, altera-se a variável da classe

a1.vc = 321  # aqui, CRIA-SE uma variável chamada vc diretamente na instância da classe

print(a1.__dict__)  # variável da instância
print(a2.__dict__)  # variável da classe
print(A.__dict__)  # variável da classe

print(a1.vc)
print(a2.vc)
print(A.vc)
print('#' * 20)


# deve-se ter cuidado, pois a expressão ->a1.vc = 321<- CRIA uma variável, ou seja, não ALTERA o valor da variável de
# classe

class B:
    vc = 123

    def __init__(self):
        self.vc = 321


b1 = B()
b2 = B()

print(b1.vc)
print(b2.vc)
print(B.vc)
