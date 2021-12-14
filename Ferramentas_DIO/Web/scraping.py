from bs4 import BeautifulSoup
import requests

#Site recebe o conteúdo da requisição http do site
site = requests.get('https://www.climatempo.com.br/').content

#soup baixa o html do site
soup = BeautifulSoup(site, 'html.parser')

#transforma o html em str e exibe
#print(soup.prettify())

temperatura = soup.find("spam", class_="_block _margin-b-5 -gray")
#print(temperatura)

print(soup.title.string)