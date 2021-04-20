from random import randint
pc = (randint(0, 10), randint(0, 10), randint(0, 10),
      randint(0, 10), randint(0, 10))
print(f'Os valores escolhidos: ', end='')
for n in pc:
    print(f'{n}', end=' ')
print(f'\nO maior valor sorteado foi {max(pc)}')
print(f'O menor valor sorteado foi {min(pc)}')