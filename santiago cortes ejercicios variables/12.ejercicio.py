#Calcular la hipotenusa con el Teorema de Pitágoras (sin usar funciones).

a = float(input("Inserte el valor del primer cateto: "))
b = float(input("Inserte el valor del segundo cateto: "))

hipo = (a**2 + b**2) ** 0.5

print(f"El valor de la hipotenusa es : {hipo}")