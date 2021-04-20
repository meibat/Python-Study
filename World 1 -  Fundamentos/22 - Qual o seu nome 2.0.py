#Entrada de dados
nome = input('\033[34mDigite o seu nome completo e aperte ENTER :')
#Processamento
espacos = nome.count(' ')
nomeQuebrado = nome.split()
# Saida de dados
print('O seu nome em MAIUSCULO: {}'.format(nome.upper()))
print('O seu nome em minusculo: {}'.format(nome.lower()))
print('O seu nome tem um total de {} letras.'.format(len(nome) - espacos))
print('O primeiro nome tem {} letras.'.format(len(nomeQuebrado[0])))
