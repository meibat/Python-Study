from ex115.lib.interface import *


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt') #lê o arquivo de txt
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') #escreve ou cria um arquivo de txt
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
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
    try:
        a = open(arq, 'at') #abre e adiciona no arquivo
    except:
        print('Houve um ERRO na abertura doarquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados.')
        else:
            print(f'Novo regristo de {nome} adicionado.')
            a.close()