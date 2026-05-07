print(f'{" Lojas Urzeda ":=^30}')

compras = float(input('Valor da compra R$: '))

print('1 - À vista dinheiro/PIX')
print('2 - À vista no cartão')
print('3 - 2x no cartão')
print('4 - 3x ou mais no cartão')

opcao = int(input('Escolha uma opção: '))

if opcao == 1:
    total = compras * 0.90
    print(f'\nValor a pagar: R$ {total:.2f}')

elif opcao == 2:
    total = compras * 0.95
    print(f'\nValor a pagar: R$ {total:.2f}')

elif opcao == 3:
    total = compras
    print(f'\nValor a pagar: R$ {total:.2f}')

elif opcao == 4:

    parcelas = int(input('Quantas parcelas? '))

    if parcelas <= 6:
        total = compras * 1.20

        print(f'\nValor total: R$ {total:.2f}')
        print(f'{parcelas}x de R$ {total / parcelas:.2f}')

    elif parcelas <= 12:
        total = compras * 1.30

        print(f'\nValor total: R$ {total:.2f}')
        print(f'{parcelas}x de R$ {total / parcelas:.2f}')

    else:
        print('Número de parcelas inválido. Escolha entre 1 e 12.')
    
else:
    print('\nOpção inválida! Digite um número entre 1 e 4.')
    