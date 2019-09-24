from urllib.request import urlopen
import json
import time

##Clase ExchangeAPIClient que tiene un array con los cambios a euros y un metodo que los recoge de  la api

class ExchangeAPIClient:
    def __init__(self):
        self.rates=[]
        
    def get_rates(self):
        api_url = 'https://api.exchangeratesapi.io/latest'
        response = urlopen(api_url)
        self.rates = json.loads(response.read())
        return self.rates['rates']

##Realiza el cambio de la moneda "de" a euros

def convert(cantidad, de):
    API = ExchangeAPIClient()
    rates = API.get_rates()
    return int(cantidad / rates[de])

##Lee el fichero y guarda los datos en elñ array "fila"

def LeerDivisas():
    i=1
    fila = []
    with open('divisas.txt') as file:
        for linea in file:
            fila.append(linea.strip().split(','))
            i += 1
    return fila

##Escribe el cambio a euros de nuestro ahorros en un fichero junto con el dia en el que se ha realizado la conversión

def EscribirAhorros(cantidad):
    with open('ahorros.txt','a+') as file:
        file.write('{}, {}\n'.format(time.strftime("%Y-%m-%d"),cantidad))

##Estructura del programa que utiliza las funciones y suma todas las catidades convertidas a euros

if __name__ == '__main__':
    MiDinero = LeerDivisas()
    cantidad_en_euros = 0
    i=0
    while i<len(MiDinero):
        if(MiDinero[i][0] == 'EUR'):
            cantidad_en_euros += int(MiDinero[i][1])
        else:
            cantidad_rate = convert(int(MiDinero[i][1]), MiDinero[i][0])
            cantidad_en_euros += cantidad_en_euros + cantidad_rate
        i += 1
    EscribirAhorros(cantidad_en_euros)
