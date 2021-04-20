#Entrada
pares = int(input('Digite um número para descobrir todos os pares: '))
#Processamento e Saída
for i in range(1, pares + 1):
    if i % 2 == 0:
        print(i)
