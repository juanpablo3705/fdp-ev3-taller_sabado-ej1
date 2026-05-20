print("¡Bienvenido al sistema de registro de habitaciones!")

ejecutiva = 0
estandar = 0

while True:
    try:
        numero_habitaciones = int(input("Ingrese el número de habitaciones a registrar: "))
        if numero_habitaciones > 0:
            break
        else:
            print("¡Cantidad inválida! Ingresa un entero positivo para continuar.")
    except ValueError:
        print("¡Cantidad inválida! Ingresa un entero positivo para continuar.")

for index in range(numero_habitaciones):

    while True:
        nombre_habitacion = input(f"Ingrese número de la habitación {index + 1} (6 caracteres, sin espacios): ")
        if (len(nombre_habitacion) < 6) or (" " in nombre_habitacion):
            print("Error. El nombre debe tener al menos 6 caracteres y no tener espacios.")
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
