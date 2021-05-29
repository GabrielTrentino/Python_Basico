for i in range (1,6):
    peso = int(input('Digite o peso: '))
    if i != 1:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
    else:
        maior = peso
        menor = peso
print('O maior peso obtido foi: {}'.format(maior))
print('O Menor peso obtido foi: {}'.format(menor))