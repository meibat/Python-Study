from ex115.lib.interface import *


def arquivoExiste(nome):
    '''
    -> Tenta abrir o arquivo
    :param nome: nome do arquvo a ser aberto
    :return: se o arquivo foi aberto ou deu erro
    '''
    try:
        a = open(nome, 'rt') #lê o arquivo de txt
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    '''
    -> Cria um arquivo de txt
    :param nome: nome do arquivo a ser criado
    :return: se o arquivo foi criado ou não
    '''
    try:
        a = open(nome, 'wt+') #escreve ou cria um arquivo de txt
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    '''
    -> Lê o arquivo de forma formatada
    :param nome: nome do arquivo a ser aberto
    :return: mostra o arquivo formatado
    '''
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='Desconhecido', idade=0):
    '''
    -> Cadastra uma nova pessoa no arquivo
    :param arq: nome do arquivo a ser usado
    :param nome: nome da pessoa a ser add
    :param idade: idade da pessoa a ser add
    :return: informa ser foi concluído ou não o cadastro
    '''
    try:
        a = open(arq, 'at') #abre e adiciona no arquivo
    except:
        print('Houve um ERRO na abertura do arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados.')
        else:
            print(f'Novo regristo de {nome} adicionado.')
            a.close()