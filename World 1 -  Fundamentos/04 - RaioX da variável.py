#Entrada de dados
texto = input('\033[35mDigite algo:')

#Saída de dados
print('='*30)
print('\033[7;1mMensagem : {}\033[m'.format(texto))
print('='*30)
print('\033[1;35mClasse: {}'.format(type(texto)))
print('Ele é um número? : {}'.format(texto.isnumeric()))
print('Ele é um texto? : {}'.format(texto.isalpha()))
print('Ele é texto e número ao mesmo tempo : {}'.format(texto.isalnum()))
print('Ele pode ser impresso?: {}'.format(texto.isprintable()))
print('Ele está em maiúsculo? : {}'.format(texto.isupper()))
print('Ele está capitalizado? : {}'.format(texto.istitle()))
