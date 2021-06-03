#Cores
def bra(msg):
    return f'\033[m{msg}'


def az(msg):
    return f'\033[1;34m{msg}\033[m'


def ama(msg):
   return f'\033[1;33m{msg}\033[m'


def ver(msg):
    return f'\033[1;32m{msg}\033[m'


def verm(msg):
    return f'\033[1;31m{msg}\033[m'


def rox(msg):
    return f'\033[1;35m{msg}\033[m'


def tur(msg):
    return f'\033[1;36m{msg}\033[m'

#Validação
def leiaint(msg):
    '''
    -> Tenta ler o valor
    :param msg: valor a ser lido
    :return: o valor ou indica o erro
    '''
    while True:
        try:
            n = int(input(msg))
        except(KeyboardInterrupt):
            print(f'\033[1;31mProcesso interrompido pelo usuário.\033[m')
            return 0
        except(ValueError, TypeError):
            print(f'\033[1;31mERRO: não é um número inteiro. Tente novamente!\033[m')
        else:
           return n

#Facilitadores
def linha(tam=42):
    return '-' * tam


def txtcor(txt, cor=bra):
    print(cor(txt))

#Interface
def cabeçalho(txt, tam=42, cor=bra):
    '''
    -> Cria um cabeçalho formatado
    :param txt: título
    :param tam: tamanho do cabeçalho
    :param cor: cor a ser usada
    :return: cabeçalho formatado
    '''
    print(cor(linha(tam)))
    print(cor(f'{txt}'.center(tam)))
    print(cor(linha(tam)))


def menu(lista, tam=42, cor1=bra, cor2=bra, cor3=bra):
    '''
    -> Cria um menu formatado
    :param lista: opções do menu
    :param tam: tamanho do menu
    :param cor1: cor dos números
    :param cor2: cor do txt do menu
    :param cor3: cor da leitura de opção
    :return: menu formatado
    '''
    cabeçalho('MENU PRINCIPAL', tam)
    c = 1
    for item in lista:
        print(f'{cor1(c)} - {cor2(item)}')
        c += 1
    print(linha(tam))
    opc = leiaint(cor3('Sua opção: '))
    return opc