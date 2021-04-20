#Variáveis
cont_P = cont_1000 = menor_P = total = 0
while True:
    nome_B = opcao = ''
    #Processamento
    print('*='*15)
    nome_P = input('Qual o nome do Produto: ')
    preco = float(input('Quanto custa: R$ '))
    if cont_P == 1 or preco < menor_P:
        nome_B = nome_P #nome do mais barato
        menor_P = preco #preço do mais barato
    if preco > 1000:
        cont_1000 += 1
    total += preco #soma os preços
    cont_P += 1 #conta os produtos
    opcao = input('Quer continuar (s/n): ').strip().lower()[0]
    if opcao == 'n':
        break
print('===RESULTADO FINAL ===')
print('Total de produtos {}: R$ {:.2f}'.format(cont_P, total))
print('====================================================')
print(f'Quantidade de compras acima de 1000 reais: {cont_1000} produtos')
print('O produto mais barato é o {}'.format(menor_P))
print('=================================================')
print('Encerrando o programa...')