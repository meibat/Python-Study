from datetime import date
cadastro = []
trabalhador = {}
qual_tra = cont = 0
while True:
    trabalhador['Nome'] = str(input('Nome: '))
    #validação da idade - de 16 até 100 anos
    trabalhador['Ano_nasc'] = 1 + date.today().year
    while not trabalhador['Ano_nasc'] < date.today().year and \
            trabalhador['Ano_nasc'] > date.today().year - 100:
        trabalhador['Ano_nasc'] = int(input('Ano de nascimento: '))
        trabalhador['Idade'] = date.today().year - trabalhador['Ano_nasc']
        while trabalhador['Idade'] < 16:
            trabalhador['Ano_nasc'] = int(input('Ano de nascimento: '))
            trabalhador['Idade'] = date.today().year - trabalhador['Ano_nasc']
    trabalhador['CTPS'] = int(input('Carteira de trabalho (0 - não existe): '))
    #se o trabalhador ter CTPS
    if trabalhador['CTPS'] > 0:
        trabalhador['Contratação'] = int(input('Ano de contratação: '))
        #validação de ano de contratação
        while trabalhador['Contratação'] < trabalhador['Ano_nasc'] + 15 and trabalhador['Contratação'] > date.today().year:
            trabalhador['Contratação'] = int(input('Ano de contratação: '))
        trabalhador['Salário'] = float(input('Salário: R$ '))
        trabalhador['Aposentadoria'] = (trabalhador['Contratação'] - trabalhador['Ano_nasc']) + 35
    trabalhador['CPF'] = int(input('CPF: '))
    cadastro.append(trabalhador.copy())
    print('-' * 40)
    quer_cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    print('_' * 40)
    if quer_cont == 'N':
        break
print('\033[1;33m-'*80)
print(f'{"CADASTRO":^80}')
print('-' * 80)
print(f'{"n°":<3}{"NOME":<10}{"ANO DE NASC":<15}{"CONTRATAÇÃO":<15}{"SALÁRIO":<10}{"CTPS":<10}{"CPF"}')
print('-' * 80)
for t in cadastro:
    print(f'\033[m{cont:<3}', end='')
    print(f'{t["Nome"]:<10}', end='')
    print(f'{t["Ano_nasc"]:<15}', end='')
    if t['CTPS'] > 0:
        print(f'{t["Contratação"]:<15}', end='')
        print(f'{t["Salário"]:<10}', end='')
    else:
        print(f'{"0":<15}', end='')
        print(f'{"0":<10}', end='')
    print(f'{t["CTPS"]:<10}', end='')
    print(f'{t["CPF"]}')
    cont += 1
while not qual_tra == 999:
    print('_' * 40)
    qual_tra = int(input('Quer ver a idade atual e a idade de aposentadoria de qual trabalhador? [999 interrompe] '))
    if qual_tra <= len(cadastro) - 1 and trabalhador['CTPS'] >= 1:
        print(f'Nome: {cadastro[qual_tra]["Nome"]}'
              f'\nIdade atual: {cadastro[qual_tra]["Idade"]}'
              f'\nIdade de se aposentar: {cadastro[qual_tra]["Aposentadoria"]}')
    elif qual_tra <= len(cadastro) - 1 and trabalhador['CTPS'] <= 0:
      print('Esse trabalhador não possui Carteira Trabalho!')
print('_' * 40)
print('Encerrando...')