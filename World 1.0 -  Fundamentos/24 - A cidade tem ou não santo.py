#Entrada
cidade = input('Digite o nome da sua cidade :').strip().capitalize().split()
#Processamento
temSanto = ''
if cidade[0] in 'Santo':
    temSanto = 'Sim'
else:
    temSanto = 'Não'
#Saída
print('A sua cidade começa com "Santo" no nome: {}'.format(temSanto))
