from datetime import datetime
pessoa = dict()
pessoa['Nome'] = str(input('Digite o nome da pessoa: ')).strip()
pessoa['Nascimento'] = int(input(f'Que ano nasceu? '))
pessoa['Idade'] = datetime.now().year - pessoa['Nascimento']
pessoa['Carteira'] = int(input('Carteira de trabalho (0 não tem) '))
if pessoa['Carteira'] != 0:
    pessoa['Contratacao'] = int(input('Ano de contratação '))
    pessoa['Aposentadoria'] = pessoa['Contratacao'] + 35 + pessoa['Idade'] - datetime.now().year
    pessoa['salario'] = float(input('Salário: R$'))
for v,k in pessoa.items():
    print("{} tem o valor {}".format(v,k))