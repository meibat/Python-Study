from lib.interface import *
from time import sleep
while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'], 40, ama, az, ver)
    if resp == 1:
        cabeçalho('Opção 1', 40)
    elif resp == 2:
        cabeçalho('Opção 2', 40)
    elif resp == 3:
        cabeçalho('SAINDO...', 40)
        break
    else:
        txtcor('ERRO! Digite uma opção válida!', verm)
    sleep(1)
