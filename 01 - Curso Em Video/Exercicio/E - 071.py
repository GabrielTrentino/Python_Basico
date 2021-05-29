saque = int(input('Qual o valor que você deseja sacar? '))
while True:
    if saque // 50 > 0:
        print('Foi sacado {} notas de 50'.format(saque//50))
        saque = saque % 50
    if saque // 20 > 0:
        print('Foi sacado {} notas de 20'.format(saque//20))
        saque = saque % 20
    if saque // 10 > 0:
        print('Foi sacado {} notas de 10'.format(saque//10))
        saque = saque % 10
    if saque // 1 > 0:
        print('Foi sacado {} notas de 1'.format(saque//1))
        break
print('Obrigado! tenha um bom dia')