# Estrutura condicional aninhada
nome = input('Qual é seu nome? ')

if nome == 'Eber':
    print(f'Que nome bonito, {nome}!')

elif nome in ['Marta', 'Maria', 'João', 'Pedro']:
    print(f'Seu nome é bem comum em Goiás, {nome}!')

elif nome in ['Carla', 'Cláudio', 'Enzo', 'Luciana', 'Patrícia']:
    print(f'Você tem o nome espanhol, "{nome}"')

else:
    print(f'Seu nome é bem comum no Brasil, {nome}!')

print(f'Tenha um bom dia, {nome}!')
print(f'Bom saber, "{nome}!"')