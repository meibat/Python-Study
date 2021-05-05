def leiaint(msg):
    while True:
        n = input(msg)
        if n.isnumeric():
            n = int(n)
            break
        else:
            print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')
    print('-'*40)
    return n


num = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {num}')
