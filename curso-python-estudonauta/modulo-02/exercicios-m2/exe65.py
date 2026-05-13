resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    
    resp = str(input('Quer continuar? [S/N] ')).upper().strip() [0]
media = soma / quant   
print(f'Você digitou {quant} números e a média foi {media:.2f}!')
print(f'(O maior valor foi {maior} e o menor foi {menor})')

"""Esse código começa com a resposta S para entrar no while. Enquanto o usuário quiser continuar, ele digita um número. O programa soma esse número, conta mais um na quantidade, verifica se ele é o maior ou o menor até aquele momento e pergunta se a pessoa quer continuar. Quando o usuário responde N, o laço para, a média é calculada dividindo a soma pela quantidade de números, e o programa mostra a quantidade, a média, o maior e o menor valor digitado."""
