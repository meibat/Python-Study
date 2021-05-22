#Entrada de dados
frase = input('Digite uma frase ou um nome :').strip().lower()
#Saída de dados
print('A Frase tem a letra "a" {} vezes'.format(frase.count('a')))
print('Ela aparece pela primeira vez na {}ª letra '.format(frase.find('a')+1))
print('Ela aparece pela ultima vez na {}ª letra'.format(frase.rfind('a')+1))