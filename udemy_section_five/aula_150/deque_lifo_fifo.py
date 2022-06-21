# LIFO e FIFO são estruturas de dados

"""
Pilha >>> stack >>> LIFO - last in, first out

Filas >>> queue >>> FIFO - first in, first out
"""

# Stack >>> O último item do arranjo é retirado, logo os itens anteriores não são afetados.
# Queue >>> O primeiro item a entrar é o primeiro item a sair, logo os itens ficam com índices diferentes.

# No caso da queue, pode-se surtir um efeito colateral grave, pois alterando o index dos itens, é mexido no endereço
# da memória do arranjo, ou seja, TUDO fica alterado. Seguindo a lógica da estrutura de dados FIFO os items andam uma
# casa (index) para trás.

# É possível resolver esse problema com python:

from collections import deque

# o módulo ->collections<- é muito útil ao lidar com uma grande quantia de dados

"""
fila = deque()  # É criado uma fila. É uma lista do tipo deque | // <class 'collections.deque'>

# Para adcionar itens:
fila.append('Leonardo')
fila.append('Leonardinger')
fila.append('Leonice')
fila.append('Lidiane')
fila.append('Leona')

# Para remover itens:
fila.popleft()  # rtype: valor removido | // Leonardo
fila.popleft()
fila.popleft()
fila.popleft()
fila.popleft()

print(fila)

# Acima, é chamado FIFO, pois o primeiro que entra é o primeiro que sai.
"""

"""
fila = deque(maxlen=5)  # Úma fila com o tamanho máximo de 5 itens
fila.extend([1, 2, 3, 4])
fila.append(5)
fila.append(6)
print(fila)  # // deque([2, 3, 4, 5, 6], maxlen=5) >>> First In, First Out
# De maneira automática, o valor mais ANTIGO foi retirado e o valor mais NOVO foi adicionado ao final da fila (e assim
# por diante).
"""

"""
from time import sleep

fila = deque(maxlen=10)

for i in range(1000):
    fila.append(i)
    sleep(1)
    print(fila)
"""

fila = deque(maxlen=10)

fila.extend([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # o método extend() suporta iteráveis
# fila.insert(2, 'Arroz')  # Caso os itens estiverem ocupando o tamanho máximo da fila, o método insert() levantará uma
# exceção | var.insert(index, value)

# var.append(item) É útil para adicionar um item
# var.extend([1, 2, 3]) É útil para adicionar vários itens
# var.index(index_desejado)  # retorna o valor contido no index
# var.index(index_desejado, start_index, end_index)  # É possível procurar o valor de um index dentro de um intervalo.

# fila.reverse()  // rtype: None | É invertida a fila.

# fila.rotate(1)  # // rtype: None | var.rotate(1) >>> o último item da fila é posto no primeiro lugar.
# print(fila)  # // deque([10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Ao passar um valor maior, o método cata os itens a partir do último item:
# fila.rotate(3)
# print(fila)  # // deque([8, 9, 10, 1, 2, 3, 4, 5, 6, 7], maxlen=10)

# Todos os exemplos mostram uma fila, porém uma fila de auto desempenho, para tratar uma grande quantia de dados.
