from time import sleep
num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''    [1] Somar
    [2] multiplicar
    [3] Maior
    [4] Novos númeors
    [5] Sair do programa''')
    opção = int(input('Qual é sua opção? '))
    if opção == 1:
        soma = num1 + num2
        print(F'A soma entre {num1} e {num2} é {soma}')
    elif opção == 2:
        multi = num1 * num2
        print(f'A multiplicação entre {num1} e {num2} é {multi}')
    elif opção == 3:
        if num1 > num2:
            maior = num1
        else: maior = num2
        print(f'Entre {num1} e {num2} o maior valor é {maior}')
    elif opção == 4:
        print('Informe os números novamente: ')
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente!')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')
