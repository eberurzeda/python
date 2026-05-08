for n in range(2, 51, 2):
    print(n, end=' ')
print('Fim!')
# 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50 Fim!
#Forma que gasta menos processador, menos iterações.


#Forma mais que gasta mais:
# ..2 ..4 ..6 ..8 ..10 ..12 ..14 ..16 ..18 ..20 ..22 ..24 ..26 ..28 ..30 ..32 ..34 ..36 ..38 ..40 ..42 ..44 ..46 ..48 ..50 Fim!
for n in range(1, 51):
    print('.', end='')
    if n % 2 == 0:
      print(n, end=' ')
print('Fim!')   