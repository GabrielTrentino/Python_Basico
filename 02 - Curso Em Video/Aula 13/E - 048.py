soma = 0
qnt = 0
for num in range (1,500,1):
    if num % 2 == 1 and num % 3 == 0:
        soma += num
        qnt += 1
print('Há {} e a soma deles é {}'.format(qnt,soma))