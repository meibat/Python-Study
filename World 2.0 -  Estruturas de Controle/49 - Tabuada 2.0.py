#Entrada de dados
numeroDaTabuada = int(input('Digite um número para descobrir a tabuada: '))
#Processamento e Saída
for i in range(1, 11):
    print('{} x {} = {}'.format(numeroDaTabuada, i, numeroDaTabuada*i))