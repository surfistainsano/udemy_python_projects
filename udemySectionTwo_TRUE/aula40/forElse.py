array = ['Leonardo', 'Maria', 'Laura', 'Luana']

for item in array:
    if item.lower().startswith('l'):
        print(f'{item} começa com "L"')
    else:
        print(f'{item} não começa com "L"')
