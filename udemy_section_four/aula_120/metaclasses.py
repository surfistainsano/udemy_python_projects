# TUDO É OBJETO

# Maioria das linguagens: o type class é um "molde" que ensina a linguagem de programação a criar outros objetos

# class A:
#     def falar(self):
#         self.b_falar()
#
#
# class B(A):
#     pass
#     # def b_falar(self):
#     #     print('B falando.')


"""
com respeito à situação acima: 
Classe A -> back-end | Classe B -> front-end
Após a call abaixo, será levantada uma exceção na classe A pelo fato de não haver o atributo ->self.b_falar<-
É deduzido que o time back-end cometeu um erro, porém tal atributo/método é de responsabilidade do front-end, pois
o método deveria existir na classe B. É preciso resolver tal problema por forçar a criação do método na classe 
respectiva, para que não haja um "mal entendido".
"""


# b = B()
# b.falar()


# É possível resolver o problema acima com metaclasses.
# O método não será criado, mas será indicada a criação. Logo, será informado que, caso não seja criado tal membro, isso
# acarretará erro no programa.

class Meta(type):
    def __new__(mcs, name, bases, namespace):

        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)

        if 'b_falar' not in namespace:  # verificar se contém o nome da membro
            print(f'É preciso criar o método b_falar na classe {name}, para não haver erro.')
        else:
            if not callable(namespace['b_falar']):  # verifica se é uma function
                print(f'b_falar precisa ser um método em {name}')

        if 'attr_01' in namespace:  # para evitar a sobreposição de membros
            del namespace['attr_01']
        else:
            print('Lembrar de não declarar uma var com o nome attr_01.')

        return type.__new__(mcs, name, bases, namespace)


"""
def __new__(mcs, name, bases, namespace)
mcs é a classe em si
nome é o nome da classe a ser criada
bases é o nome da superclasse/classe pai das classes filhas
namespace é o nome dos métodos e propriedades das classes filhas (toda classe tem namespace)
é possível criar classes com o ->type<-
"""


class A(metaclass=Meta):
    attr_01 = 'Valor de A'

    def falar(self):
        self.b_falar()


class B(A):
    attr_01 = 'Valor de B'

    def b_falar(self):
        print('B falando.')


class C(B):
    attr_01 = 'Valor de C'


c = C()
print(c.attr_01)
# o código acima pode ser útil para aplicar DESIGN PATTERS, ou, quando se está trabalhando com equipes, pois está sendo
# "protocolado" o comportamento das classes que herdam a metaclasse.
# Nota-se que foi interceptado, no meio do processo de herança, o comportamento da classe filha.

# é possível criar classes com o método ->type<-
Arroz = type('Arroz', (), {'marca': 'Tio joão', 'tempo_de_cozimento': 30})
a = Arroz()
print(a.tempo_de_cozimento)  # // 30
print(type(a))  # // <class '__main__.Arroz'> | ou seja, é uma classe NORMAL
# ->type<- é uma metaclasse, pois isso é herdado dela para criar metaclasses
