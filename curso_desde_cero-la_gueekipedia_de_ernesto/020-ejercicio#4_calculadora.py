"""
Desarrollar una calculadora con las siguientes características:

1- La calculadora deberá ser capaz de calcular las operaciones de suma, resta, 
multiplicación, división, división entera, exponente y módulo o resto.
2- La calculadora deberá tener un menú de opciones donde el usuario pueda 
elegir cual es la operación que desea ejecutar.
3- La calculadora deberá solicitar únicamente dos valores por cada operación.

Requerimientos indispensables:

El código de este programa deberá funcionar con una única variable que se 
llamará numero, es decir, no se permite la implementación de otra variable.
"""

print("""
      ********************
      * Menú de opciones *
      ********************
      1. Suma
      2. Resta
      3. Multiplicación
      4. División
      5. División entera
      6. Exponente
      7. Módulo o resto
      """)

opcion = int(input("Introduce la opción deseada: "))

if opcion == 1:
    numero = int(input("Introduce el primer número: "))
    numero = numero + int(input("Introduce el segundo número: "))
    print("El resultado de la suma es {}".format(numero))
elif opcion == 2:
    numero = int(input("Introduce el primer número: "))
    numero = numero - int(input("Introduce el segundo inúmero: "))
    print("El resultado de la resta es {}".format(numero))
elif opcion == 3:
    numero = int(input("Introduce el primer número: "))
    numero = numero * int(input("Introduce el segundo número: "))
    print("El resultado de la multiplicación es {}".format(numero))
elif opcion == 4:
    numero = int(input("Introduce el primer número: "))
    numero = numero / int(input("Introduce el segundo número: "))
    print("El resultado de la división es {}".format(numero))
elif opcion == 5:
    numero = int(input("Introduce el primer número: "))
    numero = numero // int(input("Introduce el segundo número: "))
    print("El resultado de la división entera es {}".format(numero))
elif opcion == 6:
    numero = int(input("Introduce el primer número: "))
    numero = numero ** int(input("Introduce el segundo número: "))
    print("El resultado de la potencia es {}".format(numero))
elif opcion == 7:
    numero = int(input("Introduce el primer número: "))
    numero = numero % int(input("Introduce el segundo número: "))
    print("El modulo o resto es {}".format(numero))