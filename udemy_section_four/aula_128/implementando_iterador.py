class MinhaLista:
    def __init__(self):
        self.__items = []
        self.__index = 0

    def add(self, valor):
        self.__items.append(valor)

    def __getitem__(self, index):  # permite o acesso por brackets notation
        return self.__items[index]

    def __setitem__(self, index, value):
        if index >= len(self.__items):
            self.__items.append(value)
            return
        self.__items[index] = value

    def __delitem__(self, index):
        del self.__items[index]

    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = self.__items[self.__index]
            self.__index += 1
            return item
        except IndexError:
            raise StopIteration

    def __str__(self):
        return f'{self.__class__.__name__}({self.__items})'

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    lista = MinhaLista()
    lista.add('Leonardinger')
    lista.add('Arroz')
    lista.add('Feijão')

    # lista = list(lista)  # tornando-se um iterável, extingue-se o conceito dos dados serem consumidos; não é um iter
    #
    # for value in lista:
    #     print(value)
    #
    # for value in lista:
    #     print(value)
    #
    # for value in lista:
    #     print(value)

    print(lista)
