from time import sleep
inicio = passo = 1
fim = 10
def contador(num):
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}.')
    for x in range(inicio, fim + 1, passo):
        sleep(0.2)
        print(x, end=' ')
    print('FIM!')
    print('=-' * 15)


contador('num')
inicio = 10
passo = fim = -2
contador('num')
print('')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
if passo == 0:
    passo = 1
contador('num')
