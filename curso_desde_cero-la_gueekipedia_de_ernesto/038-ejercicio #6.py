"""
Desarrollar un programa que elimine una palabra que forme parte de una cadena de caracteres.

Requerimientos indispensables:
- la cadena de caracteres deberá ser solicitada desde teclado.
- la palabra a eliminar deberá ser solicitada desde teclado.
"""

string = input("Introduzca una frase: ")
palabra = input("Introduzca la palabra que desea eliminar: ")

palabra_count = string.count(palabra)

if palabra_count > 0 :
    indice = string.find(palabra)
    substring = string[0:indice] + string[indice + len(palabra) + 1:]
    
    print(substring)
else: 
    print(f"Palabra {palabra} no encontrada")




