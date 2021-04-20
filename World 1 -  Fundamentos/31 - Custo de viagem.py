#Entrada de dados
quilometragem = float(input('Quantos quilometros dura a sua viagem? '))
#Processamento
if quilometragem > 200:
    taxa = 0.45
else:
    taxa = 0.50
#Saída
print('O Preço da passagem é R$ {:.2f}'.format(quilometragem*taxa))