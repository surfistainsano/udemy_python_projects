print('Texto explicativo.')
perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2? ',
        'respostas': {'a': '1', 'b': '4', 'c': '5'},
        'respostaCerta': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3*3? ',
        'respostas': {'a': '1', 'b': '4', 'c': '9'},
        'respostaCerta': 'c',
    },
    'Pergunta 3': {
        'pergunta': 'Quanto é 1/3? ',
        'respostas': {'a': '0.33', 'b': '4', 'c': '5'},
        'respostaCerta': 'a',
    }
}
respostasCertas = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('Respostas: ')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    respostaUsuario = input('Sua resposta: ')

    if respostaUsuario == pv['respostaCerta']:
        print('You did it!')
        respostasCertas += 1
    else:
        print('Errrrrrrrrroooooooooouuuuuuuuuu')
qtdPerguntas = len(perguntas)
porcentagemAcerto = respostasCertas / qtdPerguntas * 100
print(f'Você acertou: {porcentagemAcerto}%', f'Acertos: {respostasCertas}')
