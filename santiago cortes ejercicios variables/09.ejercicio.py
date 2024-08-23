# Programa que permita a una tienda saber el valor que pagara un cliente por la compra de varios elementos de la misma referencia. 
# Debe tener como entradas el valor unitario, 
# la cantidad de productos comprados y al valor final se debe adicionar el 16% correspondiente al IVA.

valor_product = int(input("Inserte el valor del producto: "))
cantidad_product = int(input("Inserte cuantos producto comprara: "))

valor_vent_total = valor_product * cantidad_product
iva = valor_vent_total * 0.19

valor_final = valor_vent_total + iva

print(f"El valor total de los productos es: {valor_vent_total} ")
print(f"El valor del IVA es: {iva} ")
print(f"El valor final es: {valor_final} ")