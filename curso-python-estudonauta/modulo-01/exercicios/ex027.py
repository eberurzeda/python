'''n = (input('Digite seu nome completo: ')).strip().split()
print(f'Muito prazer, {n[0]}!')
print(f'Seu primeiro nome é {n[0]}!')
print(f'Seu último nome é {n[-1]}!')'''
nome = input('Digite seu nome completo: ').strip().split()

if nome:
    print(f'Muito prazer, {nome[0]}!')
    print(f'Seu primeiro nome é {nome[0]}!')
    print(f'Seu último nome é {nome[-1]}!')
else:
    print('Você não digitou um nome válido.')

