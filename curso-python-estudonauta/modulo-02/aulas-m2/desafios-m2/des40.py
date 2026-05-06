
#nota_1 = float(input('Digite a primeira nota: '))
#nota_2 = float(input('Digite a segunda nota: '))
#media = (nota_1 + nota_2) / 2
#print(f'Tirando {nota_1} e {nota_2}, a média do aluno é {media}')
#if media >= 6:
#    print('Aluno Aprovado')
#elif media >= 4:
#   print('Aluno em Recuperação')
#else:
#    print('Aluno Reprovado')

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

print(f'\nNotas: {nota1:.1f} e {nota2:.1f}')
print(f'Média do aluno: {media:.1f}')

if media >= 6:
    print('Status: APROVADO')
elif media >= 4:
     print('Status: RECUPERAÇÃO')
else:
     print('Status: REPROVADO')