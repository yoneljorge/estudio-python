"""
Desarrolla un programa que solicite un número entero desde teclado al usuario,
posteriormente, el programa deberá determinar e indicar a través de un mensaje, 
si el número introducido es par o impar.

Requerimientos indispensables: 
El mensaje en pantalla deberá mostrar la frase el número es par o impar, 
junto con el número que el usuario introdujo desde teclado, por ejemplo: 

El número 8 es par.
El número 5 es impar.
"""
numero = int(input("Introduce un número entero: "))

if numero % 2 == 0 :
    print("El número {} es par".format(numero))
else:
    print("El número {} es impar.".format(numero))