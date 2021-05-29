numeros = []
for i in range(5):
    numeros.append(int(input('Digite o {} termo: '.format(i))))
    if i > 0:
        if numeros[i] > maior:
            maior = numeros[i]
        if numeros[i] < menor:
            menor = numeros[i]
    else:
        maior = numeros[i]
        menor = numeros[i]
print('-='*15)
print('O Maior número: {} foi digitado na posição '.format(maior), end = '')
for i, v in enumerate(numeros):
    if v == maior:
        print(i, end = ' ')
print('\nO Menor número: {} foi digitado na posição '.format(menor), end = '')
for i, v in enumerate(numeros):
    if v == menor:
        print(i, end = ' ')