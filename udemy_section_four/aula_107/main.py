from udemy_section_four.aula_107.associação import Escritor, Caneta, MaquinaDeEscrever

escritor = Escritor('Leonardo')
caneta = Caneta('Acerola')
maquina_de_escrever = MaquinaDeEscrever()
# acima, os objetos são independetes
escritor.ferramenta = caneta
escritor.ferramenta.escrever()
# acima, há um exemplo de associação
