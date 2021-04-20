opcao = 's'
menor = maior = media = soma = numero = cont = 0
while True:
        numero = float(input('Digite um número: '))
        cont += 1
        soma += numero
        if cont == 1 or numero > maior:
            maior = numero
        if cont == 1 or numero < menor:
            menor = numero
        opcao = input('Voce quer continuar (s/n) : ').upper()
        if opcao == 'N':
            break
media = soma/cont
print(f'''
====================================
A Média entre eles é {media:.1f}   |
O Maior número é {maior:.1f} |
O Menor número é {menor:.1f} |
====================================
''')
