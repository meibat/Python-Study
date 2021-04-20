#Bibliotecas
from math import sin, cos, tan, radians
#Entrada de dados
angulo = float(input('\033[32mQual o valor do ângulo :'))
#Processamento
angulo = radians(angulo)
seno = sin(angulo)
cosseno = cos(angulo)
tangente = tan(angulo)
#Saída de dados
print('Seno : {:.2f}'.format(seno))
print('Cosseno : {:.2f}'.format(cosseno))
print('Tangente : {:.2f}'.format(tangente))
