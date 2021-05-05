def ficha(n='', g=''):
    print('-'*40)
    if g.isnumeric() or n.strip() == '' or g.strip() == '':
        if g.isnumeric():
            g = int(g)
        elif g.strip() == '':
            g = 0
        if n.strip() == '':
            n = '<Desconhecido>'
        print(f'O jogador {n} fez {g} gol(s) no campeonato.')
    else:
        print('ERRO! O que foi digitado não é um número.')


nome = str(input('Nome do jogador: '))
gols = str(input('Total de gols: '))
ficha(nome, gols)
