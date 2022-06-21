import re
from itertools import count

# o code deve ser quebrado em functions

cnpj_original = input('Digite um CPNJ para validação: ')
contador_index_3 = count(5, -1)
contador_index_4 = count(6, -1)
contador_index_16 = count(9, -1)
contador_index_17 = count(9, -1)


def remover_caracteres(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)


def fatiar_cnpj(cnpj):
    return cnpj[:12]


cnpj_informado = remover_caracteres(cnpj_original)
cnpj_fatiado = fatiar_cnpj(cnpj_informado)


def calcula_until_index_3(cnpj_fatiado_parameter):
    for e, n in enumerate(cnpj_fatiado_parameter):
        if e == 3:
            zip_first_part = zip(contador_index_3, cnpj_fatiado_parameter[:4])
            comp_first_part = sum([(x * int(y)) for x, y in zip_first_part])
            return comp_first_part


def calcula_until_index_16(cnpj_fatiado_parameter):
    for e, n in enumerate(cnpj_fatiado_parameter):
        if e > 3:
            zip_second_part = zip(contador_index_16, cnpj_fatiado_parameter[4:16])
            comp_second_part = sum([(x * int(y)) for x, y in zip_second_part])
            return comp_second_part


total_to_first_digit = calcula_until_index_3(cnpj_fatiado) + calcula_until_index_16(cnpj_fatiado)
total_formula_first_digit = 11 - (total_to_first_digit % 11)


def validar_first_digit(total_formula_first_digit, cnpj_fatiado):
    if total_formula_first_digit > 9:
        return cnpj_fatiado + '0'
    else:
        return cnpj_fatiado + str(total_formula_first_digit)


cnpj_with_first_digit = validar_first_digit(total_formula_first_digit, cnpj_fatiado)


def calcula_until_index_4(cnpj_fatiado_parameter):
    for e, n in enumerate(cnpj_fatiado_parameter):
        if e == 4:
            zip_first_part = zip(contador_index_4, cnpj_fatiado_parameter[:5])
            comp_first_part = sum([(x * int(y)) for x, y in zip_first_part])
            return comp_first_part


def calcula_until_index_17(cnpj_fatiado_parameter):
    for e, n in enumerate(cnpj_fatiado_parameter):
        if e > 4:
            zip_second_part = zip(contador_index_17, cnpj_fatiado_parameter[5:17])
            comp_second_part = sum([(x * int(y)) for x, y in zip_second_part])
            return comp_second_part


total_to_second_digit = calcula_until_index_4(cnpj_with_first_digit) + calcula_until_index_17(cnpj_with_first_digit)
total_formula_second_digit = 11 - (total_to_second_digit % 11)


def validar_second_digit(total_formula_second_digit, cnpj_with_first_digit):
    if total_formula_second_digit > 9:
        return cnpj_with_first_digit + '0'
    else:
        return cnpj_with_first_digit + str(total_formula_second_digit)


cnpj_with_second_digit = validar_second_digit(total_formula_second_digit, cnpj_with_first_digit)
cnpj_novo = cnpj_with_second_digit

if cnpj_informado == cnpj_novo:
    print(f'O CNPJ: {cnpj_novo} é verdadeiro!')
else:
    print(f'O CNPJ {cnpj_informado} é falso!', {cnpj_novo})
