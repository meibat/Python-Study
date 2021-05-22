print('''Digite um NÚMERO INTEIRO e aperte ENTER para ver a sua Tabuada
Para fechar o programa digite um valor negativo e Aperte ENTER''')
while True:
    numero = int(input('Qual número? : '))
    if numero < 0:
        break
    for i in range(1, 11):
        print(f'{numero} x {i} = {numero*i}')
print('='*30)
print('ENCERRANDO O PROGRAMA...')