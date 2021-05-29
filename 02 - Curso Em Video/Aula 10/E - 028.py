import random
numero = random.randint(1,5)
chute = int(input('Digite o seu chute: '))
if chute == numero:
    print('Parabens, você acertou o número {}'.format(chute))
else:
    print('Você errou! O número era {} e você chutou {}'.format(numero,chute))
