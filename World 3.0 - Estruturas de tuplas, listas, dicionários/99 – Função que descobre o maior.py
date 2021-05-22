from time import sleep


def maior(*num):
    m = cont = 0
    print('Analisando os valores passados...')
    if len(num) > 0:
        for n in num:
            print(f'{n} ', end='', flush=True)
            sleep(0.3)
            if cont == 0:
                m = n
            if cont > 0 and n > m:
                m = n
            cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {m}.')
    print('_' * 40)


# 1° Análise
maior(2, 9, 4, 5, 7, 1)
# 2° Análise
maior(4, 7, 0)
# 3° Análise
maior(1, 2)
# 4° Análise
maior(6)
# 5° Análise
maior()
