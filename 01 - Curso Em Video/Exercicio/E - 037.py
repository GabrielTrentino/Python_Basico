num = int(input('Digite o numero para ser convertido: '))
print('-='*10)
print('''Qual base de conversão?
[ 1 ] Binário
[ 2 ] Octal
[ 3 ] hexadecimal
''')
print('-='*10)
opcao = int(input('Digite sua opcao: '))
if opcao == 1:
    print('O número {} foi convertido para {}'.format(num,bin(num)))
elif opcao == 2:
    print('O número {} foi convertido para {}'.format(num,oct(num)))
elif opcao == 3:
    print('O número {} foi convertido para {}'.format(num,oct(num)))
else:
    print('Opção invalida')