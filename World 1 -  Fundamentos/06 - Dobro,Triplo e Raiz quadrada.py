# Importação
from math import sqrt
# Entrada de dados
n = int(input('Digite um número inteiro :'))
# Saida de dados
print('\033[35mDobro : {} \nTriplo : {} \nRaiz quadrada : {:.2f}\033[m'.format(n*2, n*3, sqrt(n)))
# OU
print('_'*30)
print(f' O dobro de {n} vale {n*2}')
print(f' O dobro de {n} vale {n*3}')
print(f' O dobro de {n} vale {pow(n,(1/2)):.2f}')