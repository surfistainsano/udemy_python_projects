from udemy_section_four.aula_109.composicao import Cliente

cliente1 = Cliente('Leonardo', 23)
cliente1.inserir_enderecos('Balneário Gaivota', 'SC')

cliente2 = Cliente('Luiz', 32)
cliente2.inserir_enderecos('Rio de Janeiro', 'RJ')
cliente2.inserir_enderecos('Bombinhas', 'SC')

cliente3 = Cliente('Livia', 26)
cliente3.inserir_enderecos('Guarulhos', 'SP')

cliente2.listar_enderecos()



