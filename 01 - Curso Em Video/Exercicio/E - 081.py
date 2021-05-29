lista = list()
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    r = str(input('Deseja continuar? [S/N] ')).strip()
    if r in 'Nn':
        break
lista.sort()
lista.reverse()
print('Foram Digitados {} termos'.format(len(lista)))
print('A lista em Ordem Decrescente: {}'.format(lista))
if 5 in lista:
    print('O número 5 foi digitado')
else:
    print('O número 5 não foi digitado')
