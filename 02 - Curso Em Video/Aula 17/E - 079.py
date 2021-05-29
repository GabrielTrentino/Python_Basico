num = list()
while True:
    n = int(input('Digite um número: '))
    if n not in num:
        num.append(n)
        print('Valor Adicioando com sucesso')
    else:
        print('Valor Duplicado, não vou adicionar')
    r = str(input('Deseja continuar? [S/N] ')).strip()
    if r in "Nn":
        break
num.sort()
print('Você digitou os valores: {}'.format(num))