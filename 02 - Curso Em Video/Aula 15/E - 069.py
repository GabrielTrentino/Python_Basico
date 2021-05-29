maior18 = 0
homens = 0
mulheres = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = str(input('Qual o sexo? [H/M] ')).strip().upper()[0]
    if idade > 18:
        maior18 += 1
    if sexo == 'H':
        homens += 1
    if sexo == 'M' and idade < 20:
        mulheres += 1
    opcao = str(input('Deseja Continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break
print('A) {} pessoas acima de 18 anos'.format(maior18))
print('B) {} homens cadastrados'.format(homens))
print('C) {} mulheres com menos de 20 anos'.format(mulheres))