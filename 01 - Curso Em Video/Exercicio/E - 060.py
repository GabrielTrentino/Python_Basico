numero = int(input('Digite o número para calcular sua fatorial: '))
fatorial = 1
c = numero
print('Calculando Fatorial de {}!'.format(numero))
print('Calculando {}! = '.format(numero), end = '')
while c > 0:
    fatorial *= c
    print('{}'.format(c), end = '')
    print(' x ' if c > 1 else ' = ', end = '')
    c-=1
print('{}'.format(fatorial))
