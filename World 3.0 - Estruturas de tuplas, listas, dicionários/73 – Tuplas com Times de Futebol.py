times = ('Internacional', 'Flamengo','Atlético-MG',
         'São Paulo', 'Fluminense', 'Palmeiras', 'Grêmio',
         'Corinthians', 'Bragantino', 'Athletico-PR',
         'Santos', 'Ceara SC', 'Atlético-GO', 'Sport Recife',
         'Fortaleza', 'Vasco de Gama', 'Bahia', 'Goiás',
         'Coritiba', 'Botafogo')
print('-' * 40)
print(f' Os 5 primeiros times: {times[0:5]}')
print('-' * 40)
print(f'Os últimos 4 colocados: {times[-4:]}')
print('-' * 40)
print('Times em ordem alfabética:')
for t in times:
    print(t)
print('-' * 40)
pos = times.index('Corinthians') #posição
print(f'Em que posição está o time do Corinthians: {pos + 1}ª')
