#Entrada de dados
print("== CONVERSOR DE NÚMEROS ==")
numeroAleatorio = int(input("Digite um número inteiro e aperte ENTER : "))
opcao = int(input('''\033[32m
Qual a base númerica de conversão:
[1] - Binário
[2] - Octal
[3] - Hexadecimal
Digite a opção : \033[m'''))
#Processamento e Saida
if (opcao == 1) :
    print('O número em binário é {}'.format(bin(numeroAleatorio)))
elif (opcao == 2):
    print('O número em octal é {}'.format(oct(numeroAleatorio)))
elif (opcao == 3):
    print('O número em hexadecimal é {}'.format(hex(numeroAleatorio)))
else:
    print('\033[1;7;31mOPÇÃO INVÁLIDA!')
print('\033[mObrigado por utilizar!')
