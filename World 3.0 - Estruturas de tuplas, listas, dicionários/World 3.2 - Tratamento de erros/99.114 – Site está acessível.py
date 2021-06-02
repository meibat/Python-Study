import urllib
import urllib.request
try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('Não foi possível acessar o site do pudim :(')
else:
    print('Consegui acessar o site do pudim :)')
    print(site.read()) #mostra o código html do site
