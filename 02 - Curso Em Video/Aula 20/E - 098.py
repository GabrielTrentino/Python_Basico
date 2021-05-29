from time import sleep
def contagem(inicial,final,passo):
    print('-='*20)
    print(f'Contagem de {inicial} até {final} com passos de {passo}:')
    if inicial < final:
        num = inicial
        while num <= final:
            print(num, end=' ')
            sleep(0.5)
            num += passo
    elif inicial > final:
        num = inicial
        while num >= final:
            print(num,end=' ')
            sleep(0.5)
            num -= passo
    print()

contagem(1,10,1)
contagem(10,0,2)
print('-='*20)
print('Agora é sua vez de personalizar a contagem: ')
inicio = int(input('Inicio: '))
final = int(input('Final: '))
passo = int(input('Passo: '))
contagem(inicio,final,passo)