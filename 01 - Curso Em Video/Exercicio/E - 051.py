primeiro_termo = int(input('Qual o primeiro termo Dessa P.A? '))
razao = int(input('Qual a razão dessa P.A.? '))
for i in range (1,11):
    if i != 1:
        print(primeiro_termo + razao*i)
    else:
        print(primeiro_termo)
