total = cont = totmil = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: ')).strip()
    preco = float(input('Preço do Produto: '))
    resp = ' '
    cont += 1
    total += preco
    if preco >= 1000:
        totmil += 1
    if cont == 1:
        menorprod = produto
        menorpreco = preco
    else:
        if preco < menorpreco:
            menorprod = produto
            menorpreco = preco
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('A) O total gasto na compra é: R${:.2f}'.format(total))
print('B) {} produtos custam mais que R$ 1000'.format(totmil))
print('C) O Produto {} possui menor preço'.format(menorprod))
print('{:-^40}'.format('FIM DO PROGRAMA'))