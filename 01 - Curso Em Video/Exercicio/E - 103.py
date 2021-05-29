def ficha(nome,gol):
    if nome.isalpha():
        nome = str(nome)
    else:
        nome = '<desconhecido>'
    if gol.isnumeric():
        gol = int(gol)
    else:
        gol = 0
    print(f'O jogador {nome} fez {gol} gol(s) no campeonato')

jogador = input('Nome do Jogador: ')
gol = input('Número de Gols: ')
ficha(jogador,gol)
