def leiaInt(msg):
    while True:
        try:
            num = int(input(msg).replace(',','.').strip())
        except(ValueError, TypeError, Exception) as erro:
            print('\033[0;31mERRO! Digite um número inteiro valido\033[m')
            print(f'Você digitou um erro: {erro.__class__}')
        else:
            return num


def leiaFloat(msg):
    while True:
        try:
            num = float(input(msg).replace(',','.').strip())
        except(ValueError, TypeError, Exception) as erro:
            print('\033[31mDigite um número Flutuante certo!\033[m')
            print(f'Você digitou e causou um erro do tipo: {erro.__class__}')
        else:
            return num


nint = leiaInt('Digite um numero Inteiro: ')
nfloat = leiaFloat('Digite um número Flutuante: ')
print(f'Você digitou um número Inteiro: {nint}\nE um número Flutuante: {nfloat}')