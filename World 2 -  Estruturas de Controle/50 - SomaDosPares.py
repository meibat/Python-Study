#Variáveis Globais
soma = 0
#Entrada de dados
for i in range(1, 7):
    numero = int(input('({}/6) - Digite um número inteiro: '.format(i)))
    if numero % 2 == 0:
        soma += numero
print('A Soma de todos os pares é {}.'.format(soma))
