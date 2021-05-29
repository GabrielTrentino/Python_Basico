Galera = list()
Pessoa = dict()
while True:
    totaldegols = 0
    Pessoa['nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {Pessoa["nome"]} jogou? '))
    gols = list()
    for i in range(0,partidas):
        gol = int(input(f'    Quantos gols na {i} partida? '))
        gols.append(gol)
        totaldegols += gol
    Pessoa['gols'] = gols
    Pessoa['total'] = totaldegols
    Galera.append(Pessoa.copy())
    while True:
        r = str(input('Deseja continuar? [S/N] ')).strip().upper()
        if r in 'SN':
            break
        print('Digite S ou N.')
    if r == 'N':
        break

#print(Galera)
print('-='*40)
print(f'{"RESULTADOS":^80}')
print(f'{"cod":<4}{"nome":<30}{"gols":<30}{"total":<5}')
print('-'*80)
for pos, p in enumerate(Galera):
    print(f'{pos:<3}{p["nome"]:<30}{str(p["gols"]):<30}{p["total"]:<5}')

while True:
    r = int(input('Mostrar dados de Qual jogador? (999 para parar) '))
    if r == 999:
        break
    if r >= len(Galera):
        print('Número não encontrado, tente novamente.')
    else:
        print(f' -- Levantamento do jogador: {Galera[r]["nome"]}')
        for i in Galera[r]["gols"]:
            print('    => Na partida {}, fez {} gols'.format(i-1,Galera[r]["gols"]))


