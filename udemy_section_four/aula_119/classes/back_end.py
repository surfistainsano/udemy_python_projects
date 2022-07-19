class Biblioteca:
    def biblioteca_method(self):
        print('Método da biblioteca')

    def call_method_from_interface(self):
        self.interface_method()  # é utilizada a INSTÂNCIA EM SI e não a classe pai.
