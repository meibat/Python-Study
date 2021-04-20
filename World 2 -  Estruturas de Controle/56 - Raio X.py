#Variáveis
somaidade = mediaidade = maioridade_H = cont = 0
nome_H_velho = ''
for dados in range(0, 5):
    #Entrada de dados
    print('FORMULÁRIO {}/{}'.format(i+1, 5))
    print('='*30)
    nome = input('Digite o seu nome : ').strip()
    sexo = input('Agora digite o seu sexo biológico (M/F) : ').upper()
    idade = int(input('Agora, digite quantos anos você tem : '))
    somaidade += idade
    #Processamento
    if idade >= maioridade_H and sexo == 'M':
        nome_H_velho = nome
        maioridade_H = idade
    if sexo == 'F' and idade < 20:
        cont += 1
#Saída de dados
mediaidade = somaidade / dados
print('='*30)
print('''
MÉDIA DE IDADE DO GRUPO: {:.1f} ANOS
NOME DO HOMEM MAIS VELHO: {}
MULHERES COM MENOS DE 20 ANOS: {}'''.format(mediaidade, nome_H_velho, cont))
