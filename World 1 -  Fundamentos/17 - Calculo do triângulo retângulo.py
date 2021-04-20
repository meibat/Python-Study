#bibliotecas
from math import sqrt
#Entrada de dados
catetoOp = float(input('\033[32mQual o valor do cateto oposto :'))
catetoAdj = float(input('Qual o valor do cateto adjacente :'))
#Processamento
hipotenusa = catetoOp**2 + catetoAdj**2
hipotenusa = sqrt(hipotenusa)
#Saida de dados
print('O Valor da hipotenusa é {:.2f}'.format(hipotenusa))