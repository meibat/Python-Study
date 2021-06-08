from Ex_melhorados.lib.interface import *


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


def criarArquivo(nome_arq):
    '''
    -> Cria um arquivo de txt
    :param nome: nome do arquivo a ser criado
    :return: se o arquivo foi criado ou não
    '''
    try:
        a = open(nome_arq, 'wt+') #escreve ou cria um arquivo de txt
        a.close()
    except:
        txtcor('Houve um ERRO na criação do arquivo.', verm)
    else:
        print(f'Arquivo {nome_arq} criado com sucesso!')


def lerArquivo(nome_arq):
    '''
    -> Lê o arquivo de forma formatada
    :param nome: nome do arquivo a ser aberto
    :return: mostra o arquivo formatado
    '''
    try:
        a = open(nome_arq, 'rt')
    except:
        txtcor('Erro ao ler o arquivo!', verm)
    else:
        try:
            for linha in a:
                dado = linha.split(';')
                dado[7] = dado[7].replace('\n', '')
                print(f'{dado[0]:<3}{dado[1]:<10}{dado[2]:<15}{dado[3]:<15}{dado[4]:<10}{dado[5]:<10}{dado[7]}')
        except:
            txtcor('Erro ao ler o arquivo!', verm)
    finally:
        a.close()


def cadastrar(arq, nome, nasc=0, idade=0, ctps=0,contra=0, sal=0, aposen=0, cpf=0):
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
        txtcor('Houve um ERRO na abertura do arquivo', verm)
    else:
        try:
            a.write(f'{nome};{nasc};{idade};{ctps};{contra};{sal};{aposen};{cpf}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados.')
        else:
            print(f'Novo regristo de {nome} adicionado.')
            a.close()
