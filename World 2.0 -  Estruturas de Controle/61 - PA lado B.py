#Dados de Entrada
a1 = int(input('Qual o primeiro termo (a1) da PA: '))
r = int(input('Qual a razão(r): '))
termo = a1
cont = 1
while cont <= 10:
    print('{}'.format(termo), end=' => ')
    termo += r
    cont += 1
print('...')
print('\nFim Do Programa')