print('Dividindo valores em várias listas:')
num = []
par = []
imp = []#ímpar
cont = ''
while not cont == 'N':
    num.append(int(input('Digite um número: ')))
    cont = str(input('Quem continuar? [S/N] ')).strip().upper()
num.sort()#Coloca a lista em ordem
for n in num:
    if n % 2 == 0:
        par.append(n)
    elif n % 2 == 1:
        imp.append(n)
print('_'*40)
print(f'Lista Completa: {num}')
print(f'Lista de pares: {par}')
print(f'Lista de ímpares: {imp}')
