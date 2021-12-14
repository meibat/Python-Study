import random, string

tamanho = 8 #tamanho da senha
chars = string.ascii_letters + string.digits + 'ç%!@&$*#' #caracteres e numeros
rnd = random.SystemRandom()

print(''.join(rnd.choice(chars) for i in range(tamanho)))
