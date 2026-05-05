# Entrada de dados
valor_casa = float(input('Valor da casa: R$ '))
salario = float(input('Salário do comprador: R$ '))
anos = int(input('Em quantos anos vai pagar? '))

# Convertendo anos para meses
meses = anos * 12

# Calculando prestação mensal
prestacao = valor_casa / meses

# Calculando limite de 30% do salário
limite = salario * 0.30

# Verificação
if prestacao <= limite:
    print('Empréstimo APROVADO!')
else:
    print('Empréstimo NEGADO!')

# Mostrar informações
print(f'Prestação: R$ {prestacao:.2f}')
print(f'Limite permitido: R$ {limite:.2f}')