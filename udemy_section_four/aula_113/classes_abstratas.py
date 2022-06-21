from abc import ABC, abstractmethod


# uma classe abstrata serve como base para outras classes não necessitando ser instanciada

class A(ABC):  # ABC significa Abstract Base Class
    # para criar um método abstrato, a fim de que outras classes forcem sua criação. Logo, as classes filhas da classe A
    # terão tal método
    @abstractmethod
    def falar(self):
        pass


class B(A):
    def falar(self):  # nota-se que o método foi sobreposto e por isso foi possivel instanciar a classe B
        print('Falando... B...')


# a = A()  # Exception
a = B()
a.falar()
