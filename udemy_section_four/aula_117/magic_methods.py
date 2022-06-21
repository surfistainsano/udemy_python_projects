# sempre terão o formato __magicmethod__
# permitem a mudança do comportamento da classe
# toda classe em python deriva do ->object<-

# class A:
#     def __new__(cls, *args, **kwargs):  # __new__ é o construtor em parceria com o __init__. O __new__ é o 1st chamado.
#         print('Eu sou o __new__')
#         return object.__new__(cls)  # return para que não seja sobrescrito o método __new__
#
#     def __init__(self):  # é iniciado NO MOMENTO DA INSTANCIAÇÃO do objeto.
#         print('Eu sou o __init__')
#
#
# a = A()


# class A:
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls, '_jaexiste'):
#             cls._jaexiste = object.__new__(cls)
#
#         return cls._jaexiste
#
#     def __init__(self):
#         print('Eu sou o __init__')
#
#
# a = A()
# b = A()
# c = A()
#
# print(a == c)
# # True, pois foi modificado o magicmethod __new__, para que retorne a mesma classe para qualquer instância
# print(id(a), id(b), id(c))  # todos iguais, pois são AS MESMAS instâncias


class A:
    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):  # possibilita chamar o objeto como uma função | a = A() | a(paramer, paramer)
        result = 1

        for i in args:
            result *= i

        return result

    # def __setattr__(self, key, value):
    #     self.__dict__[key] = value  # configurado para settar o valor
    #     # t odo set de atributo novo passa por esse método

    # é possível intervir durante um set de um atributo:
    def __setattr__(self, key, value):
        if key == 'nome':
            self.__dict__[key] = 'The jokes on you!'
        else:
            self.__dict__[key] = value

    def __str__(self):  # altera o retorno ao printar um objeto instanciado | a = A() | print(a) // "<class 'A'>"
        return "<class 'A'>"

    def __len__(self):  # a = A() | print( len(a) ) // 22
        return 22

    def __del__(self):  # não é garatido que o método seja executado sempre que houver
        print('Lixo coletado.')


a = A()
print(len(a))
