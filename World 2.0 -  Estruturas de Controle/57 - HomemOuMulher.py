#Varíaveis
sexo = ''
laço = True
#processamento
while laço:
	sexo = input('Digite o seu sexo biológico(M/F) : ').upper().strip()[0]
	if sexo == 'M' or sexo == 'F':
		laço = False
print('Encerrando...')
