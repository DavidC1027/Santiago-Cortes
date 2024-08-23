#Programa que permita calcular la edad de una persona conociendo el año actual y el usuario digita su año de nacimiento.

año_actu = int(input("Inserte el año actual: "))
año_nacimiento = int(input("Inserte el año de nacimiento: "))

edad = año_actu - año_nacimiento

print(f"la edad es: {edad}")