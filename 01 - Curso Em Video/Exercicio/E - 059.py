num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
while True:
    print ('-='*10, '''
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do Programa''')
    print('-='*10)
    opcao = int(input('>>>>> Qual a sua opção? '))
    if opcao == 1:
        print('A soma de {} com {} dá {}'.format(num1,num2,num1 + num2))
    elif opcao == 2:
        print('A multiplicação de {} com {} da {}'.format(num1,num2,num1*num2))
    elif opcao == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print('O Maior número é: {}'.format(maior))
    elif opcao == 4:
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
    elif opcao == 5:
        break
    else:
        print('Opção Invalida, tente novamente')
print('Programa encerrado')