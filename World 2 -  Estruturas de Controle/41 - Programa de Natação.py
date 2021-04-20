#Importação de pacotes
from datetime import date
#Entrada de dados
anoDeNascimento = int(input('Digite o seu ano de nascimento: '))
#Processamento e Saída
anoAtual = date.today().year
idade = anoAtual - anoDeNascimento
if idade <= 9:
    print('Você entrará na categoria MIRIM')
elif idade <= 14:
    print('Você entrará na categoria INFANTIL')
elif idade <= 19:
    print('Você entrará na categoria JUNIOR')
elif idade <= 25:
    print('Você entrará na categoria SÊNIOR')
elif idade > 25:
    print('Você entrará na categoria MESTRE')
