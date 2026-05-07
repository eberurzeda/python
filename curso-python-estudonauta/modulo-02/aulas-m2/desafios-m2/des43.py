peso = float(input('Digite seu peso: (kg) '))
altura = float(input('Digite sua altura: (M) '))
imc = peso / (altura ** 2)
print(f'\nSeu IMC é {imc:.1f}')
if imc < 18.5:
    print('Status: Abaixo do Peso!')
elif imc < 25:
    print('Status: Peso Ideal!')
elif imc < 30:
    print('Status: Sobrepeso!')
elif imc < 40:
    print('Status: Obesidade!')
else:
    print('Status: Obesidade Mórbida!')