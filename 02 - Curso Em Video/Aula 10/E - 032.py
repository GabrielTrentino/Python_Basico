ano = int(input('Digite o ano: '))
if ano % 4 == 0:
    print('{} é um ano Bissexto'.format(ano))
else:
    print('{} não é um ano Bissexto'.format(ano))