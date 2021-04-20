print('\033[1m-'*30)
print('{:^30}'.format('CAIXA ELETRÔNICO'))
print('-\033[m'*30)
total_valor = total_saque = valor = 0
opcao_cont = ' '
while opcao_cont != 'N':
    print('\033[1;34mQual valor quer retirar?\n'
                    '[A] R$ 200,00\n'
                    '[B] R$ 300,00\n'
                    '[C] R$ 500,00\n'
                    '[D] R$ 1000,00\n'
                    '[E] Para digitar o valor')
    opcao_saque = str(input('Digite a opção desejada: ')).strip().upper()[0]
    if opcao_saque == 'A':
        valor = 200
    elif opcao_saque == 'B':
        valor = 300
    elif opcao_saque == 'C':
        valor = 500
    elif opcao_saque == 'D':
        valor = 1000
    elif opcao_saque == 'E':
        valor = float(input('Digite o valor: R$ '))
    else:
        valor = float(input('Digite o valor: R$ \033[m'))
    total = valor #total de dinheiro
    ced = 100 #primeira cédula
    total_ced = 0 #total de cédula
    #Saída de dados
    print(f'\033[1mVALOR DE SAQUE = R$ {valor:.2f}')
    print('-------------------------------')
    while True:
        if total >= ced:
            total -= ced #subtrai a cédula do total
            total_ced += 1
        else:
            if total_ced > 0:
                print(f'{total_ced} x R$ {ced} |\033[m')
            if ced == 100:
                ced = 50
            elif ced == 50:
                ced = 20
            elif ced == 20:
                ced = 10
            elif ced == 10:
                ced = 5
            elif ced == 5:
                ced = 1
            total_ced = 0  # Encerra a contagem de cedula
            if total == 0:
                break
    if valor > 0:
        total_saque += 1
    total_valor += valor
    opcao_cont = str(input('Quer efetuar outro saque? [S/N]')).strip().upper()[0]
print('\033[1;34m='*30)
print(f'{total_saque} saques efetuados. Total: R$ {total_valor:.2f}')
print('='*30, '\033[m')
print('\033[1mPROGRAMA ENCERRADO...VOLTE SEMPRE!\033[m')

