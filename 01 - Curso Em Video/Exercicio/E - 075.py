numeros = (int(input('Digite um número: ')),
           int(input('Digite mais um número: ')),
           int(input('Digite um outro número: ')),
           int(input('Digite o Ultimo número: ')))
print('Você digitou os números: {}'.format(numeros))
print('O número nove (9) apareceu: {} vezes'.format(numeros.count(9)))
print('O número três (3) apareceu na posição: {}'.format(numeros.index(3)+1))
print('Os números pares foram: ', end = '')
for i in numeros:
    if i % 2 == 0:
        print(i,end = ' ')
