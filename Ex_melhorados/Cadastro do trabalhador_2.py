from lib import interface, arquivo
from datetime import date
opcs = ['Ver pessoas cadastradas', 'Registrar nova pessoa', 'Ver a idade de aposentadoria'
                                                            '', 'Sair o programa'] #opções
aposentadoria = salario = contratacao = 0

#verificando se o arquivo existe
arq = 'Cadastros'
if not arquivo.arquivoExiste(arq):
    arquivo.criarArquivo(arq)

while True:
    op = interface.menu(opcs, 80)
    if op == 1:
        arquivo.Ver_cadastro(arq)
    elif op == 2:
        arquivo.Ler_aposentadoria(arq, 80)
    elif op == 3:
        arquivo.Ler_aposentadoria(arq, 80)#Problema
    elif op == 4:
        interface.cabeçalho('Encerrando...', 80)
        break