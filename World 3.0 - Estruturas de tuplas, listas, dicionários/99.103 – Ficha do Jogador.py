def ficha(n='<Desconhecido>', g=0):
    print('-'*40)
    print(f'O jogador {n} fez {g} gol(s) no campeonato.')


nome = str(input('Nome do jogador: '))
gols = str(input('Total de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(g=gols)
else:
    ficha(nome, gols)
