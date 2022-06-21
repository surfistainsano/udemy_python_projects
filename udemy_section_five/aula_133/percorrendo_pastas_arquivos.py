import os
from utils import formata_tamanho
caminho_procura = input('Digite um caminho: ')
termo_procura = input('Digite um termo: ')
conta = 0

for raiz, diretorios, arquivos in os.walk(caminho_procura):
    for arquivo in arquivos:
        if termo_procura in arquivo:
            try:
                conta += 1
                caminho_completo = os.path.join(raiz, arquivo)  # une a pasta raiz com o nome do arquivo. rtype: list
                nome_arquivo, nome_extensao = os.path.splitext(arquivo)  # rtype: tuple -> (file_name, file_extension)
                tamanho = os.path.getsize(caminho_completo)  # retorno em bytes
                print(arquivo)

                print()
                print('Encontrei o arquivo:', arquivo)
                print('Caminho:', caminho_completo)
                print('Nome:', nome_arquivo)
                print('Extensao:', nome_extensao)
                print('Tamanho:', tamanho)
                print('Tamanho formatado:', formata_tamanho(tamanho))
            except PermissionError as e:
                print('Sem permissão!')
            except FileNotFoundError as e:
                print('Arquivo não existe!')
            except Exception as e:
                print('Aconteceu algo inesperado. Erro:', e)

print()
print(f'{conta} arquivo(s) encontrado(s).')
