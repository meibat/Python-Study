numero = soma = contagemDeNumeros = 0
print('Digite um número inteiro e Aperte [ENTER]')
print('(i) - Digite 999 para parar as solicitações')
print('====================')
while numero != 999:
    numero = int(input('Numero: '))
    if numero != 999:
        contagemDeNumeros += 1
        soma += numero
print('=================')
print('Contagem de números: {}'.format(contagemDeNumeros))
print('Sumarização (Soma total): {}'.format(soma))
