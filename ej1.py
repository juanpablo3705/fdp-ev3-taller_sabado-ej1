print("Bienvenido al programa para registro de habitaciones.")

while True:
    try:
        cantidad_habitaciones = int(input("Ingrese la cantidad de habitaciones que desea registrar: "))
        if cantidad_habitaciones > 0:
            break
        else:
            print("¡Cantidad inválida! Ingresa un entero positivo para continuar.")
    except ValueError:
        print("¡Cantidad inválida! Ingresa un entero positivo para continuar.")

ejecutiva = 0
estandar = 0

for index in range (cantidad_habitaciones):
    
    while True:
        numero_habitacion = input(f"Ingrese el número de la habitación {index + 1}: ")
        if len(numero_habitacion) < 6 or " " in numero_habitacion:
            print("Error. El número de habitación debe tener 6 caracteres y no tener espacios.")
        else:
            break

    while True:
        try:
            tarifa = int(input(f"Ingrese tarifa de la habitación {index + 1}: "))
            if tarifa > 0:
                break
            else:
                print("¡Error tarifario! Ingresa un número entero positivo para la tarifa nocturna.")
        except ValueError:
            print("¡Error tarifario! Ingresa un número entero positivo para la tarifa nocturna.")

    if tarifa > 90000: 
        ejecutiva = ejecutiva + 1
    else:
        estandar = estandar + 1

print(f"¡El hotel cuenta con {ejecutiva} Suites Ejecutivas y {estandar} Habitaciones Estándar! ¡Check-in disponible!")