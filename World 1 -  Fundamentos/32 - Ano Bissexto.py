#Biblioteca
from datetime import date
#Entrada
ano = int(input('Qual o ano de hoje (0 = Ano atual): '))
#Processamento e Saída
if ano == 0:
    ano = date.today().year #Ano atual
if ano % 4 == 0:
    print('É um ano bissexto')
else:
    print('Não é um ano bissexto')
