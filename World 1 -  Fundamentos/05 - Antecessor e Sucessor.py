#Entrada de dados
numero = int(input('Digite um número:'))
#Saída de dados
print('_'*40)
print('\033[31mA Sequência é {},{},{},...\033[m'.format(numero-1,numero,numero+1))
# OU
print(f'\033[32mA Sequência é {numero-1},{numero},{numero+1},...\033[m')
# OU
a = numero - 1
s = numero + 1
print('\033[33mA Sequência é {},{},{},...\033[m'.format(numero, a, s))
