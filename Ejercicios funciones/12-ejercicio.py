#Escriba una función que compruebe si una cadena frase o palabra pasada es palíndromo o no. 
# Una palabra o frase que es palíndromo se lee igual de izquierda a derecha que de derecha a izquierda. 
# Por ejemplo: Ana, Anita lava la tina.

def es_palindromo(cadena):
  """Comprueba si una cadena es un palíndromo.

  Args:
    cadena: La cadena a evaluar.

  Returns:
    True si la cadena es un palíndromo, False en caso contrario.
  """

  # Convertir la cadena a minúsculas y eliminar espacios
  cadena = cadena.lower().replace(" ", "")

  # Invertir la cadena
  cadena_invertida = cadena[::-1]

  # Comparar la cadena original con la invertida
  return cadena == cadena_invertida

# Ejemplo de uso:
palabra = input("Ingrese una palabra o frase: ")
if es_palindromo(palabra):
  print("Es un palíndromo.")
else:
  print("No es un palíndromo.")