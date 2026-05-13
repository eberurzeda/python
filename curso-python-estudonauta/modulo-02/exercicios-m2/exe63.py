print('-' *30)
print('Sequência de Fibonacci')
num = int(input('Quantos termos você quer mostrar: '))
termo1 = 0
termo2 = 1
print('~' *30)
print(f'{termo1} → {termo2}', end='')
cont = 3 #contador
while cont <= num:
    termo3 = termo1 + termo2
    print(f' → {termo3}', end='')
    termo1 = termo2
    termo2 = termo3
    cont += 1
print(' → Fim!')
print('~' *30)

"""Esse código começa mostrando 0 e 1, que são os dois primeiros números da sequência de Fibonacci. Depois, dentro do while, ele soma sempre os dois últimos números para gerar o próximo. Após cada soma, ele atualiza os valores para continuar a sequência até chegar na quantidade de termos que o usuário pediu."""

