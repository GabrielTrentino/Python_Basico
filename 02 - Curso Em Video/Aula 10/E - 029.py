velo = int(input('Qual a velocidade do carro?'))
if velo > 80:
    print('Você foi multado por R${:.2f}'.format((velo-80)*7))
else:
    print('Você nao foi multado dessa vez')
