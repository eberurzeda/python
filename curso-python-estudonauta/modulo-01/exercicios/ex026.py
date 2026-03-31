frase = str(input('Digite uma frase: ')).upper().strip()
print(f'A letra "A" aparece {frase.count("A")} vezes na farse!')
print(f'A primeira letra "A" apareceu na posição {frase.find("A")+1}')
print(f'A última letra "A" aparece na posicão {frase.rfind("A")+1}')
