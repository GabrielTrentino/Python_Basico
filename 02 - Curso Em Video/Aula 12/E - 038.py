num1 = int(input('Digite o primeiro numero '))
num2 = int(input('Digite o segundo numero '))
if num1 > num2:
    print('O primeiro numero {} é maior que o segundo numero {}'.format(num1,num2))
elif num1 < num2:
    print('O primeiro numero {} é menor que o segundo numero {}'.format(num1,num2))
else:
    print('Os numeros digitados são iguais')