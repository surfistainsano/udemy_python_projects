# no windows, por conta das barras invertidas, coloca-se um r'string\string\string' para evitar erros de barra invertida

import os
import shutil

caminho_original = r'C:\udemyPythonProjects\media'
caminho_novo = r'C:\udemyPythonProjects\media2'

try:
    os.mkdir(caminho_novo)  # caso já exista 'media2', será levantada uma exceção. Logo, deve-se tratá-la.
except FileExistsError as e:
    print(f'Pasta {caminho_novo} já existe.')

for root, dirs, files in os.walk(caminho_novo):  # root é a raiz | dirs são os diretórios | files são arquivos
    for file in files:
        old_file_path = os.path.join(caminho_original, file)
        new_file_path = os.path.join(root, file)

        # shutil.move(old_file_path, new_file_path)  # shutil.move(caminho_antigo, caminho_novo) | Também renomeia.
        # if '.mp4' in file:
        #     shutil.copy(old_file_path, new_file_path)
        #     print(f'O arquivo {file} foi copiado com sucesso!')

        if '.mp4' in file:
            os.remove(new_file_path)
            print(f'Arquivo {file} apagado.')
