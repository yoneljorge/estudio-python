"""
Desarrollar un programa que invierta una cadena de caracteres, y a su vez, 
esta cadena de caracteres deberá ser ingresada por el usuario desde teclado.

Requrimientos indispensables:
- No se permite modificar la cadena de caracteres original.
- Utilizar el ciclo o bucle for.
"""

# yonel
string = input("Introduce un string para invertirlo: ")
string_invertido = ""

for character in string:
    string_invertido = character + string_invertido
    print(string_invertido)

print(f"Esta es el string invertido: {string_invertido}")