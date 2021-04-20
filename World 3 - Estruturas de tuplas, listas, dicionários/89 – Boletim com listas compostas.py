lista = []
cont = qual_aluno = 0
quer_cont = ' '
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    quer_cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if quer_cont == 'N':
        break
print('_'*30)
print(f'{"n°":<4}{"NOME":<10}{"NOTA":<4}')
print('-'*30)
for pessoa in lista:
    print(f'{cont:<4}', end='')
    print(f'{pessoa[0]:<10}', end='')
    print(f'{pessoa[2]:<4}')
    cont += 1
while not qual_aluno == 999:
    print('_' * 30)
    qual_aluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if qual_aluno <= len(lista) - 1:
        print(f'notas de {lista[qual_aluno][0]} são {lista[qual_aluno][1]}')
print('FINALIZANDO...')