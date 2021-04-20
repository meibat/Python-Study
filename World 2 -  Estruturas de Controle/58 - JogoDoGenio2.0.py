#Bibliotecas
from random import randint
cont = 0
pc = randint(0, 10)
#Entrada de dados
pessoa = int(input('Estou pensando em um número entre 0 e 10, qual o número:'))
#Processamento
while pessoa != pc:
	print('='*20)
	pessoa = int(input('ERROU! Tente novamente: '))
	cont += 1
	if pessoa > pc:
		print('O número é menor que {}'.format(pessoa))
	elif pessoa < pc:
		print('O número é maior que {}'.format(pessoa))
#Saída de dados
print('='*20)
if (pessoa == pc):
	print('Parabéns, você acertou, de {} tentativas'.format(cont))