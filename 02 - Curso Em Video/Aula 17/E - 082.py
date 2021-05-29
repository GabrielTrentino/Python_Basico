lista = list()
pares = list()
impares = list()
while True:
    n = int(input('Digite um número para ser adicionado à lista: '))
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    r = str(input('Deseja continuar? [S/N] ')).strip()
    if r in 'Nn':
        break
lista.sort()
pares.sort()
impares.sort()
print('Você digitou: {}'.format(lista))
print('São Pares: {}'.format(pares))
print(f'São Impares: {impares}')