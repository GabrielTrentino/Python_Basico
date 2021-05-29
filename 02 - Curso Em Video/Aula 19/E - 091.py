from random import randint
from time import sleep
from operator import itemgetter

jogada = {'jogador 1': randint(1,6),
          'jogador 2': randint(1,6),
          'jogador 3': randint(1,6),
          'jogador 4': randint(1,6)}
print('Valores Sorteados: ')
for i,a in jogada.items():
    print('O {} jogou {}'.format(i,a))
    sleep(1)
rank = sorted(jogada.items(), key=itemgetter(1))
rank.reverse()
print('-'*40)
print(f'{"RANKING":^40}')
for i,a in rank:
    print(i)
