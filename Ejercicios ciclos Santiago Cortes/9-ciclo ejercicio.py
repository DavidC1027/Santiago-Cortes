#Escriba un programa para calcular el factorial de un número dado.

num = int(input("Ingresa un numero:"))
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(f"El factorial de {num} es: {factorial}")
