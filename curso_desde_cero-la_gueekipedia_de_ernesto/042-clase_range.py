"""
La clase range genera secuencias de números inmutables, es decir 
que no se pueden modificar, estas secuencias se generan a partir 
de un rango previamente establecido.

Generalmente la clase range, se utiliza como objeto iterable dentro 
de la sintaxis del ciclo o bucle for, con el cual se logran realizar 
las respectivas iteraciones.

Nos permite trabajar con un mínimo de un argumento y un máximo de tres
argumentos de manera simultánea.

Así  podremos decidir el número con el que comenzará y terminará la 
secuencia de números, y a su vez, indicar el incremento o el decremento 
entre un número y el siguiente.

La sintaxis para utilizar la clase range, es la siguiente:

range(stop)

stop: es un valor entero, que indica el número hasta el cual se va a 
generar la secuencia de números, y este número jamás formará parte de 
la secuencia.

range(start, stop)

start: es un valor entero, que indica el número a partir del cual se 
comenzará a generar la secuencia de números, y este número siempre 
formará parte de la secuencia.

range(start, stop, step)

step: es un valor entero, que indica el decremento o el incremento 
de la sucesión numérica entre un número y el siguiente.

"""

for indice in range(1, 5):
    print(indice)
    
print("Fin del programa")