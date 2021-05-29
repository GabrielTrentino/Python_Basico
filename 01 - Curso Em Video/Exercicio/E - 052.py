num = int(input('Digite o número para verificaçao: '))
for i in range (2, 1000):
    if i == num:
        continue
    if num % i == 0:
        print ("O número não é primo", i)
        break
    if i == 999:
        print("O número é primo")