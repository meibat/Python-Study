print('=*=SEQUÊNCIA DE FIBONACHII =*=')
termos = int(input('Digite quantos termos você quer: '))
t1 = 0
t2 = 1
t3 = 0
print(t1, ' =>', t2, ' =>', end='')
for i in range(1, termos+1):
    t3 = t2 + t1
    print(t3, end=' => ')
    t1 = t2
    t2 = t3
print('...')
print('Fim do Programa')
