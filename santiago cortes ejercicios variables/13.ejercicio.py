#Solicitar tiempo en segundos y transformar a horas y minutos.

t = int(input("Inserte el tiempo en segundos: "))

minutos = t / 60
h = t / 3600

print(f"El tiempo en minutos es: {minutos}")
print(f"El tiempo en horas es: {h}")
