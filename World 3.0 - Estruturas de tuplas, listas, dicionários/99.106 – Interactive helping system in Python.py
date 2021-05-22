from time import sleep
c = ['\033[m',  # sem cor
     '\033[1;30;44m',  # Azul
     '\033[1;30;46m',  # Turquesa
     '\033[1;30;45m',  # Roxo
     '\033[0;30;41m']  # Vermelho


def ajuda(msg):
    titulo(f'Acessando o manual do comando {qual}', cor=2)
    print(c[3], end='')
    help(msg, )
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], '-' * tam)
    print(f'  {msg}')
    print('-' * tam)
    print(c[0], end='')
    sleep(3)


while True:
    titulo('SISTEMA DE AJUDA PYHELP', cor=1)
    qual = str(input('Função ou Biblioteca > '))
    if qual.lower() == 'fim':
        print(c[4], 'ENCERRANDO O PROGRAMA...')
        break
    else:
        ajuda(qual)
