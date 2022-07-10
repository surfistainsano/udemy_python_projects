array = ['Leonardo', 'Maria', 'João', 'Laura', 55, 56, 57, 'arroz']

first_value, *_ = array  # o sinal '*' seguido de uma variável armazena o restante dos valores em uma array
# a variável '_' indica para um futuro dev que não se irá utiilizar o "resto da lista"

print(first_value, _)
