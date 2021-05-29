print('-='*15)
print('Sequência de Fibonacci')
print('-='*15)
termos = int(input('Quantos termos você deseja imprimir?'))
n = 3
t1 = 0
t2 = 1
t3 = 0
print('{} -> {}'.format(t1,t2), end = '')
while n <= termos:
    t3 = t1 + t2
    print('-> ', t3, end = ' ')

    t1 = t2
    t2 = t3
    n +=1