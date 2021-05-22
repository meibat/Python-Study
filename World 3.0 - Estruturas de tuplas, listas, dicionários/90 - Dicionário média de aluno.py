aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif aluno['média'] < 7:
    aluno['situação'] = 'Reprovado'
print('-'*30)
for k, v in aluno.items():
    print(f' - {k} é igual a {v}.')
