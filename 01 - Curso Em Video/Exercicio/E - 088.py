from random import randint

print('='*40)
print('{:^40}'.format('JOGO DA MEGA SENA'))
print('='*40)
quant = int(input('Digite a quantidade de jogos que você quer jogar: '))
for i in range(1,quant+1):
    print('Jogada {}: '.format(i),end = '')
    lista = list()
    while True:
        num = randint(1,60)
        if num in lista:
            continue
        else:
            lista.append(num)
        if len(lista) == 6:
            break
    lista.sort()
    print(lista)