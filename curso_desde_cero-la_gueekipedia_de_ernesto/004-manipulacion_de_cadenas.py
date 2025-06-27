mensaje = "Hola Yonel"

'''
La Búsqueda: consiste en localizar dentro de una cadena, una subcadena más pequeña a un carácter.

Para lo caul es necesario utilizar el método find.
'''
print("Búsqueda")
buscar_subcadena = mensaje.find("Yonel")
print(buscar_subcadena)

'''
La extracción: se trata de sacer fuera de una cadena, una porción de la misma según su posición dentro de ella.

Para ello es necesario indicar la posición a extraer [1:8].
'''
print("Extracción:")

extraer_cadena = mensaje[1:6]
print(extraer_cadena)

print("Comparación")

mensaje_uno = "Hola"
mensaje_dos = "Hola"
print(mensaje_uno == mensaje_dos)
