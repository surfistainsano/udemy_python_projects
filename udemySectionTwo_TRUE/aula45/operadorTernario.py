# portaAberta = True
# msg = 'Podem entrar!' if portaAberta else 'Hooooooolllld!'
# print(msg)

# idade = input('Qual a sua idade? ')
#
# if not idade.isnumeric():
#     print('Você só pode digitar números.')
# else:
#     idade = int(idade)
#     isMajor = (idade >= 18)
#     msg = 'Pode tomar cerveja.' if isMajor else 'Sem gole pra você!'
#     print(msg)

# Aula46
# OR

# nome = input('Qual seu nome? ')
# print(nome or 'Você não digitou nada.')

a = 0
b = False
c = None
d = 1
e = 'Leo'
f = []

# CERTO
variavelBool = a or b or c or e or d or f
print(variavelBool)

# ERRADO
if a:
    variavelBool = a
elif b:
    variavelBool = b
elif c:
    variavelBool = c
