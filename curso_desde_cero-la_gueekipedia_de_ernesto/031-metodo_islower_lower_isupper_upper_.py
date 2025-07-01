"""
Metodo islower() y lower() nos permiten saber si todos los caracteres de una 
cadena de texto son minusculas y cambiarlas todas a minusculas.

Metodo isupper() y upper() lo contrario de islower() y lower()
"""
string = input("Introduce un String: ") 

print(f"\nTodas las letras están en minúsculas?: {string.islower()}")
string.islower()
print(f"String en minúsculas: {string.lower()}")

print(f"\nTodas las letras están en mayúsculas?: {string.isupper()}")
print(f"String en mayúsculas: {string.upper()}")

print(f"String original: {string}")
