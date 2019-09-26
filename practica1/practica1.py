import random

##Clase jugador
class Jugador:
    def __init__(self, nombre):
        self.nombre=nombre
        self.intentos
        
        def get_intentos()
            return self.intentos
        
        def increment_intentos()
            self.intentos += 1
        
        def initialize_intentos()
            self.intentos=0

##Clase maquina
class Jugador:
    def __init__(self):
        self.intentos
        
        def get_intentos()
            return self.intentos
        
        def increment_intentos()
            self.intentos += 1
        
        def initialize_intentos()
            self.intentos=0
        
##Obtenemos numero aleatorio
def getRandom(x,y):
    return random.randrange(x,y)


##El jugador adivina el numero de la maquina
def adivinaJugador(jugador):
    jugador.initialize_intentos
    jugador.increment_intentos
    a=getRandom(0,100)
    repeat = 'y'
    while repeat == 'y':
        b=input()
        if b.isnumeric():
            if ((eval(b)<0) | (eval(b)>100)) :
                print("Error: el número esta fuera del rango [0,100], por favor introduzca un número correcto.")
            else:
                repeat = 'n'
                while eval(b)!=a:
                    jugador.increment_intentos
                    if eval(b)<a:
                        print("Mi número es mayor")
                    else:
                        print("Mi número es menor")  
                    b=input()
        else:
            print("Error: No me has dado un número, por favor introduzca un número.")
    
    
##El ordenador adivina el numero del jugador
def adivinaMaquina(maquina):
    x=0
    y=100
    r=' '
    maquina.initialize_intentos
    while r != 'Correcto':
        maquina.increment_intentos
        if x==y:
            r=input('El número que has pensado es el {}.\nMayor/Menor/Correcto? '.format(x))
        else:
            a=getRandom(x,y)
            repeat = 'y'
            while repeat == 'y':
                r=input('El número que has pensado es el {}.\nMayor/Menor/Correcto? '.format(a))
                if r=='Mayor':
                    x=a+1
                    repeat='n'
                elif r=='Menor':
                    y=a-1
                    repeat='n'
                elif r!='Correcto':
                    print('Error: La respuesta no es valida.')

##Main - Estructura del juego
if __name__ == '__main__':
    nombre_jugador=input("¡Hola! ¿Como te llamas?\n")
    jugador = Jugador(nombre_jugador)
    maquina = Maquina()
    repetir="S"
    while repetir=="S":
        print("Bueno, {}, estoy pensando en un número entre 1 y 100. Intenta adivinarlo.".format(jugador.nombre))
        adivinaJugador(jugador)
        print("¡Buen trabajo, {}! ¡Has adivinado mi número en {} intentos! Es tu turno.\n".format(jugador.nombre, jugador.intentos))
        adivinaMaquina(maquina)
        if jugador.intentos>maquina.intentos:
            print("\nYo gano. He acertado en {} intentos.".format(maquina.intentos))
        elif jugador.intentos<maquina.intentos:
            print("\nTu ganas. Has acertado en {} intentos.".format(jugador.intentos))
        else:
            print("\nHemos empatado. Ambos hemos acertado en {} intentos.".format(maquina.intentos))
        repetir = input("\nQuieres seguir jugando? S/N ")
