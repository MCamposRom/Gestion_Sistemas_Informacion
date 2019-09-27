import random

##Clase jugador
class Jugador:
    def __init__(self, nombre):
        self.nombre=nombre
        self.intentos=0

##Clase maquina
class Maquina:
    def __init__(self):
        self.intentos=0
            
##Clase partida
class Partida:
    
    def juegaPartida(self):
        maquina = Maquina()
        nombre_jugador=input("¡Hola! ¿Como te llamas?\n")
        jugador=Jugador(nombre_jugador)
        repetir="S"
        while repetir=="S":
            print("Bueno, {}, estoy pensando en un número entre 1 y 100. Intenta adivinarlo.".format(jugador.nombre))
            jugador.intentos=self.adivinaJugador()
            print("¡Buen trabajo, {}! ¡Has adivinado mi número en {} intentos! Es tu turno.\n".format(jugador.nombre, jugador.intentos))
            maquina.intentos=self.adivinaMaquina()
            if jugador.intentos>maquina.intentos:
                print("\nYo gano. He acertado en {} intentos.".format(maquina.intentos))
            elif jugador.intentos<maquina.intentos:
                print("\nTu ganas. Has acertado en {} intentos.".format(jugador.intentos))
            else:
                print("\nHemos empatado. Ambos hemos acertado en {} intentos.".format(aquina.intentos))
            repetir = input("\nQuieres seguir jugando? S/N ")
        
    ##El jugador adivina el numero de la maquina
    def adivinaJugador():
        intentos = 1;
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
                        intentos += 1
                        if eval(b)<a:
                            print("Mi número es mayor")
                        else:
                            print("Mi número es menor")  
                        b=input()
                    if eval(b) == a:
                        return intentos
            else:
                print("Error: No me has dado un número, por favor introduzca un número.")
        
        
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
                    if r=='Mayor':
                        x=a+1
                        repeat='n'
                    elif r=='Menor':
                        y=a-1
                        repeat='n'
                    elif r=='Correcto':
                        return intentos
                    else:
                        print('Error: La respuesta no es valida.')

        
##Obtenemos numero aleatorio
def getRandom(x,y):
    return random.randrange(x,y)



##Main - Estructura del juego
if __name__ == '__main__':
    partida=Partida
    partida.juegaPartida(partida)
