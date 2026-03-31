velocidade = float(input('Qual a velocidade atual do carro: '))
if velocidade > 80:
    print('Multado! Você excedeu a velocidade máxima que é de 80Km/h')
    multa = (velocidade - 80) *7
    print(f'Você foi multado em R$ {multa:.2f}')
print('Tenha um bom dia! Dirija com segurança!')