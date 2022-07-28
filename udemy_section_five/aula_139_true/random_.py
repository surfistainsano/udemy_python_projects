import random, string

inteiro = random.randint(10, 20)
flutuante = random.uniform(10, 20)
like_ecs6 = random.random()  # // 0.8785945596858687

# Gerar um número aleatório usando range()
random_range = random.randrange(90, 100, 2)  # range(start, stop, step)

# O módulo random pode ser útil para lidar com iteráveis
lista = ['Leo', 'Lidi', 'Lili', 'Nic', 'Day', 'Joelson', 'Lindomar']
sorteio = random.choice(lista)  # retorna um valor aleatório da array

sorteio_multi = random.choices(lista, k=3)  # retorna múltiplos itens, porém repete os termos

sorteio_multi_once = random.sample(lista, k=3)
# print(sorteio_multi_once)  # retorna múltiplos itens, porém NÃO repete os termos

# Para embaralhar a list original
print(lista)
random.shuffle(lista)
print(lista)

# Gerar senha aleatória
letras = string.ascii_letters
digitos = string.digits
caracteres = '!@#$%&*_-'
geral = letras + digitos + caracteres

senha = ''.join(random.choices(geral, k=10))
print(senha)
