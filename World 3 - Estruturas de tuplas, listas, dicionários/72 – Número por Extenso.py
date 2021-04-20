print('Número por extenso:')
numero = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
          'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze',
          'Doze', 'Treze', 'Cartorze', 'Quinze', 'Dezesseis',
          'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    qual = int(input('Digite um número entre 0 e 20: '))
    if 0 <= qual <= 20:
        print(f'Você digitou o número \033[1;34m{numero[qual]}\033[m.')
        op = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if op == 'N':
            break
    else:
        print('\033[1;31mInválido\033[m.', end='')
print('Encerrando...')
