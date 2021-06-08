from Ex_melhorados.lib.cores import *
from datetime import date


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


def leiafloat(msg):
    '''
    -> Tenta ler o valor e o válida
    :param msg: valor a ser lido
    :return: o valor ou indica o erro
    '''
    while True:
        try:
            n = str(input(msg)).strip().replace(',', '.')
            n = float(n)
        except(KeyboardInterrupt):
            print(f'\033[1;31mProcesso interrompido pelo usuário.\033[m')
            return 0
        except (ValueError, TypeError):
            print(f'\033[1;31mERRO: não é um número flutuante. Tente novamente!\033[m')
        else:
            return (f'{n:.2f}')

def nome():
    valido = False
    while not valido:
        n = str(input('Nome: ')).strip()
        if n.isnumeric():
            txtcor('ERRO: Nome inválido!', verm)
        elif n == '':
            n = '-Desconhecido-'
            valido = True
        else:
            valido = True
    return n

def nasc_val():
    nasc = date.today().year + 1
    # validação da idade - até 100 anos
    while date.today().year <= nasc or date.today().year - 100 > nasc:
        nasc = leiaint('Ano de nascimento: ')
    return nasc


def idade_val(nasc):
    idade = date.today().year - nasc
    return idade


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
    print(cor(f'{txt}'.center(tam).upper()))
    print(cor(linha(tam)))


def tabela(txt, tam=42, cor=bra):
    print(cor(linha(tam)))
    print(cor(f'{txt}'.upper()))
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
    opc = 0
    for item in lista:
        print(f'{cor1(c)} - {cor2(item)}')
        c += 1
    print(linha(tam))
    while opc < 1 or opc > c+1:
        opc = leiaint(cor3('Sua opção: '))
        linha(80)
    return opc


def quer_cont(tam=42, cor=bra):
    '''
    -> Validando o 'Quer continuar'
    :param tam: tamanho do txt
    :param cor: cor do txt
    :return: a opção escolhida
    '''
    cont = ' '
    while cont not in 'SN':
        print(cor(linha(tam)))
        cont = input('Quer continuar? [S/N] ').strip().upper()[0]
        if cont not in 'SN':
            txtcor('Opção inválida! Tente novamente...', verm)
    return cont
