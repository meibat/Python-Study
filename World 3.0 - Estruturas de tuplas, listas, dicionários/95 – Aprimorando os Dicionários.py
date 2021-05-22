jogadores = []
jogador = {}
gols = []
qual_jog = 0
while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for j in range(1, partidas + 1):
        gols.append(int(input(f'Quantos gols na partida {j}? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    jogadores.append(jogador.copy())
    gols.clear()
    print('_'*40)
    quer_cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while not quer_cont in 'SN':
        print('ERRO! Responda apenas S ou N')
        quer_cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if quer_cont == 'N':
        break
print('=-'*40)
print(f'{"cod":<4}{"NOME":<15}{"GOLS":<15}{"TOTAL"}')
print('-'*40)
for k, v in enumerate(jogadores):
    print(f'{k + 1:<4}', end='')
    for c in v.values():
        print(f'{str(c):<20}', end='')
    print()
print('-'*40)
while not qual_jog == 999:
    qual_jog = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    print(f' -- LEVANTAMENTO DO JOGADOR: {jogadores[qual_jog]["nome"]}')
    if qual_jog <= len(jogadores) - 1:
        for i, v in enumerate(jogadores[qual_jog]['gols']):
            print(f'No jogo {i + 1} fez {v} gols.')
    else:
        print('Esse código não existe. Digite novamente!')
print('ENCERRANDO...')
