# Entrada de dados
Celsius = float(input('\033[34mInforme a temperatura em celsius(ºC) :'))
# Processamento
Fahrenheit = ((9 * Celsius) / 5) + 32
Kelvin = ((Celsius * 5) / 5)
# Saída de dados
print('A Temperatura em fahrenheit é {:.1f} ºF'.format(Fahrenheit))
print('A Temperatura em kelvin é {:.1f} ºK'.format(Kelvin))
