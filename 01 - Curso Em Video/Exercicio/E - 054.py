maioridade = 0
menoridade = 0
for i in range (1,8):
    idade = int(input('Digite a idade: '))
    if idade >= 18:
        maioridade += 1
    else:
        menoridade += 1
print('{} Chegaram a maioridade, enquanto que {} estão na menoridade'.format(maioridade,menoridade))