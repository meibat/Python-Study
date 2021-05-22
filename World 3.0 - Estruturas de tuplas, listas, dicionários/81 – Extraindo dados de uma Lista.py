lista = []
qct = ''
n = cont = 0
while True:
    lista.append(int(input('Digite um número: ')))
    qct = str(input('Quer continuar:[S/N] ')).strip().upper()
    if qct == 'N':
        break
print(f'Foram digitados {len(lista)} números')
lista.sort(reverse=True)
print(f'Ordem descrecente:{lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')