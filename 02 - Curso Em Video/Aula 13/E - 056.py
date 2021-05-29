somaidade = 0
nomevelho = ''
maioridade = 0
contadormulher = 0
for i in range (1,5):
    print('-='*3, '{}a PESSOA'.format(i), '-='*3)
    nome = str(input('Qual o nome? ')).strip()
    c = 0
    while c == 0:
        sexo = str(input('É Masculino (M) ou Feminino (F)? ')).strip().upper()
        if sexo == 'M' or sexo == 'F':
            c = 1
    idade = int(input('Qual a idade? '))
    if sexo == 'M' and idade > maioridade:
        maioridade = idade
        nomevelho = nome
    somaidade += idade
    if sexo == 'F' and idade < 20:
        contadormulher += 1
media = somaidade / 4
print('A média de idade do grupo é de {:.2f}'.format(media))
print('O nome do homem mais velho é {} e ele tem {} anos'.format(nomevelho,maioridade))
print('Nesse grupo houve {} mulheres com idade abaixo dos 20'.format(contadormulher))