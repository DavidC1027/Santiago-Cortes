#Escribe un programa para copiar los elementos 44 y 55 de la siguiente tupla en una nueva tupla.


tuple1 = (11, 22, 33, 44, 55, 66)


for i in tuple1:
    if i == 44:
        tuple2 = [i]
    if i == 55:
        tuple2.append(i)
        
tuple2 = tuple(tuple2)
print(tuple2)