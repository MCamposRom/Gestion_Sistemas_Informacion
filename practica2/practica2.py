from urllib.request import urlopen
import json
import time

##Clase ExchangeAPIClient que tiene un array con los cambios a euros y un metodo que los recoge de  la api
class ExchangeAPIClient:
    def __init__(self):
        self.data=[]
        
    def get_data(self):
        api_url = 'https://api.exchangeratesapi.io/latest'
        response = urlopen(api_url)
        self.data = json.loads(response.read())

    def convert(self,cantidad, de):
        return cantidad / self.data['rates'][de]


##Lee el fichero y guarda los datos en elñ array "fila"
def LeerDivisas():
    fila = []
    with open('divisas.txt') as file:
        for linea in file:
            fila.append(linea.strip().split(','))
    return fila


##Escribe el cambio a euros de nuestro ahorros en un fichero junto con el dia en el que se ha realizado la conversión
def EscribirAhorros(cantidad,fecha):
    with open('ahorros.txt','a+') as file:
        file.write('{}, {}\n'.format(fecha, int(cantidad)))


##Estructura del programa que utiliza las funciones y suma todas las catidades convertidas a euros
if __name__ == '__main__':
    API = ExchangeAPIClient()
    API.get_data()
    MiDinero = LeerDivisas()
    cantidad_total = 0
    for element in MiDinero:
        if element[0] == API.data['base']:
            cantidad_total += int(element[1])
        else:
            if element[0] in API.data['rates']:
                cantidad_total += + API.convert(int(element[1]),element[0])
    EscribirAhorros(cantidad_total,API.data['date'])
