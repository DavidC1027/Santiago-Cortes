#Programa que permita ingresar 5 números y calcular el promedio.

numero1 = int(input("Inserte el primer número: "))
numero2 = int(input("Inserte el segundo número: "))
numero3 = int(input("Inserte el tercer número: "))
numero4 = int(input("Inserte el cuarto número: "))
numero5 = int(input("Inserte el quinto número: "))

suma = numero1 + numero2 + numero3 + numero4 + numero5
promedio = suma / 5

print(f"El promedio de los numeros insertados es: {promedio}")