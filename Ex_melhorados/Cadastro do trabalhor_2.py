from lib import interface, arquivo
from datetime import date
opcs = ['Ver pessoas cadastradas', 'Registrar nova pessoa', 'Sair o programa'] #opções
salario = contratacao = 0

#verificando se o arquivo existe
arq = 'Cadastros'
if not arquivo.arquivoExiste(arq):
    arquivo.criarArquivo(arq)

while True:
    op = interface.menu(opcs, 80)
    if op == 1:
        interface.cabeçalho('cadastro', 80)
        interface.tabela(f'{"NOME":<10}{"ANO DE NASC":<15}{"CONTRATAÇÃO":<15}{"SALÁRIO":<10}{"CTPS":<10}{"CPF"}', 80)
        arquivo.lerArquivo(arq)
    elif op == 2:
        while True:
            nome = interface.nome()
            #validação da idade - de 16 até 100 anos
            ano_nasc = interface.nasc_val()
            idade = interface.idade_val(ano_nasc)
            while idade < 16:
                ano_nasc = interface.nasc_val()
                idade = interface.idade_val(ano_nasc)
            # se o trabalhador ter CTPS
            ctps = interface.leiaint('Carteira de trabalho (0 - não existe): ')
            if ctps > 0:
                contratacao = interface.leiaint('Ano de contratação: ')
                #validação de ano de contratação
                while contratacao < ano_nasc + 15 or contratacao > date.today().year:
                    contratacao = interface.leiaint('Ano de contratação: ')
                salario = interface.leiafloat('Salário: R$ ')
            cpf = interface.leiaint('CPF: ')
            arquivo.cadastrar(arq, nome, ano_nasc, ctps, contratacao, salario, aposentadoria, cpf)
            quer_cont = interface.quer_cont(80)
            if quer_cont == 'N':
                break
    elif op == 3:
        interface.cabeçalho('Encerrando...', 80)
        break