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
                print(f'{dado[0]:<15}{dado[1]:<15}{dado[3]:<10}{dado[4]:<15}{dado[5]:<15}{dado[7]}')
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


#Funções específicas
def Ver_cadastro(arquivo):
    cabeçalho('cadastro', 80)
    tabela(f'{"NOME":<10}{"ANO DE NASC":<15}{"CONTRATAÇÃO":<15}{"SALÁRIO":<15}{"CTPS":<15}{"CPF"}', 80)
    lerArquivo(arquivo)


def Ler_aposentadoria(arquivo, tam):
    Ver_cadastro(arquivo)
    linha(tam)
    arquivo = open(arquivo, 'r')
    while True:
        trabalhadores = arquivo.read()
        trabalhadores = trabalhadores.split('\n')
        print(trabalhadores)  # divide as linhas
        linha(40)
        qual_tra = str(input('Quer ver a idade de aposentadoria de qual trabalhador? ')).lower().strip()
        for t in trabalhadores:
            #print(t)escreve o que ta na lista
            lista_trabalhador = t.split(';')
            #print(lista_trabalhador)divide o conteúdo da lista
            trabalhador = lista_trabalhador[0]
            #print(trabalhador)nome do trabalhador
            if qual_tra == trabalhador:
                nome = trabalhador
                aposentadoria = lista_trabalhador[6]
            else:
                nome = ''
                aposentadoria = ''
                print('erro')
        print(nome, aposentadoria, 'FIM')