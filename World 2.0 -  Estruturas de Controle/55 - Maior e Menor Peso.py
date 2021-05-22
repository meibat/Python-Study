#Variáveis
maoir = menor = 0
#Entrada de dados
for i in range(0, 6):
    peso = float(input('{}/5 - Digite um peso (em kg): '.format(i+1)))
    # Processamento
    if i == 0:
        maior = menor = peso
    else:
        #Comparação bruta dos pesos
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
#Saída de dados
print('='*35)
print('O maior peso foi {} kg e o menor peso foi {} kg'.format(maior, menor))
