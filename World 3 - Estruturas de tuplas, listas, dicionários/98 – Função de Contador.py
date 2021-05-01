from time import sleep


def contador(i, f, p):
    if p < 0: # Se os passos for menor que 0
        p *= -1
    if p == 0: # Se os passos for igual a 0
        p = 1
    print('-='*20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)

    if i < f:
        cont = i
        while cont <= f:# Se inicio for menor que o fim
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f: # Se inicio for maior que o fim
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!')


# Programa principal
# a) de 1 até 10, de 1 em 1
contador(1, 10, 1)
# b) de 10 até 0, de 2 em 2
contador(10, 0, 2)
# c) uma contagem personalizada
print('Agora é sua vez de personalizar a contagem:')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
