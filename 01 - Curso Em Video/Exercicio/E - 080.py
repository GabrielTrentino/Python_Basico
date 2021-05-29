lista = list()
for i in range(0,5):
    n = int(input('Digite o número: '))
    if i == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionada no Final da Lista')
    else:
        pos = 0
        while True:
            if n <= lista[pos]:
                lista.insert(pos, n)
                print('Adicionada na Posição {} da Lista'.format(pos))
                break
            pos += 1
print('Os números Digitados foram: {}'.format(lista))