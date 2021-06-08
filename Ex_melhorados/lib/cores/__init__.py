#Cores
def bra(msg):
    return f'\033[m{msg}'


def az(msg):
    return f'\033[1;34m{msg}\033[m'


def ama(msg):
   return f'\033[1;33m{msg}\033[m'


def ver(msg):
    return f'\033[1;32m{msg}\033[m'


def verm(msg):
    return f'\033[1;31m{msg}\033[m'


def rox(msg):
    return f'\033[1;35m{msg}\033[m'


def tur(msg):
    return f'\033[1;36m{msg}\033[m'


if __name__ == '__main__': #testando as cores
    print(bra('Teste'))
    print(az('Teste'))
    print(ama('Teste'))
    print(ver('Teste'))
    print(verm('Teste'))
    print(rox('Teste'))
    print(tur('Teste'))