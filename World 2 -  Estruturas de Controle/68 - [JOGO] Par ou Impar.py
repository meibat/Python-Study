#Bibliotecas
from random import randint
cont = 0
#Processamento
while True:
    n = int(input('Digite um número [0 a 10]: '))
    pc = randint(0, 10)
    p = ' ' #pergunta
    r = (pc + n) % 2 #determina se é par ou ímpar
    while p not in 'PI':
        p = str(input('Par ou ímpar? ')).strip().upper()[0]
    print(f'Você jogou {n} e o PC {pc}. Total: {n + pc} - ', end='')
    print('Deu PAR!' if r == 0 else 'Deu ÍMPAR!')
    if r == 0 and p == 'P' or r == 1 and p == 'I':
        print('Você GANHOU!')
        print('_'*40)
        print('Vamos jogar novamente...')
        cont += 1
    if r == 0 and p == 'I' or r == 1 and p == 'P':
        print('Você PERDEU! GAME OVER...')
        break
print('_'*40)
print(f'Você ganhou {cont}x do computador!')
print('Encerrando o programa...')
