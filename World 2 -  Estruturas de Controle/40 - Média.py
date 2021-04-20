#Entrada de dados
primeiraAvaliacao = float(input('Digite a primeira avaliação : '))
segundaAvaliacao = float(input('Digite a nota da segunda avaliação : '))
media = (primeiraAvaliacao + segundaAvaliacao) / 2
#Processamento - Saída de dados
if media <= 5.0:
    print('REPROVADO!')
elif 7 > media >= 5.0:
    print('RECUPERAÇÃO!')
elif 10 >= media >= 7:
    print('APROVADO!')
else:
    print('Valores incorretos.')