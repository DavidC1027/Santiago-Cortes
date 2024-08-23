#Solicitar al usuario una distancia en metros y transformar a km., cm. y mm.

Dist = int(input("Inserte la distancia en metros: "))

km = Dist / 1000
cm = Dist * 100
mm = Dist * 1000 

print(f"La distancia en kilometros es: {km} km")
print(f"La distancia en centimetros es: {cm} cm")
print(f"La distancia en milimetros es: {mm} mm")
