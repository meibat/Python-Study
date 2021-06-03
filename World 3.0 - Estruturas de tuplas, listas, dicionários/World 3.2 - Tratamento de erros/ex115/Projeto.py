from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'], 40, ama, az, ver)
    if resp == 1:
        lerArquivo(arq)
    elif resp == 2:
        cabeçalho('NOVO CADASTRO', 40)
        nome = input('Nome: ')
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resp == 3:
        cabeçalho('SAINDO...', 40)
        break
    else:
        txtcor('ERRO! Digite uma opção válida!', verm)
    sleep(1)
