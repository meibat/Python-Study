import phonenumbers
from phonenumbers import geocoder

phone = input('Telefone:')

#convertendo o imput em telefone
phone_number = phonenumbers.parse(phone)

#verifica de qual estado é
print(geocoder.description_for_number(phone_number, 'pt'))