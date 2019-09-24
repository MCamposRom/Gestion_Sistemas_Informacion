import random

##Clase jugador

class Jugador:
    def __init__(self, nombre):
        self.nombre=nombre
        
        
##Obtenemos numero aleatorio

def getRandom(x,y):
    return random.randrange(x,y)


##El jugador adivina el numero de la maquina

def adivinaJugador():
    intentos=1
    a=getRandom(0,100)
    repeat = 'y'
    while repeat == 'y':
        b=input()
        if b.isnumeric():
            repeat = 'n'
            while eval(b)!=a:
                intentos += 1
                if eval(b)<a:
                    print("Mi número es mayor")
                else:
                    print("Mi número es menor")  
                b=input()
            return intentos
        else:
            print("Error: No me has dado un numero.")
    
    
##El ordenador adivina el numero del jugador
            
def adivinaMaquina():
    x=0
    y=100
    r=' '
    intentos=0
    while r != 'Correcto':
        intentos += 1
        if x==y:
            r=input('El número que has pensado es el {}.\nMayor/Menor/Correcto? '.format(x))
            return intentos
        else:
            a=getRandom(x,y)
            repeat = 'y'
            while repeat == 'y':
                r=input('El número que has pensado es el {}.\nMayor/Menor/Correcto? '.format(a))
                if r=='Correcto':
                    return intentos
                else:
                    if r=='Mayor':
                        x=a+1
                        repeat='n'
                    else :
                        if r=='Menor':
                            y=a-1
                            repeat='n'
                        else:
                            print('Error: La respuesta no es valida.')

##Main - Estructura del juego

if __name__ == '__main__':
    nombre_jugador=input("¡Hola! ¿Como te llamas?\n")
    jugador = Jugador(nombre_jugador)
    intentos_jugador=0
    intentos_maquina=0
    repetir="S"
    while repetir=="S":
        print("Bueno, {}, estoy pensando en un número entre 1 y 100. Intenta adivinarlo.".format(jugador.nombre))
        intentos_jugador=adivinaJugador()
        print("¡Buen trabajo, {}! ¡Has adivinado mi número en {} intentos! Es tu turno.\n".format(jugador.nombre, intentos_jugador))
        intentos_maquina=adivinaMaquina()
        if intentos_jugador>intentos_maquina:
            print("\nYo gano. He acertado en {} intentos.".format(intentos_maquina))
        else:
            if intentos_jugador<intentos_maquina:
                print("\nTu ganas. Has acertado en {} intentos.".format(intentos_jugador))
            else:
                print("\nHemos empatado. Ambos hemos acertado en {} intentos.".format(intentos_maquina))
        repetir = input("\nQuieres seguir jugando? S/N ")
