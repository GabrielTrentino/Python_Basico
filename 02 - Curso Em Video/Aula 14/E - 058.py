from random import randint
computador = randint(1,10)
print('Vamos começar o jogo da Advinhação.')
contador = 0
while True:
    chute = 0
    while chute < 1 or chute > 10:
        chute = int(input('Digite um valor:'))
        if chute < 1 or chute > 10:
            print('Digite novamente, valor inserido não valido')
    contador += 1
    if chute == computador:
        break
    print('Não Foi esse valor, tente novamente')
print('Parabens! Após {} tentativas, você acecrtou!'.format(contador))