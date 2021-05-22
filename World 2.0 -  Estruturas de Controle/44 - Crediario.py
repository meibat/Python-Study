#Entrada de dados
preco = float(input('Digite o preço do produto (em R$) : '))
print('''
    Qual a forma de pagamento?
    
    [1] - Dinheiro / Cheque
    [2] - Cartão de Débito
    [3] - Cartão de Crédito (3x ou mais)''')
opcao = int(input('Escolha a sua opçao : '))
#Processamento
if opcao == 1: # 10% de desconto
    precofinal = preco - (preco * (10/100))
elif opcao == 2: # 5% de desconto
    precofinal = preco - (preco * (5 / 100))
elif opcao == 3: # 20% de juros
    x = int(input('Quantas parcelas? [Até 12x] '))
    if 3 >= x <= 12:
        parcela = (preco + (preco * 20/100)) / x
        precofinal = parcela * x
else:
    print('Opção Inválida!')
#Saída de dados
print('=== CUPOM FISCAL ELETRÔNICO ===')
print('Valor da Compra : R$ {:.2f}'.format(preco))
if opcao == 3:
    print('Parcelas: {} x R$ {:.2f}'.format(x, parcela))
elif opcao == 3:
    print('Parcela Inválida!')
else:
    print('TOTAL A PAGAR: R$ {:.2f}'.format(precofinal))
