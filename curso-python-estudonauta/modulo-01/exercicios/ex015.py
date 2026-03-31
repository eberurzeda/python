km = float(input('Quantos quilômetros o carro percorreu?: '))
Dias = int(input('Quantos dias o carro foi alugado?: '))
custo = (km * 0.15) + (Dias * 60)
print(f'O custo do carro foi de R$ {custo: .2f}')

