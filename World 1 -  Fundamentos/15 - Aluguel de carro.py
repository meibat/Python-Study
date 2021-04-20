#Constantes
precoDaDiariaDoCarro = 60
precoDoKmRodado = 0.15
#Entrada de dados
dias = int(input('\033[32mQuantos dias foram alugados :'))
km = float(input('Quantos quilometros foram rodados :'))
#Processamento
preço = (dias * 60) + (km * 0.15)  # Total a pagar
#Saída de dados
print('O Total a pagar é R$ {:.2f}'.format(preço))