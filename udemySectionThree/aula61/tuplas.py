# não é possível "CRUD" em tuplas; somente listas

arroz = ('Tio joão', 3.99, 'Caldão', 6.77, 'Milano', 8.99) * 5  # pode-se obter uma tupla com ou sem ()
# sem a virgula o valor é respectivo, ou seja, colocando a croma ao final do valor único, tem-se uma tupla

# v1, v2, v3, *_, last = arroz  # desempacotamento

print(arroz)

# para alterar uma tupla, deve-se fazer cast
