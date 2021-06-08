alunos = []
aluno = {}
cont = qual_aluno = 0
while True:
    aluno['nome'] = str(input('Nome: '))
    aluno['nota 1'] = float(input(f'Nota da 1° Prova: '))
    aluno['nota 2'] = float(input(f'Nota da 2° Prova: '))
    aluno['média'] = (aluno['nota 1'] + aluno['nota 2']) / 2
    if aluno['média'] >= 7:
        aluno['situação'] = '\033[1;34mAprovado\033[m'
    elif 5 <= aluno['média'] < 7:
        aluno['situação'] = '\033[1;33mRecuperação\033[m'
    elif aluno['média'] < 7:
        aluno['situação'] = '\033[1;31mReprovado\033[m'
    alunos.append(aluno.copy())
    print('_' * 30)
    quer_cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if quer_cont == 'N':
        break
print('_'*40)
print(f'{"n°":<4}{"NOME":<10}{"MÉDIA":<10}{"SITUAÇÃO"}')
print('-' * 40)
for aluno in alunos:
    print(f'{cont:<4}', end='')
    print(f'{aluno["nome"]:<10}', end='')
    print(f'{aluno["média"]:<10}', end='')
    print(f'{aluno["situação"]}')
    cont += 1
print('='*40)
print(f'TOTAL DE ALUNOS: {len(alunos)}')
print('_'*40)
while not qual_aluno == 999:
    qual_aluno = int(input('Mostrar notas de qual aluno?\033[1;31m(999 INTERROMPE)\033[m '))
    print('_' * 40)
    if qual_aluno <= len(alunos) - 1:
        print(f'Nome: {alunos[qual_aluno]["nome"]}'
              f'\nNota 1: {alunos[qual_aluno]["nota 1"]}'
              f'\nNota 2: {alunos[qual_aluno]["nota 2"]}')
print('_'*40)
print('FINALIZANDO...')
