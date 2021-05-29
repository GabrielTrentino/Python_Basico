cont = maior = menor = 0
while True:
    nome = str(input('Digite o nome: ')).strip()
    peso = float(input('Digite o peso: '))
    cont+=1

    if peso > maior or cont == 1:
        maior = peso
        maiorpeso = list()
        maiorpeso.append(nome)
    elif peso == maior:
        maiorpeso.append(nome)
    if peso < menor or cont == 1:
        menor = peso
        menorpeso = list()
        menorpeso.append(nome)
    elif peso == menor:
        menorpeso.append(nome)

    r = str(input('Deseja continuar? [S/N] ')).strip()
    if r in "Nn":
        break
print('Foram Cadastradas {} pessoas'.format(cont))
print('Maior Pesos: {}. Pessoas: '.format(maior), end = '')
for p in maiorpeso:
    print(p, end = ' ')
print('\nMenor Pesos: {}. Pessoas: '.format(menor),end = '')
for p in menorpeso:
    print(p, end = ' ')
