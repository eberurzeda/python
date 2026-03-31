from random import randint
from time import sleep
computador = randint(0, 5,) # Faz o computador pensar num nº de 1 a 5
print('-=-' * 20)
print('Vou pensar num nº de 1 a 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que nº eu pensei? '))
print('Processando...')
sleep(2)
if jogador == computador:
    print('Parabéns, você conseguiu me vencer!')
else:
    print(f'Ganhei! Eu pensei no nº {computador} e não no {jogador}')



