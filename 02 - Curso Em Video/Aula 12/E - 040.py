n1 = float(input('Qual a n1? '))
n2 = float(input('Qual a n2? '))
media = (n1+n2)/2
if media < 5:
    print('Reprovado')
elif media >= 7:
    print('Aprovado')
else:
    print('Recuperação né Filhao')