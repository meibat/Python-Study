#Entrada de dados
numero = input('\033[32mDigite um número natural entre 0 e 9999 :')
numeroDeCasas = len(numero)
#Saida de dados
if (numeroDeCasas > 4):
    print('Digite um número válido na condição mencionada acima')
elif (numero.count('-') > 0):
    print('Não digite números negativos')
else:
    if numeroDeCasas == 1:
        print('Unidade: {}'.format(numero))
    elif numeroDeCasas == 2:
        print('Unidade: {}'.format(numero[1]))
        print('Dezena: {}'.format(numero[0]))
    elif numeroDeCasas == 3:
        print('Unidade: {}'.format(numero[2]))
        print('Dezena: {}'.format(numero[1]))
        print('Centena: {}'.format(numero[0]))
    elif numeroDeCasas == 4:
        print('Unidade: {}'.format(numero[3]))
        print('Dezena: {}'.format(numero[2]))
        print('Centena: {}'.format(numero[1]))
        print('Milhar: {}'.format(numero[0]))