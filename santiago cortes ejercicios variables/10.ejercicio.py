# Programa que permita determinar el salario a pagar a un empleado, 
# teniendo como entradas el salario diario y el número de días trabajados. 
# Tenga en cuenta que al empleado se le debe descontar el 10% por concepto de pensión y 15% por concepto de salud.

salario_diario = int(input("Inserte el salario diario del empleado: "))
numerodias_trabaj = int(input("Inserte el numero de dias trabajados del empleado: "))

suma_sueldo = salario_diario * numerodias_trabaj
pension = suma_sueldo * 0.10
salud = suma_sueldo * 0.15

salario_final = suma_sueldo - pension - salud

print(f"la suma del sueldo es: {suma_sueldo}")
print(f"El valor de la pensiom es: {pension}")
print(f"El valor de la salud es: {salud}")
print(f"El sueldo fin al del empleado es: {salario_final}")