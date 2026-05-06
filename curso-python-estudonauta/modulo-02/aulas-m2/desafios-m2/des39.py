from datetime import date
atual = date.today().year
nasc = int(input('Ano de Nascimento: '))
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}!')
if idade == 18:
    print('Você tem que se alistar este ano!')
elif idade < 18:
    saldo1 = 18 - idade
    print(f'Ainda faltam {saldo1} anos para o alistamento!')
    ano = atual + saldo1
    print(f'Seu alistamento será em {ano}')
else:
    saldo2 = idade - 18
    print(f'Você já deveria ter se alistado há {saldo2} anos.')
    ano = atual - saldo2
    print(f'Seu ano de alistamento foi em {ano}')


