def voto(ano):
    from datetime import date
    ano_atual = date.today().year
    if ano < ano_atual:
        idade = ano_atual - ano
        print(f'Com {idade} anos: ', end='')
        if idade < 16:
            return 'NÃO VOTA.'
        elif idade < 18 or idade > 70:
            return 'VOTO OPCIONAL.'
        elif 18 <= idade:
            return 'VOTO OBRIGATÓRIO.'
    else:
        print('ERRO! Ano maior do que o ano atual!')


# Programa principal
ano_nascimento = int(input('Ano de nascimento: '))
voto(ano_nascimento)
