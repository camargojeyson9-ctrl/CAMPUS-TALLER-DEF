# 1. Creo la funcion para area del triangulo.

def area (base,altura):
    resultado = base * altura/2
    return resultado

while True:
    base1 = int(input("Ingrese el valor de la base del Triangulo 1: "))
    altura1 = int(input("Ingrese el valor de la altura del Triangulo 1: "))
    base2 = int(input("Ingrese el valor de la base del Triangulo 2: "))
    altura2 = int(input("Ingrese el valor de la altura del Triangulo 2: "))

    if base1 > 0 and altura1 > 0 and base2 > 0 and altura2 > 0:

        area1 = area(base1, altura1)
        area2 = area(base2, altura2)

        suma_areas = area1+area2

        print("Areas: ", area1, area2, "suma: ",suma_areas)
        break
    else: 
        print("Los numeros ingresados deben ser mayores a 0")

        
    