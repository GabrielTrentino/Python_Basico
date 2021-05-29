galera = list()
soma = 0
pessoa = dict()
while True:
    pessoa['nome'] = str(input('Nome da pessoa: ')).strip()
    while True:
        pessoa['sexo'] = str(input('Sexo: ')).strip()
        if pessoa['sexo'] in "MmFf":
            break
        print('Dado Invalido! Digite M ou F para sexo.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        r = str(input('Deseja continuar? [S/N] ')).strip().upper()
        if r in 'SN':
            break
        print('Digite S ou N.')
    if r == 'N':
        break
print('-='*40)
print('Foram cadastradas {} entradas'.format(len(galera)))
media = soma/len(galera)
print('A média da idade é {:5.2f}'.format(media))
print('-='*25)
print(f'{"PESSOAS DO SEXO FEMININO":^50}')
print('Nomes:',end =' ')
for p in galera:
    if p['sexo'] in 'Ff':
        print(p["nome"], end = ' ')
print()
print('-=' * 25)
print(f'{"PESSOAS COM IDADE ACIMA DA MEDIA":^50}')
for p in galera:
    if p['idade'] >= media:
        print(p['nome'],' -> ',p['sexo'],' -> ',p['idade'])
        print(f'{"-"*10:^30}')
