print("Bienvenido al programa para registro de habitaciones.")

cantidad_habitaciones = int(input("Ingrese la cantidad de habitaciones que desea registrar: "))

ejecutiva = 0
estandar = 0

for index in range (cantidad_habitaciones):
    
    numero_habitacion = input("Ingrese el número de la habitación: ")

    tarifa = int(input("Ingrese tarifa de la habitación: "))

    if tarifa > 90000: 
        ejecutiva = ejecutiva + 1
    else:
        estandar = estandar + 1

print(f"¡El hotel cuenta con {ejecutiva} Suites Ejecutivas y {estandar} Habitaciones Estándar! ¡Check-in disponible!")