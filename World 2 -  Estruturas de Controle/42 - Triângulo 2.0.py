#Entrada de dados
a = int(input('Valor 1:'))
b = int(input('Valor 2:'))
c = int(input('Valor 3:'))
#Processamento
if a < b + c and b < a + c and c < a + b:
    if a == b == c:
        print('Triângulo Equilátero.')
    elif a == b or b == c or a == c:
        print('Triângulo Isósceles.')
    else:
        print('Triângulo Escaleno.')
else:
    print('Estas medidas não formam um trângulo.')
