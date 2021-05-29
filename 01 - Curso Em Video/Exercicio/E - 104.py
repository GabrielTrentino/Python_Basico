def leiaInt(msg):
    while True:
        num = input(msg)
        if num.isnumeric():
            print(f'Você digitou {num}')
            return num
        else:
            print('\033[0;31mERRO! Digite um número valido\033[m')


n = leiaInt('Digite um numero: ')