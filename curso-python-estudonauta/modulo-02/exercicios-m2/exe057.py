sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()
while sexo == '' or sexo[0] not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()
print(f'Sexo {sexo} resgistrado com sucesso!')

"""sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper() [0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper() [0]
print(f'Sexo {sexo} resgistrado com sucesso!')"""

