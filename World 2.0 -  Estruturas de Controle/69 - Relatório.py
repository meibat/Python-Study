#Variáveis
cont_P = cont_M = cont_18 = cont_F_20 = 0
#Processamento
while True:
    sexo = opcao = ' '
    print('===PESQUISA=== | Total de cadastros: {}'.format(cont_P))
    idade = int(input('Qual a idade do usuário: '))
    while sexo not in 'mf':
        sexo = str(input('Sexo [M/F]: ')).strip().lower()[0]
    cont_P += 1  #conta a pessoa
    while opcao not in 'sn':
        print('_'*40)
        opcao = str(input('Quer cadastrar mais alguém? [S/N] ')).strip().lower()[0]
    if idade >= 18: #se for maior de 18 anos
        cont_18 += 1
    if sexo == 'm':
        cont_M += 1
    if idade >= 20 and sexo == 'f':
        cont_F_20 += 1
    if opcao == 'n': #Encerra o loop
        break
print('==FIM DA PESQUISA ===')
print(f'Total de Entrevistados {cont_P} pessoas')
print('-------------------------------------------------')
print(f'Qtde de Maiores de Idade = {cont_18} pessoas | '
      f'Correspondendo à {(cont_18/cont_P)*100:.2f} % dos cadastros')
print(f'Qtde de Homens = {cont_M} | '
      f'Correspondendo à {(cont_M/cont_P)*100:.2f} % dos cadastros')
print(f'Qtde de Mulheres com menos de 20 anos = {cont_F_20} | '
      f'Correspondendo à {(cont_F_20/cont_P)*100:.2f} % dos cadastros')