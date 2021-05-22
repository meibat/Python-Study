print('Quem é o maior?')
#Entrada de dados
numero1 = int(input('Digite um número inteiro: '))
numero2 = int(input('Digite outro número inteiro: '))
#Processamento e saida
if numero1 > numero2:
    print('O número {} é o maior'.format(numero1))
elif numero2 > numero1:
    print('O número {} é o maior'.format(numero2))
else:
    print('Os números são iguais')
