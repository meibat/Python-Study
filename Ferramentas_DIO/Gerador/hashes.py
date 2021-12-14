import hashlib

string = str(input('Digite: '))

resultado = hashlib.md5(string.encode('utf-8'))

print(f'Hash: {resultado.hexdigest()}')