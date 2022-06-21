# Os sets suportam apenas tipos de dados IMUTÁVEIS
# sets não possuem PAR de chaves/valores
# é possível ITERAR sobre sets, porém não é possível acessar diretamente (brackets notation)
# para criar um set vazio, é preciso chamar o método set

voidSet = set()
voidSet.add('arroz')
s1 = {1,2,3,4,5}
s1.discard(5)
# s1.update('XYZ')  # a função update ITERA sobre cada item do valor passado (não respeita ordem)
s1.update({9,10,5}, [5,6,7], (13,14))  # usa-se sets para se lidar com arranjos

l2 = [1,1,1,2,2,3,4,5,6,6,6,6,'Leo', 'Leo', 'Laura']
s2 = set(l2)  # elementos duplicados são ignorados
tratedL2 = list(s2)

# print(tratedL2[-1])

s3 = {1, 2, 3, 4, 5, 7}
s4 = {1, 2, 3, 4, 5, 6}
# s5 = s3 | s4  # para duplicar, utiliza-se o pipe |
# s5 = s3 & s4  # para exibir os elementos presentes nos dois sets, utiliza-se o &
# s5 = s3 - s4  # são exibidos os elementos que constam somente no set da ESQUERDA (primeiro)
# s5 = s3 ^ s4  # são exibidos os elementos que estão nos dois sets, mas NÃO EM AMBOS

l3 = ['Leo', 'Nicole', 'Lidiane']
l4 = ['Leo', 'Nicole', 'Nicole', 'Nicole', 'Nicole', 'Nicole', 'Lidiane', 'Lidiane', 'Lidiane']

if set(l3) == set(l4):
    print('São iguais!')
else:
    print('São diferentes!')
