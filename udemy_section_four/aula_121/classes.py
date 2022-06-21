"""Descrição rápida e simples.


What is Lorem Ipsum?

Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's
standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a
type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting,
remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem
Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem
Ipsum.


What is Lorem Ipsum?

Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's
standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a
type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting,
remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem
Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem
Ipsum.
"""""


class A:
    """
    Classe A apresenta:
    """
    def __init__(self, texto):
        """Inicializador de membros

        :param texto: Texto de até 100 caracteres
        :type texto: str
        """
        self.texto = texto
        self.exibe_texto(texto)

    a = 1
    b = 2
    c = 3

    @staticmethod
    def exibe_texto(texto):

        """Método que exibe um texto de 100 caracteres na tela

        :param texto: Um texto de 100 caracteres
        :type texto: str

        :return: O texto com 100 caracteres
        :rtype: str

        :raises ValueError: Se o texto tiver mais de 100 caracteres
        :raises TypeError: Se o texto não for uma string
        """""
        if not isinstance(texto, str):
            raise TypeError("O texto precisa ser uma string.")

        if len(texto) > 100:
            raise ValueError("O texto deve ser de 100 caracteres ou menos.")

        return texto
