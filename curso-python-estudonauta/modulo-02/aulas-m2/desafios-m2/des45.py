from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')

computador = randint(0, 2)

print('''Suas opções:
0 - Pedra
1 - Papel
2 - Tesoura''')

jogador = int(input('Qual é a sua jogada? '))
print('JO...')
sleep(1)
print('Ken...')
sleep(1)
print('Po!!!')

print('-=' * 11)

if jogador < 0 or jogador > 2:
    print('Jogada inválida. Escolha um número de 0 a 2')

else:
    print(f'Computador jogou {itens[computador]}')
    print(f'Jogador jogou {itens[jogador]}')

    print('-=' * 11)
    if computador == 0: #computador jogou pedra
        if jogador == 0:
            print('Empate!')
        elif jogador == 1:
            print('Jogador Vence!')
        elif jogador == 2:
            print('Computador Vence!')
        else:
            print('Jogada inválida!')

    elif computador == 1: # computador jogou Papel
        if jogador == 0:
            print('Computador Vence!')
        elif jogador == 1:
            print('Empate!')
        elif jogador == 2:
            print('Jogador Vence!')
        else:
            print('Jogada inválida!')

    elif computador == 2: # computador jogou tesoura
        if jogador == 0:
            print('Jogador Vence!')
        elif jogador == 1:
            print('Computador Vence!')
        elif jogador == 2:
            print('Empate!')
        else:
            print('Jogada inválida!')

        