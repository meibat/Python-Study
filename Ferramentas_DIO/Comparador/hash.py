import hashlib

arq1 = 'a.txt'
arq2 = 'b.txt'

#cria o objeto
hash1 = hashlib.new('ripemd160')
hash2 = hashlib.new('ripemd160')

#gera o hash
hash1.update(open(arq1, 'rb').read())
hash2.update(open(arq2, 'rb').read())

if hash1.digest() != hash2.digest():
    print('O conteúdo dos arquivos são diferentes')
    print(f'Hash1: {hash1.hexdigest()}') #hash em hexadecimal
    print(f'Hash2: {hash2.hexdigest()}')
else:
    print('O conteúdo dos são iguais')
    print(f'Hash1: {hash1.hexdigest()}')
    print(f'Hash2: {hash2.hexdigest()}')
