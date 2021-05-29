resp = 'S'
soma = cont = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    cont += 1
    if cont != 1:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    else:
        maior = menor = num
    resp = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
media = soma/cont
print('Você digitou {} termos, a média é {:.2f}'.format(cont,media))
print('O Maior valor foi {} e o menor foi {}'.format(maior,menor))