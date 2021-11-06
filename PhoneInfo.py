# Obtener informacion sobre un numero telefonico
import phonenumbers
from phonenumbers import carrier, geocoder

def numChecker(phone):
  info = []
  phone = phonenumbers.parse(phone)
  info.append(geocoder.description_for_number(phone, "es"))
  info.append(carrier.name_for_number(phone, "es"))
  return info

phone = input("Introduzca un numero telefonico => ")
print(numChecker(phone))
