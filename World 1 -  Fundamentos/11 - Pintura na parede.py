# Entrada de dados
a = float(input('\033[35mQual a altura da parede em metros :'))
l = float(input('Qual a largura da parede em metros :'))
# Processamento
litro = (a*l) / 2  # Cada litro de tinta suporta até 2m²
# Saída de dados
print('A quantidade de tinta necessária é de {:.1f} litros'.format(litro))
