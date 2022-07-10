import os
from PIL import Image  # Essa classe possibilita a modificação da imagem (reduz em megabytes e em pixels)


def main(main_images_folder, new_width=800):
    if not os.path.isdir(main_images_folder):
        raise NotADirectoryError(f"O diretório localizado em {main_images_folder} não existe.")

    for root, dirs, files in os.walk(main_images_folder):
        for file in files:
            file_full_path = os.path.join(root, file)
            file_name, extension = os.path.splitext(file)  # rtype: tuple | Desempacota-se o nome_do_arquivo, extensao

            converted_tag = '_CONVERTED'

            new_file = f'{file_name}{converted_tag}{extension}'
            new_file_full_path = os.path.join(root, new_file)

            # if converted_tag in file_full_path:
            #     os.remove(file_full_path)
            #
            # continue

            if os.path.isfile(new_file_full_path):
                print(f'O arquivo {new_file_full_path} já existe.')
                continue

            if converted_tag in file_full_path:
                print('Imagem já convertida')
                continue

            # é importante notar que o interpretador do python "procura" a kw ->continue<- no código, ou seja, mesmo
            # havendo uma kw ->continue<- primeiro, a segunda kw não será ignorada. Logo, o interpretador "vendo" que é
            # a última kw ->continue<- no código, ele passa para a próxima iteração.

            img_pillow = Image.open(file_full_path)  # o arquivo é aberto pelo pillow

            """ Para consultar metadados do arquivo de imagem:
            # print(img_pillow._getexif())
            file_exif = img_pillow._getexif()  # rtype: dict
            data_m = file_exif.get(306)  # Acessa-se a chave e obtém-se o valor da metadado
            print(data_m)
            continue
            """

            width, height = img_pillow.size  # rtype: tuple | Desempacota-se a largura, altura

            """
            É possível calcular a proporção de uma imagem com base em 3 informações: largura original, altura original
            e NOVA largura. Logo, é possível fazer uma regra de 3:

            width         height
            new_width       X

            É possível concluir que o valor de X se dá pela expressão: new_width * height / width = X (new_height)
            """

            # Lembrando que a largura desejada está sendo passada por parâmetro:
            new_height = round(new_width * height / width)
            new_image = img_pillow.resize((new_width, new_height), Image.LANCZOS)  # Ler a documentação, para mais infos
            new_image.save(new_file_full_path, optimize=True, quality=70, exif=img_pillow.info['exif'])
            # Acima de 60, a qualidade já é boa
            # Foi passado o parâmetro nomeado ->exif<- para preservar os metadados do arquivo original, ou seja, ao
            # converter arquivos de imagem com pillow, o exif original é deletado.

            print(f'{file_full_path} foi convertido com sucesso.')

            new_image.close()  # Foi chamado o .close() para garantir o fechamento da new_img
            img_pillow.close()  # Aqui, garante-se que o arquivo (original) aberto será fechado.

            os.remove(file_full_path)  # CUIDADO! Remove os arquivos originais após a conversão.


if __name__ == '__main__':
    main_images_folder = r'C:\Users\arroz\Documents\aula_152_udemy_python_pillow_to_covert_images\images'
    main(main_images_folder, new_width=1920)
