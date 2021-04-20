#Apresentação
print('=== PROGRAMA DE EMPRÉSTIMO ===')
#Entrada de dados
valorDaCasa = float(input('Quanto é o valor da casa? (Em R$) '))
salario = float(input('Qual o seu salário? (Em R$) '))
periodoDeCompra = int(input('Em quantos anos você irá pagar? '))
mensagem = ''
#Processamento
valorDaPrestacao = valorDaCasa / (periodoDeCompra*12)
if valorDaPrestacao > (0.3*salario) :
	mensagem = '\033[1;7;31mEMPRÉSTIMO RECUSADO'
else:
	mensagem = '\033[1;7;32mEMPRÉSTIMO APROVADO'
mensagem +='\033[m'
#Saida de dados
print(mensagem, f'\n Valor da prestação:{valorDaPrestacao}')
