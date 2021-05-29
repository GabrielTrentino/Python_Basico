from random import randint
def maior(*valores):
    cont = maior = 0
    print('-=' * 20)
    print('Analisando os valores passados: ',end='')
    for i in valores:
        print(i,end=' ')
        if i > maior or cont == 0:
            maior = i
            cont += 1
    print()
    print(f'Foram passados {cont} valores ao todo. ')
    print(f'O maior valor passado foi: {maior}')


maior(-1,-2,-3,-4)
maior(4,7,0)
maior(1,2)
maior(6)
maior(0)