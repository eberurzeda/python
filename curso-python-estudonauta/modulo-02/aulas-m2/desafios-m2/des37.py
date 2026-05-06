numero = int(input('Digite um número: '))

print(
    '\n[1] Binário'
    '\n[2] Octal'
    '\n[3] Hexadecimal'
)

opcao = int(input('\nEscolha: '))

if opcao == 1:
    conversao = bin(numero)[2:]
    print(f'Binário: {conversao}')

elif opcao == 2:
    conversao = oct(numero)[2:]
    print(f'Octal: {conversao}')

elif opcao == 3:
    conversao = hex(numero)[2:]
    print(f'Hexadecimal: {conversao.upper()}')

else:
    print('Opção inválida. Tente novamente!')