# Entrada de dados
salario = float(input('\033[32mDigite o salário do funcionário (em R$) :'))
# Processamento
salario = salario + (salario*15/100)# Aumento de 15%
# Saida de dados
print('O Novo salário do funcionário é \033[1;7mR$ {:.2f} \033[m'.format(salario))