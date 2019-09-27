import random

##Clase jugador
class Jugador:
    def __init__(self, nombre):
        self.nombre=nombre
        self.intentos=0
        
    def get_nombre(self):
        return self.nombre
    
    def get_intentos(self):
        return self.intentos
    
    def increment_intentos(self):
        self.intentos += 1
        
    def decrement_intentos(self):
        self.intentos -= 1
    
    def initialize_intentos(self):
        self.intentos=0

##Clase maquina
class Maquina:
    def __init__(self):
        self.intentos=0
        
    def get_intentos(self):
        return self.intentos
    
    def increment_intentos(self):
        self.intentos += 1
        
    def decrement_intentos(self):
        self.intentos -= 1
    
    def initialize_intentos(self):
        self.intentos=0
            
##Clase partida
class Partida:
    def __init__(self):
        self.maquina=Maquina()
        self.jugador=Jugador(self.nameJugador())
        
    def nameJugador(self):
        nombre_jugador=input("¡Hola! ¿Como te llamas?\n")
        return nombre_jugador
    
    ##El jugador adivina el numero de la maquina
    def adivinaJugador(self,jugador):
        jugador.initialize_intentos()
        jugador.increment_intentos()
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
                        jugador.increment_intentos()
                        if eval(b)<a:
                            print("Mi número es mayor")
                        else:
                            print("Mi número es menor")  
                        b=input()
            else:
                print("Error: No me has dado un número, por favor introduzca un número.")
        
        
    ##El ordenador adivina el numero del jugador
    def adivinaMaquina(self,maquina):
        x=0
        y=100
        r=' '
        maquina.initialize_intentos()
        while r != 'Correcto':
            maquina.increment_intentos()
            if x==y:
                print('Solo queda un número y es {}. Ese es el numero que has pensado.'.format(x))
                r='Correcto'
            else:
                a=getRandom(x,y)
                repeat = 'y'
                while repeat == 'y':
                    r=input('El número que has pensado es el {}.\nMayor/Menor/Correcto? '.format(a))
                    if r=='Correcto':
                        repeat='n'
                    elif r=='Mayor':
                        if a != y:
                            x=a+1
                            repeat='n'
                    elif r=='Menor':
                        if a != x:
                            y=a-1
                            repeat='n'
                    else:
                        print('Error: La respuesta no es valida.')
                        
    def juegaPartida(self):
        repetir="S"
        while repetir=="S":
            print("Bueno, {}, estoy pensando en un número entre 1 y 100. Intenta adivinarlo.".format(self.jugador.get_nombre()))
            self.adivinaJugador(self.jugador)
            print("¡Buen trabajo, {}! ¡Has adivinado mi número en {} intentos! Es tu turno.\n".format(self.jugador.get_nombre(), self.jugador.get_intentos()))
            self.adivinaMaquina(self.maquina)
            intentos_jugador=self.jugador.get_intentos()
            intentos_maquina=self.maquina.get_intentos()
            if intentos_jugador>intentos_maquina:
                print("\nYo gano. He acertado en {} intentos.".format(intentos_maquina))
            elif intentos_jugador<intentos_maquina:
                print("\nTu ganas. Has acertado en {} intentos.".format(intentos_jugador))
            else:
                print("\nHemos empatado. Ambos hemos acertado en {} intentos.".format(intentos_maquina))
            repetir = input("\nQuieres seguir jugando? S/N ")
     

        
##Obtenemos numero aleatorio
def getRandom(x,y):
    return random.randrange(x,y)



##Main - Estructura del juego
if __name__ == '__main__':
    partida=Partida()
    partida.juegaPartida()
