from random import randint
print('-='*15)
print('   VAMOS JOGAR PAR OU IMPAR')
print('-='*15)
valor = int(input('Diga um valor: '))
opcao = str(input('Par ou Impár? [P/I]' )).strip().upper()[0]
while True:
    computador = randint(1,10)
    print('Você jogou {} e o computador {}. Total de {}'.format(valor,computador, valor+computador))
    if opcao == 'I':
        if valor+computador % 2 == 1:
            print('Por você ter escolhido Impar, você ganhou!')
        else:
            print('Por você ter escolhido Impar, você perdeu!')
    elif opcao == 'P':
        if valor+computador % 2 == 1:
            print('Por você ter escolhido Par, você perdeu!')
        else:
            print('Por você ter escolhido Par, você ganhou!')
    flag = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if flag == 'N':
        break
    valor = int(input('Diga um valor: '))
    opcao = str(input('Par ou Impár? [P/I]')).strip().upper()[0]
print('Jogo Finalizado')