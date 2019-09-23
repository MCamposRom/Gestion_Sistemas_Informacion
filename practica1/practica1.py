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
    b=input()
    if b.isnumeric():
        while eval(b)!=a:
            intentos += 1
            print("intento++")
            if eval(b)<a:
                print("Mi número es mayor")
            else:
                print("Mi número es menor")  
            b=input()
        return intentos
    else:
        print("No me has dado un numero.")
        return -1
    
    
##El ordenador adivina el numero del jugador
            
def adivinaMaquina():
    print("AdivinaMaquina")
    x=0
    y=100
    r=' '
    intentos=0
    while r != 'Correcto':
        intentos += 1
        print("intento++")
        if x==y:
            print(intentos)
            return intentos
        else:
            a=getRandom(x,y)
            r=input('El número que has pensado es el {}.\nMayor/Menor/Correcto? '.format(a))
            if r=='Correcto':
                print(intentos)
                return intentos
            else:
                if r=='Mayor':
                    x=a+1
                else:
                    y=a-1


if __name__ == '__main__':
    nombre_jugador=input("¡Hola! ¿Como te llamas?\n")
    jugador = Jugador(nombre_jugador)
    intentos_jugador=0
    intentos_maquina=0
    repetir="S"
    while repetir=="S":
        print("Bueno, {}, estoy pensando en un número entre 1 y 100. Intenta adivinarlo.".format(jugador.nombre))
        intentos_jugador=adivinaJugador()
        print("¡Buen trabajo, {}! ¡Has adivinado mi número en {} intentos! Es tu turno.".format(jugador.nombre, intentos_jugador))
        intentos_maquina=adivinaMaquina()
        print("Jugador {} - {} Maquina".format(intentos_jugador,intentos_maquina))
        if intentos_jugador>intentos_maquina:
            print("Yo gano. He acertado en {} intentos.".format(intentos_maquina))
        else:
            if intentos_jugador<intentos_maquina:
                print("Tu ganas. Has acertado en {} intentos.".format(intentos_maquina))
            else:
                print("Hemos empatado. Ambos hemos acertado en {} intentos.".format(intentos_maquina))
        repetir = input("Quieres seguir jugando? S/N ")
