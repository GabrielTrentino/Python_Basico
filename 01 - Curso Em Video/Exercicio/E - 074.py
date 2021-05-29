from random import randint
print('Os números Sorteados foram: ',end = '')
numeros = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
for n in numeros:
    print(n, end = ' ')
print('\nO Maior número é: {}'.format(max(numeros)))
print('O Menor número é: {}'.format(min(numeros)))
