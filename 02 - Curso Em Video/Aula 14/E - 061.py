print('Gerador de PA')
print('-='*10)
termo1 = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
termos = 10
ant = termo1
while termos != 0:
    prox = ant + razao
    print('{} -> '.format(ant) if termos > 1 else '{} '.format(ant), end = '')
    ant = prox
    termos -= 1
    while termos == 0:
        termos = int(input('Digite a quantidade de termos que devem ser calculados: '))
        if termos == 0:
            break
