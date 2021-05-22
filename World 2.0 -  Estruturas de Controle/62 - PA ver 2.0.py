#Dados de Entrada
a1 = int(input('Qual o primeiro termo (a1) da PA: '))
r = int(input('Qual a razão(r): '))
termo = a1
cont = 1
total = 0
mais = 10
#processamento
while mais != 0:
    total += mais
    while cont <= total:
        print('{} ->'.format(termo), end='')
        termo += r
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos quer mostrar a mais? '))
print('Progressão encerrada com {} termos apresentados'.format(total))
