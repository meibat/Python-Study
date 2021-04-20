#Importação de pacotes
from random import choice
#Entrada
opcoes = ['pedra', 'papel', 'tesoura']
playerGanhou = False
escolhaDoJogador = input('Escolha: Pedra, Papel ou Tesoura? ').lower().strip()
escolhaDaMaquina = choice(opcoes)
#Regras
if escolhaDoJogador == 'pedra':
	if escolhaDaMaquina == 'tesoura':
		playerGanhou = True
	else:
		playerGanhou = False
elif escolhaDoJogador == 'papel':
	if escolhaDaMaquina == 'pedra':
		playerGanhou = True
	else:
		playerGanhou == False
elif escolhaDoJogador == 'tesoura':
	if escolhaDaMaquina == 'papel':
		playerGanhou = True
	else:
		playerGanhou = False
else:
	print('Esta opção não existe')

#Saída de dados
print('A MAQUINA ESCOLHEU {}'.format(escolhaDaMaquina))
if playerGanhou:
	print('\033[1;7;32m VOCÊ VENCEU! ')
elif escolhaDaMaquina == escolhaDoJogador:
	print('\033[1;7;33m EMPATOU! ')
else:
	print('\033[1;7;31m VOCÊ PERDEU! ')
