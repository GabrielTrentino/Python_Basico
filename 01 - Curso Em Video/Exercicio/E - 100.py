from random import randint
from time import sleep
def sorteia(lista):
        for cont in range (0,5):
            n = randint(1,10)
            lista.append(n)

def somapar(lista):
    s = 0
    print('Os números sorteados são: ', end='')
    sleep(0.3)
    for valor in lista:
        print(valor, end=' ')
        sleep(0.3)
        if valor % 2 == 0:
            s += valor
    print(f'\nE a soma dos pares são é: {s}')


numeros = list()
sorteia(numeros)
somapar(numeros)
