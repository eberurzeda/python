n1 = float(input('Digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))
m = (n1 + n2)/2
'''print(f'A sua média foi {m:.1f}')
if m >= 7.0:
    print('Sua média foi boa, Parabéns!')
else:
    print('Sua média foi ruim, estude mais!')'''
print(f'Sua média foi {m:.1f}')
print('Parabéns!' if m >= 7.0 else 'Estude mais!')


