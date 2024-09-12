def rectangulo():
    if opcion == 1:
        largo = float(input("Ingrese el valor del largo: "))
        ancho = float(input("Ingrese el valor del ancho: "))
        area_rectangulo = largo * ancho
        print(f"El área del rectángulo es: {area_rectangulo}")
        
def cuadrado():
    if opcion == 2:
        lado = float(input("Ingrese el valor del lado: "))
        area_cuadrado = lado * lado
        print(f"El área del cuadrado es: {area_cuadrado}")
        
def paralelogramo():
    if opcion == 3:
        base = float(input("Ingrese la base: "))
        altura = float(input("Ingrese la altura: "))
        area_paralelogramo = base * altura
        print(f"El área del paralelogramo es: {area_paralelogramo}")
        
def rombo():
    if opcion == 4:
        diagonal_mayor = float(input("Ingrese la diagonal mayor: "))
        diagonal_menor = float(input("Ingrese la diagonal menor: "))
        area_rombo = (diagonal_mayor * diagonal_menor) / 2
        print(f"El área del rombo es: {area_rombo}")
        
def trapecio():
    if opcion == 5:
        base_superior = float(input("Ingrese la base superior: "))
        base_inferior = float(input("Ingrese la base inferior: "))
        altura = float(input("Ingrese la altura: "))
        area_trapecio = ((base_superior + base_inferior) / 2) * altura
        print(f"El área del trapecio es: {area_trapecio}")
        
def triangulo():
    if opcion == 6:
        base = float(input("Ingrese la base: "))
        altura = float(input("Ingrese la altura: "))
        area_triangulo = (base * altura) / 2
        print(f"El área del triángulo es: {area_triangulo}")
        
def triangulo_equilatero():
    if opcion == 7:
        lado = float(input("Ingrese el valor del lado: "))
        area_triangulo_equilatero = ((3**0.5) / 4) * (lado**2)
        print(f"El área del triángulo equilátero es: {area_triangulo_equilatero}")
        
def triangulo_rectangulo():
    if opcion == 8:
        cateto_adyacente = float(input("Ingrese el valor del cateto adyacente: "))
        cateto_opuesto = float(input("Ingrese el valor del cateto opuesto: "))
        area_triangulo_rectangulo = (cateto_adyacente * cateto_opuesto) / 2
        print(f"El área del triángulo rectángulo es: {area_triangulo_rectangulo}")
        
def poligono_regular():
    if opcion == 9:
        perimetro = float(input("Ingrese el valor del perímetro: "))
        apotema = float(input("Ingrese el valor de la apotema: "))
        area_poligono_regular = (perimetro * apotema) / 2
        print(f"El área del polígono regular es: {area_poligono_regular}")
        
opcion = int(input("""
    Elija una opción:
    (1) Rectángulo
    (2) Cuadrado
    (3) Paralelogramo
    (4) Rombo
    (5) Trapecio
    (6) Triángulo
    (7) Triángulo equilátero
    (8) Triángulo rectángulo
    (9) Polígono regular
"""))

rectangulo()
cuadrado()
paralelogramo()
rombo()
trapecio()
triangulo()
triangulo_equilatero()
triangulo_rectangulo()
poligono_regular()
