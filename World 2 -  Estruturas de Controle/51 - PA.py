#Forma 1
#Entrada de dados
print('=== PROGRESSÃO ARITMÉTICA ===')
a1 = int(input('Digite o primeiro termo (a1): '))
r = int(input('Agora digite a razão (r): '))
#Saída de dados
print('='*30)
for i in range(a1, 11):
    an = a1 + (i-1) * r
    print(an, end=', ')
print('...')
print('_'*40)
#Forma 2
#Entrada de dados
print('=== PROGRESSÃO ARITMÉTICA ===')
a1 = int(input('Digite o primeiro termo (a1): '))
r = int(input('Agora digite a razão (r): '))
n = int(input('Quantos termos? '))
#Saída de dados
print('='*30)
for an in range(a1, n + 2, r):
    print(an, end=', ')
print('...')