#Entrada de dados
print('== CALCULO DO IMC ==')
pesoDaPessoa = float(input('Digite o seu peso (em Kg) : '))
alturaDaPessoa = float(input('Agora digite a sua altura (em m) : '))
#Processamento
IndiceDeMassaCorporal = pesoDaPessoa / alturaDaPessoa**2
#Saida de dados
if IndiceDeMassaCorporal < 18.5:
    print('Você está \033[1;30;45m ABAIXO DO PESO IDEAL\033[m')
elif IndiceDeMassaCorporal >= 18.5 and IndiceDeMassaCorporal <= 25:
    print('Você está no \033[1;30;42;m PESO IDEAL\033[m ')
elif IndiceDeMassaCorporal > 25 and IndiceDeMassaCorporal <= 30:
    print('Você está na faixa do \033[1;30;43m SOBREPESO\033[m ')
elif IndiceDeMassaCorporal > 30 and IndiceDeMassaCorporal <= 40:
    print('Você está \033[1;7;33m OBESO\033[m ')
elif IndiceDeMassaCorporal > 40:
    print('Você está na faixa da \033[1;7;31m OBESIDADE MÓRBIDA\033[m ')
