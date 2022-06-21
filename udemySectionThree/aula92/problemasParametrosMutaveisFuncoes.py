def listaDeClientes(clientesArray, lista=None):  # Por conta do parâmetro ser imutável, o método não "mescla" as arrays
    if lista is None:
        lista = []
    lista.extend(clientesArray)
    return lista


otherClientes = ['Luana']
clientes1 = listaDeClientes(['Leonardo', 'Nicole', 'Lidiane'], otherClientes)
clientes2 = listaDeClientes(['Eduarda', 'Vera', 'Mauro'])
clientes3 = listaDeClientes(['Cássio', 'Lilian'])

print(clientes1)
print(clientes2)
print(clientes3)

# não se deve utilizar parâmetro padrão com tipo MUTÁVEL!
# a sulução está no code acima
