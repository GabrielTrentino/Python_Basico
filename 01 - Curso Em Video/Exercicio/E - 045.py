from random import randint
opcao = ['Pedra','Papel','Tesoura']
computador = randint(0,2)
print('=-='*10)
print('''Escolha sua opção:
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura
''')
jogador = int(input('Digite o número da sua opcao: '))-1
if computador == 0: #PC joga pedra
    if jogador == 0:
        print("EMPATE, você jogou {} e o computador jogou {}".format(opcao[jogador],opcao[computador]))
    elif jogador == 1:
        print("GANHOU, você jogou {} e o computador jogou {}".format(opcao[jogador],opcao[computador]))
    elif jogador == 2:
        print("PERDEU, você jogou {} e o computador jogou {}".format(opcao[jogador],opcao[computador]))
elif computador == 1: #PC joga Papel
    if jogador == 0:
        print("PERDEU, você jogou {} e o computador jogou {}".format(opcao[jogador],opcao[computador]))
    elif jogador == 1:
        print("EMPATE, você jogou {} e o computador jogou {}".format(opcao[jogador],opcao[computador]))
    elif jogador == 2:
        print("GANHOU, você jogou {} e o computador jogou {}".format(opcao[jogador],opcao[computador]))
elif computador == 2:
    if jogador == 0:
        print("GANHOU, você jogou {} e o computador jogou {}".format(opcao[jogador],opcao[computador]))
    elif jogador == 1:
        print("PERDEU, você jogou {} e o computador jogou {}".format(opcao[jogador],opcao[computador]))
    elif jogador == 2:
        print("EMPATE, você jogou {} e o computador jogou {}".format(opcao[jogador],opcao[computador]))