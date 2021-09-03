from math import pi
print('Volume de esfera com raio 5: ', end='')
print(f'{(4/3)*pi*(5**3):.2f}')
print('Custo de 60 livros no atacado: ', end='')
des = 24.95 - (24.95 * (40/100))
print(f'{(des*60) + 3 + (0.75*59):.2f}')
print('Que horas chego em casa para o café da manhã: ', end='')
passo1 = 2 * ((8*60) + 15)
passo2 = 3 * ((7*60)+ 12)
minutos = (6*60) + 52 + ((passo1 + passo2) / 60)
horas = minutos/60
print(f'{horas:.2f}')