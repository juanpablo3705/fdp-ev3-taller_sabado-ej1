print("¡Bienvenido al programa de registro de habitaciones!")

while True:
    try:
        cantidad_habitaciones = int(input("Ingrese la cantidad de habitaciones a  registrar: "))
        if cantidad_habitaciones > 0:
            break
        else:
            print("Error. Este valor debe ser un número entero positivo.")
    except ValueError:
        print("¡Cantidad inválida! Ingresa un entero positivo para continuar.")

ejecutiva = 0
estandar = 0

for index in range(cantidad_habitaciones):

    while True:
        numero_habitacion = input(f"Ingrese el número de la habitación {index + 1} (6 caracteres, sin espacios): ")
        if len(numero_habitacion) < 6 or (" " in numero_habitacion):
            print("Error. Debe tener al menos 6 caracteres sin espacios.")
        else:
            break

    while True:
        try:
            tarifa_habitacion = int(input(f"Ingrese tarifa de la habitación {index + 1}: "))
            if tarifa_habitacion > 0:
                break
            else:
                print("¡Error tarifario! Ingresa un número entero positivo para la tarifa nocturna.")
        except ValueError:
            print("¡Error tarifario! Ingresa un número entero positivo para la tarifa nocturna.")

    if tarifa_habitacion > 90000:
        ejecutiva = ejecutiva + 1
    else:
        estandar = estandar + 1

print(f"¡El hotel cuenta con {ejecutiva} Suites Ejecutivas y {estandar} Habitaciones Estándar! ¡Check-in disponible!")