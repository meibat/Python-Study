#Importação de pacotes
from datetime import date
#Variaveis
ano_atual = date.today().year
maior = menor = 0
#Entrada de dados
for i in range(1, 8):
    nasc = int(input('{}º Ano de nascimento: '.format(i)))
    #Processamento
    idade = ano_atual - nasc
    if idade <= 18:
        menor += 1
    else:
        maior += 1
#Saída de dados
print('''
=== RESULTADO FINAL ===
Número de maiores: {} pessoas
Número de menores: {} pessoas'''.format(maior, menor))
