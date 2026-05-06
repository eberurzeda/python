n1 = float(input('Digite o primeiro segmento: '))
n2 = float(input('Digite o segundo segmento: '))
n3 = float(input('Digite o terceiro segmento: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os segmentos acima podem formar um triângulo ', end='')
    if n1 == n2 == n3:
        print('Equilátero!')
    elif n1 != n2 != n3 != n1:
        print('Escaleno!')
    else:
        print('Isósceles!')
else:
    print('Os segmentos acima não podem formar um triãngulo!')
    