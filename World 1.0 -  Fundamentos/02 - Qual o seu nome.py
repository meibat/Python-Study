# Entrada de dados
nome = input('Qual o seu nome? ')
# Saída de dados
print('É um prazer em te conhecer {}'.format('\033[7;33m'+nome+'\033[m'))
# OU
print('É um prazer em te conhecer {}{}{}'.format('\033[7;34m', nome,'\033[m'))
# OU
print(f'É um prazer em te conhecer {nome}')
