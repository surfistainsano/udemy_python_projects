"""
class Arquivo:
    def __init__(self, arquivo, modo):  # o arquivo é aberto
        print('__init__')
        self.arquivo = open(arquivo, modo)

    def __enter__(self):  # aqui, o retorno vai para a variável apelidada ->arquivo<- | with ... as arquivo
        print('Entrou na classe')
        return self.arquivo

    def __exit__(self, exc_type, exc_val, exc_tb):  # o arquivo é fechado
        print('Saiu da classe')
        self.arquivo.close()


# acima, tem-se um protocolo de context manager | open -> return -> close

with Arquivo('arroz.txt', 'w') as arquivo:
    arquivo.write('Arroz sempre será bom.')


# é importante notar que o context manager serve para tudo que é necessário ABRIR E FECHAR ou CAPTURAR E SOLTAR,
# ou seja, não se limita a arquivos e.g. database and network connections, etc...

"""

# ################################################### # ##################################################

"""
class File:
    def __init__(self, arquivo, modo):
        print('__init__')
        self.arquivo = open(arquivo, modo)

    def __enter__(self):
        print('Entrou na classe')
        return self.arquivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Saiu da classe')
        self.arquivo.close()
        print(exc_type)  # Tipo da exceção // <class 'AttributeError'>
        print(exc_val)  # Valor da exceção // '_io.TextIOWrapper' object has no attribute 'metodo_inexistente'
        print(exc_tb)  # Traceback da exceção // <traceback object at 0x000001A39EC105C0>
        return True  # SOMENTE APÓS SER TRATADA A EXCEÇÃO. Logo, mesmo tendo exceção, não acarretará erro.


# caso seja levantada alguma exceção ao executar o context manager (dentro da tab do with), será possível tratá-la
# por meio dos parâmetros do magicmethod ->__exit__<-
# SOMENTE APÓS SER TRATADA, pode-se aplicar o return True ao final do magicmethod ->__exit__<-

with File('feijao.txt', 'w') as arquivo:
    arquivo.metodo_inexistente('arroz')  # return True ->__exit__<- | Logo, o dev assume que a exceção já foi tratada.
    arquivo.write('Feijão sempre será bom.')

"""

# ################################################### # ##################################################

# Para fazer um context manager como função

from contextlib import contextmanager


@contextmanager  # novamente, open -> return -> close
def abrir(arquivo, modo):
    try:
        arquivo = open(arquivo, modo)
        yield arquivo
    finally:
        arquivo.close()


with abrir('sonic.txt', 'w') as file:
    file.write('Você quis dizer: sonic.exe?')
