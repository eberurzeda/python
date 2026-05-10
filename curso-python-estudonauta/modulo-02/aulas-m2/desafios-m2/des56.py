somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = 0
for p in range(1, 5):
    print(f'---- {p}ª pessoa ----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1:
        

mediaidade = somaidade / 4
print(f'A mádia de idade do gropo é de {mediaidade} anos.')
