"""
Desarrollar un programa que solicite una frase desde teclado, 
así como un caracter en específico, ya sea una letra, un número 
o caracter especial.

Posteriormente, el programa deberá imprimir en pantalla la frase 
ingresada desde teclado, "sin vocales", y en caso de que el caracter 
en específico sea parte de la frase, el bucle deberá finalizar su 
ejecución.

Requerimientos indispensables:
- Utilizar un ciclo o bucle, ya sea while o for.
- Considerar que el usuario puede ingresar vocales en mayúsculas y/o minúsculas.
"""

"yonel"
string = input("Introduzca una frase: ")
letra = input("Con que letra deseas terminar el bucle?: ")
string_sin_vocales = ""

vocales = "aeiou"
for character in string:
    if character == letra:
            break
    else:
        bandera = False
        for vocal in vocales:
            if vocal == character.lower():
                bandera = True
                break
        if bandera == False:
            string_sin_vocales = string_sin_vocales + character

print(string_sin_vocales)
