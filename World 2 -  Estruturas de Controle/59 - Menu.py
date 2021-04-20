#Variáveis e entrada
numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
maior = opcao = 0
print('='*30)
#Processamento
while opcao != 5:
	print('''
	_______________________
	| CALCULADORA SIMPLES |
	=======================
	| 1 | - Adição        |
	=======================
	| 2 | - Multiplicação |
	=======================
	| 3 | - Qual o maior? |
	=======================
	| 4 | - Novos números |
	=======================
	| 5 | - Encerrar      |
	=======================''')
	opcao = int(input('Qual a sua opção: '))
	print('='*30)
	#Opção 1 do menu - Adição
	if opcao == 1:
		print('{} + {} = {}'.format(numero1, numero2, numero1 + numero2))
	#Opção 2 do menu - Multiplicação
	elif opcao == 2:
		print('{} * {} = {}'.format(numero1, numero2, numero1 * numero2))
	#Opção 3 - Qual o número maior
	elif opcao == 3:
		if numero1 > numero2:
			maior = numero1
		elif numero2 > numero1:
			maior = numero2
		if numero1 == numero2:
			print('Os dois são iguais')
		else:
			print('O maior número é o {}'.format(maior))
	#Opção 4 - Novos Números
	elif opcao == 4:
		numero1 = int(input("Digite um novo valor para o 1º número : "))
		numero2 = int(input("Digite um novo valor para o 2º número : "))
	#Opção 5 - Fechar
	elif opcao == 5:
		print('Encerrando...')
	#Outras opções - Não existe
	else:
		print('OPÇÃO INVALIDA!')
