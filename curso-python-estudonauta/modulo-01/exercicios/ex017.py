'''co = float(input('Digite o valor do cateto opsto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print(f'O valor do cateto oposto é {co}, do cateto adjacente é {ca}, logo a hipotenusa é {hi:.2f}')'''
import math
co = float(input('Digite o valor do cateto opsto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hi = math.hypot(co, ca)
print(f'O cateto oposto é {co}, o cateto adjacente é {ca} e a hipotenusa é {hi:.2f}')
