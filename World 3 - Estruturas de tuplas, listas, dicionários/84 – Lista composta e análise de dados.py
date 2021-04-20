print('Lista composta e análise de dados:')
pessoa = []
pessoas = []
qct = '' # quer continuar?
maior = menor = 0
while not qct == 'N':
    pessoa.append(str(input('Digite um nome: ')))
    pessoa.append(float(input('Digite um peso: ')))
    # Comparando os valores
    if len(pessoas) == 0:
        maior = menor = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        if pessoa[1] < menor:
            menor = pessoa[1]
    # criando uma lista dentro de outra lista:
    pessoas.append(pessoa[:])
    pessoa.clear()
    qct = str(input('Que continuar? [S/N] ')).strip().upper()
print('-'*40)
print(f'Lista: {pessoas}')
print(f'Foi resgistrado {len(pessoas)} pessoas.')
print(f'O maior peso foi {maior}KG, peso de', end='')
for p in pessoas:
    if p[1] == maior:
        print(f' {p[0]}', end='')
print(f'\nO menor foi {menor}KG, peso de', end='')
for p in pessoas:
    if p[1] == menor:
        print(f' {p[0]}', end='')
