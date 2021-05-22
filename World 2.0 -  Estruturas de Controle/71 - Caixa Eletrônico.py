total_ced = nota_100 = nota_50 = nota_20 = nota_10 = 0
print('== CAIXA ELETRÔNICO 24 HORAS ==')
valor = float(input('Qual o valor que você quer sacar : R$ '))
ced = 100 #primeira cedula
total = valor #total de dinheiro
print(f'VALOR DE SAQUE = R$ {valor:.2f}')
print('-------------------------------')
while True:
    if total >= ced:
        total -= ced #subrai do total
        total_ced += 1
    else:
        if total_ced > 0:
            print(f'{total_ced} x R$ {ced} |')
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        total_ced = 0 #Encerra a contagem de cedula
        if total == 0:
            break
print('Obrigado por utilizar')