'''nome = str(input('Qual é seu nome completo? ')).strip()
print('Seu nome tem Silva?', 'Silva' in nome)'''
import unicodedata

nome = input('Qual é seu nome completo? ')

# 1️⃣ remover espaços e colocar minúsculo
nome = nome.strip().lower()

# 2️⃣ remover acentos
nome = unicodedata.normalize('NFD', nome)
nome = ''.join(c for c in nome if unicodedata.category(c) != 'Mn')

# 3️⃣ separar palavras
partes = nome.split()

print('Seu nome tem Silva?', 'silva' in partes)















