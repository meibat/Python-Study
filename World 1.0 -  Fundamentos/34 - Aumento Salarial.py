#Entrada de dados
salarioReal = float(input('Digite o salario do funcionário :'))
#Processamento
if salarioReal > 1250:
    Aumento = salarioReal + (salarioReal*10/100)
else:
    Aumento = salarioReal + (salarioReal*15/100)
#Saída de dados
print('O Novo Salário é de R$ {:.2f}'.format(Aumento))
