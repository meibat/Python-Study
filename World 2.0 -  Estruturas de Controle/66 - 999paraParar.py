numero = soma = cont = 0
print('Digite um número inteiro e Aperte [ENTER]')
print('(i) - Digite 999 para parar as solicitações')
print('====================')
while True:
    numero = int(input('Numero: '))
    if numero != 999:
        cont += 1
        soma += numero
    else:
        break
print('=================')
print(f'Contagem de números: {cont}')
print(f'Sumarização (Soma total): {soma}')