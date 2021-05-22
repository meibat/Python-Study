#Entrada de dados
a = float(input('Digite o valor da reta 1 :'))
b = float(input('Digite o valor da reta 2 :'))
c = float(input('Digite o valor da reta 3 :'))
#Processamento
if a < b + c and b < a + c and c < a + b:
    print('Forma um triângulo')
else:
    print('Não forma um triângulo')