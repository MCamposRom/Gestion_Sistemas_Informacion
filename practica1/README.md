practica1

He realizado el juego pedido en la Tarea de MiAulario. He seguido la estructura de la posible ejecución que ha dejado el profesor. 

He creado tres clases: la clase jugador con nombre e intentos, la clase máquina que solo tiene los intentos y la clase Pratida que se encarga de gestionar la partida (crear al jugador y a la máquina, juega la partida y ejecuta las funciones en las que adivina el jugador o la máquina)

He tenido en cuenta los posibles errores que puede cometer el usuario al introducir datos por la patalla: no introducir un número cuando se le pide tal cosa, superar el rango en el que se debe pensar el número o introducir mal las indicaciones a la máquina cuando ésta trata de adivinar su número ya sea porque escribe mal las opciones que la máquina le pide (Menor/Mayor/Correcto) o por que le da una indicación imposible (Por ejemplo, al preguntarle si su número es el mínimo del rango, el jugador no puede decirle que su número es menor, porque es imposible). En dicho caso, se le indica cual ha sido su error y se le pide que lo corrija. Como el codigo cuenta un intento en ese caso, decermento el número de intentos, porque es el usuario el que se ha equivocado, no la máquina.

Si se da el caso de que la máquina solo tiene un calor dentro del rango porque el minimo y el maximo son iguales, selo comunica al jugador diciendole que ese es su número y lo cuenta como un intento de la máquina.

Al finalizar la partida, como indicaba el profesor, el programa evalua quién ha ganado o si se ha producido un empate y lo comunica antes de preguntar al usuario si desea continuar jugando.
