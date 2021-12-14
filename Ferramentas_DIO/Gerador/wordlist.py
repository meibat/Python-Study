import itertools

resultado = itertools.permutations('chars', 3)

for i in resultado:
    print(''.join(i))