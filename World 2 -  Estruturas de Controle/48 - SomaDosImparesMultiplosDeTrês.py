#Variaveis Globais
limite = 500
soma = cont = 0
#Processamento
for i in range(0, limite+1):
    if i % 2 == 1 and i % 3 == 0:
        soma += i
print('A Somatoria de todos os impares multiplos de três até {} é {}'.format(limite, soma))