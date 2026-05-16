print('=' * 30)
print(f'{"Banco UdS":^30}')
print('=' * 30)

valor = int(input('Que valor você quer sacar? R$ '))

cedulas = (50, 20, 10, 1)
restante = valor

for cedula in cedulas:
    quantidade = restante // cedula
    restante = restante % cedula

    if quantidade > 0:
        print(f'Total de {quantidade} cédulas de R${cedula}')

print('Volte sempre ao Banco UdS! Tenha um bom dia!!!')


