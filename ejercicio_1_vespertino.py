while True:
    try:
        # Solicitar la cantidad de habitaciones a registrar y transformar el valor a entero
        cantidad_habitaciones = int(input("Ingrese la cantidad de habitaciones a registrar: "))

        if cantidad_habitaciones > 0:
            break
        else:
            print("¡Cantidad inválida! Ingresa un entero positivo para continuar.")

    except ValueError:
        print("¡Cantidad inválida! Ingresa un entero positivo para continuar.")

# Establecemos un contador de habitaciones ejecutivas
cantidad_habitaciones_ejecutivas = 0

# Establecemos un contador de habitaciones estandar
cantidad_habitaciones_estandar = 0

for i in range(cantidad_habitaciones):
    
    while True:
        numero_habitacion = input(f"Ingrese el número de la habitación {i+1}/{cantidad_habitaciones}: ")

        if len(numero_habitacion) < 6 or " " in numero_habitacion:
            print("Numero de habitación incorrecto, debe tener más de 6 caracteres y no contener espacios")
        else:
            break

    while True:
        try:
            precio_habitacion = int(input(f"Ingrese el precio de la habitación {i+1}: "))

            if precio_habitacion > 0:                    
                break
            else:
                print("¡Error tarifario! Ingresa un número entero positivo para la tarifa nocturna.")

        except ValueError:
            print("¡Error tarifario! Ingresa un número entero positivo para la tarifa nocturna.")

    if precio_habitacion > 90000:
        cantidad_habitaciones_ejecutivas += 1
    else:
        cantidad_habitaciones_estandar += 1

print(f"¡El hotel cuenta con {cantidad_habitaciones_ejecutivas} Suites Ejecutivas y {cantidad_habitaciones_estandar} Habitaciones Estándar! ¡Check-in disponible!")