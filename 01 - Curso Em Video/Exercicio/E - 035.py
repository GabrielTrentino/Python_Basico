r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))
maior = r3
lado1 = r1
lado2 = r2
if r1 > r2 and r1 > r3:
    maior = r1
    lado1 = r3
if r2 > r1 and r2 > r3:
    maior = r2
    lado2 = r3
if lado1+lado2 > maior:
    print('As três retas formam um triangulo')
else:
    print('As retas não formam um triangulo')