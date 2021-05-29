soma = 0
valor = 0
cont = -1
while valor != 999:
    soma += valor
    cont += 1
    valor = int(input('Digite o valor: [999 para parar] '))
print('A soma de {} termos é igual a {}'.format(cont,soma))