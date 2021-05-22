from datetime import date
cadastro = {}
cadastro['Nome'] = str(input('Nome: '))
nasc = int(input('Data de nascimento: '))
cadastro['Idade'] = date.today().year - nasc
cadastro['CTPS'] = int(input('Carteira de trabalho (0 - não existe): '))
if cadastro['CTPS'] > 0:
    cadastro['Contratação'] = int(input('Ano de contratação: '))
    cadastro['Salário'] = float(input('Salário: '))
    cadastro['Aposentadoria'] = (cadastro['Contratação'] - nasc) + 35
print('-'*30)
for k, v in cadastro.items():
    print(f' - {k}: {v}')