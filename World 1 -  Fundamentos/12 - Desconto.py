#Entrada de dados
p = float(input('Digite o preço de um produto (em R$) :'))
#Processamento
d = p - (p * 5 / 100)
#Saida de dados
print('O Novo preço do produto é R$ {:.2f}'.format(d))