#Entrada de dados
frase = input('Digite uma frase: ').upper().strip()
#processamento
palavras = frase.split() #separa em lista
junto = ''.join(palavras) #junta as palavras sem espaço
inverso = junto[::-1] #do inicio ao fim, de trás para frente
#Saída de dados
if inverso == junto:
    print('Essa frase é um palindromo.')
else:
    print('Essa frase não é palindromo.')
