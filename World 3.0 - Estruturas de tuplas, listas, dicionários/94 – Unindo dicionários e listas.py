cadastro = []
pessoa = {}
media = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while not pessoa['sexo'] in 'MF':
        print('ERRO! Pro favor, digite apenas M ou F.')
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    pessoa['idade'] = int(input('Idade: '))
    cadastro.append(pessoa.copy())
    print('-'*30)
    quer_cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while not quer_cont in 'SN':
        print('ERRO! Responda apenas S ou N')
        quer_cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if quer_cont == 'N':
        break
print('='*30)
print(f'A) Ao todo temos {len(cadastro)} pessoas cadastradas.')
for pessoa in cadastro:
    media += pessoa['idade']
media = media / len(cadastro)
print(f'B) A média de idade é {media:.2f}')
print(f'C) As mulheres cadastradas foram: ', end=' ')
for p in cadastro:
    if p['sexo'] == 'F':
        print(p['nome'], end=' ')
print('\nLista de pessoas que estão acima da média:', end='')
for p in cadastro:
    if p['idade'] >= media:
        print('  ')
        for k, v in p.items():
            print(f' {k} = {v};', end='')
print('\n<<<ENCERRADO>>>')