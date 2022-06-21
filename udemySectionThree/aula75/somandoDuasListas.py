
# my solution

# listaA = [1, 2, 3, 4, 5, 6, 7, 8]
#
# listaB = [1, 2, 3, 4, 5, 6]
#
# zipLists = list(zip(listaA, listaB))
#
# compList = [x + y for x, y in zipLists]
#
# print(compList)

# solução "global"

# listaA = [1, 2, 3, 4, 5, 6, 7, 8]
# listaB = [1, 2, 3, 4, 5, 6]
# somaLista = []
#
# for i in range(len(listaB)):
#     somaLista.append(listaA[i] + listaB[i])
# print(somaLista)

# python solution

listaA = [1, 2, 3, 4, 5, 6, 7, 8]
listaB = [1, 2, 3, 4, 5, 6]

somaLista = [x + y for x, y in zip(listaA, listaB)]

print(somaLista)
