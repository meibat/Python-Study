#Entrada de dados
print("=== RADAR ELETRÔNICO ===")
velocidadeDoCondutor = float(input("Qual a velocidade do motorista (em km/h) :"))
#Processamento e Saída
limiteDeVelocidade = 80
if (velocidadeDoCondutor > limiteDeVelocidade):
    print('\033[1;7;31mVOCÊ ULTRAPASSOU O LIMITE DA VELOCIDADE NA RODOVIA\033[m')
    print('Velocidade permitida: {} km/h'.format(limiteDeVelocidade))
    print('\033[1;5mVelocidade registrada {} km/h'.format(velocidadeDoCondutor))
    print('\033[mValor da Multa : R$ {:.2f}'.format(7 * (velocidadeDoCondutor - limiteDeVelocidade)))
    print('Pontos na carteira : +5 (INFRAÇÃO GRAVISSIMA)')
else:
    print('\033[1;7;32mVocê está dentro da velocidade permitida de {} km/h'.format(limiteDeVelocidade))
print('DIRIJA COM PRUDÊNCIA, FAÇA DO TRANSITO SEGURO')