lista = list()
r = 's'
while r in 'Ss':
    nome = str(input('Digite o nome do Aluno: '))
    n1 = int(input('N1: '))
    n2 = int(input('N2: '))
    media = (n1+n2)/2
    lista.append([nome,n1,n2,media])

    r = str(input('Deseja continuar? [S/N] ')).strip()
    while r not in 'NnSs':
        r = str(input('Deseja continuar? [S/N] ')).strip()
    if r in 'Nn':
        break

print('-='*20)
print('{:^40}'.format('NOTAS DOS ALUNOS'))
print('-='*20)
print(f'{"No.":<4}{"NOME":<30}{"MÉDIA":<5}')
for i,a in enumerate(lista):
    print(f'{i:<4}{a[0]:<30}{a[3]:<5}')
while True:
    r = int(input('Mostrar notas de qual aluno? (999 para interrompner) '))
    if r == 999:
        break
    elif r == 1000:
        print('-=' * 20)
        print('{:^40}'.format('NOTAS DOS ALUNOS'))
        print('-=' * 20)
        print(f'{"No.":<4}{"NOME":<30}{"MÉDIA":<5}')
        for i, a in enumerate(lista):
            print(f'{i:<4}{a[0]:<30}{a[3]:<5}')
        continue
    print('As notas de {} são {}'.format([lista[r][0]],lista[r][1:3]))
    print()
    print('Para mostrar a lista, digite: 1000')

print('-'*40)
print('Programa Finalizado')