numero = int(input('Digite um número inteiro: '))

print('''
Escolha uma das bases para conversão:

[1] Binário
[2] Octal
[3] Hexadecimal
''')

opcao = int(input('Sua opção: '))

if opcao == 1:
    print(f'{numero} em binário é {bin(numero)[2:]}')

elif opcao == 2:
    print(f'{numero} em octal é {oct(numero)[2:]}')

elif opcao == 3:
    print(f'{numero} em hexadecimal é {hex(numero)[2:]}')

else:
    print('Opção inválida. Tente novamente!')