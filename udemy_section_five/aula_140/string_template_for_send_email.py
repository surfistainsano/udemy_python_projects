from string import Template
from datetime import datetime
from locale import LC_ALL, setlocale

setlocale(LC_ALL, 'pt_BR.utf-8')

data_atual = datetime.now().strftime('%A, %d de %B de %Y %H:%M:%S')

with open('template.html', 'r') as html:
    template = Template(html.read())
    corpo_msg = template.substitute(nome='Marilene', data=data_atual)  # rtype: str

"""
Caso não haja certeza de que todos os placeholders do html tenham sido passados como parâmetros,
pode-se utilizar o método .safe_substitute. Logo, não será levantada nenhuma exceção, porém será exibida
a variável do html e.g. $variavel
"""
print(corpo_msg)
