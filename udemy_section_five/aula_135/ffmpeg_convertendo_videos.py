"""
ffmpeg -i "ENTRADA" -i "LEGENDA" -c:v libx264 -crf 23 -preset ultrafast -c:a aac -b:a 320k
-c:s srt -map v:0 -map a -map 1:0 -ss 00:00:00 -to 00:00:10 "SAIDA"
"""

# vale notar que isso não é um programa e sim um script, pois será usado apenas para seu fim: coverter vídeos.

import os
import fnmatch
import sys

comando_ffmpeg = r'C:\udemyPythonProjects\udemy_section_five\aula_135\ffmpeg\ffmpeg.exe'

codec_video = '-c:v libx264'
crf = '-crf 23'  # entre 15 e 28 considera-se boa qualidade. 18 é a melhor; 28 é a pior.
preset = '-preset ultrafast'
codec_audio = '-c:a aac'
bitrate_audio = '-b:a 320k'
debug = '-ss 00:00:00 -to 00:00:10'

caminho_origem = r'C:\udemyPythonProjects\media'
caminho_destino = r'C:\udemyPythonProjects\media2'

for root, dirs, files in os.walk(caminho_origem):
    for file in files:
        if not fnmatch.fnmatch(file, '*.mp4'):
            continue

        caminho_completo = os.path.join(root, file)
        file_name, file_extension = os.path.splitext(caminho_completo)  # obtém-se o file's path sem a extensão
        caminho_legenda = file_name + '.srt'

        if os.path.isfile(caminho_legenda):  # para verificar se contém arquivo .srt
            input_legenda = f'-i "{caminho_legenda}"'
            map_legenda = '-c:s srt -map v:0 -map a -map 1:0'  # é mapeado o vídeo, áudio e legenda
        else:  # caso a legenda não existir
            input_legenda = ''
            map_legenda = ''

        nome_arquivo, extensao_arquivo = os.path.splitext(file)

        arquivo_saida = f'{caminho_destino}\\{nome_arquivo}_novo.mkv'

        # para salvar no mesmo diretório:
        # new_name_file = nome_arquivo + '_novo' + extensao_arquivo
        # arquivo_saida = os.path.join(root, new_name_file)

        comando = f'{comando_ffmpeg} -i "{caminho_completo}" {input_legenda} ' \
                  f'{codec_video} {crf} {preset} {codec_audio} {bitrate_audio} ' \
                  f'{debug} {map_legenda} "{arquivo_saida}"'

        os.system(comando)
