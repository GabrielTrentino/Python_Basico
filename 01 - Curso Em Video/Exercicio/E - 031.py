dist = float(input('Digite a distância da viagem: '))
if dist > 200:
    preco = 0.45*dist
else:
    preco = 0.50*dist
print('O preço da passagem é de R${:.2f}'.format(preco))