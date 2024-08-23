#Programa para calcular la distancia recorrida en un movimiento rectilíneo. 
#Recuerde x=v*t donde v es velocidad y t es tiempo. 
#Solicitar al usuario velocidad en kilómetros por hora (Km/h) y tiempo en horas (h) para obtener la distancia en kilómetros (Km).

vel = int(input("Inserte la velocidad en km/h: "))
h = int(input("Inserte el tiempo en horas: "))

dist = vel * h

print(f"La distancia en kilometros es {dist} km")