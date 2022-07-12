class LogMixin:
    @staticmethod
    def write(msg):
        with open('log.txt', 'a+') as f:  # with open('file_name.extension', 'a+') a+ quer dizer que adicionará sempre
            # ao final da linha do arquivo. Como a kw with é um gerenciador de contexto, ele fechará o file sozinho.
            f.write(msg)
            f.write('\n')

    def log_info(self, msg):
        self.write(f'INFO: {msg}')

    def log_error(self, msg):
        self.write(f'ERROR: {msg}')

# foi chegada a conclusão de que não foi preciso usar o parâmetro self no método. Isso indica que ele pode se tornar
# estático, pois independe do objeto instanciado.

# nota-se que a classe LogMixin não tem relação alguma com as classes Smartphone e Eletronico, porém, para que seja
# adicionada a funcionalidade de gerar log's em ambas as classes, é utilizado o Mixin. Nesse caso, cabe o conceito de
# herança múltipla, pois a classe LogMixin serve apenas para adicionar uma funcionalidade a outra classe.
