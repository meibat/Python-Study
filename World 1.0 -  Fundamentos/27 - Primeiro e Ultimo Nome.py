#Entrada de dados
nomeCompleto = input('Digite o seu nome completo: ').split()
#Isso não precisa, só que acho que ficar melhor de entender o código assim
primeiroNome = nomeCompleto[0]
ultimoNome = nomeCompleto[len(nomeCompleto)-1]
#Saída de dados
print('O nome Completo: {} {}'.format(primeiroNome, ultimoNome))
