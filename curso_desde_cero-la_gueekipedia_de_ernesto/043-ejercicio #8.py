"""
Desarrolla un programa que muestre en pantalla, la tabla de 
multiplicar de un número cualquiera, este número deberá ser 
solicitado e ingresado desde teclado por el usuario.

Requerimientos indispensables:
- Utilizar el ciclo o bucle for.
- La tabla debe contener las multiplicacines que van desde el 0 hasta el 10.
"""

numero = int(input("Que tabla de multiplicar quieres ver?: "))

print(f"La tabla del {numero} es: ")

for indice in range(0, 11):
    print(f"{numero} x {indice} = {numero * indice}")