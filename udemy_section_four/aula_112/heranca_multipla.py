# Herança Múltipla

class A:
    def falar(self):
        print('Estou em A')


class B(A):
    def falar(self):
        print('Estou em B')


class C(A):
    def falar(self):
        print('Estou em C')


class D(B, C):
    def falar(self):
        print('Estou em D')


d = D()
d.falar()
