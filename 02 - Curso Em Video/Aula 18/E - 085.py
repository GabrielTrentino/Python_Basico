num = [[],[]]
for i in range (1,8):
    n = int(input('Digite o {} valor: '.format(i)))
    if n % 2 == 0:
        num[0].append(n)
    else:
        num[1].append(n)
num[0].sort()
num[1].sort()
print(f'Lista de Pares {num[0]}')
print(f'Lista de Impares {num[1]}')