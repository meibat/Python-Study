#Bibliotecas
from random import shuffle
#Entrada de dados
aluno01 = str(input('Digite o nome do 1º Aluno :'))
aluno02 = str(input('Digite o nome do 2º Aluno :'))
aluno03 = str(input('Digite o nome do 3º Aluno :'))
aluno04 = str(input('Digite o nome do 4º Aluno :'))
lista = [aluno01, aluno02, aluno03, aluno04]
#Processamento
shuffle(lista)
#Saida de dados
print('O ordem de apresentação será {}'.format(lista))