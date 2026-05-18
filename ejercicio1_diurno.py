# Validación hasta que el usuario ingrese un valor correcto
while True:
    try:
        # Solicitar la cantidad de habitaciones y la transformamos en numero entero
        cantidad_habitaciones = int(input("Ingresa la cantidad de habitaciones a registrar: "))

        if cantidad_habitaciones < 0:
            print("¡Cantidad inválida! Ingresa un entero positivo para continuar.")
        else:
            break
    except Exception:
        print("¡Cantidad inválida! Ingresa un entero positivo para continuar.")

# Contadores de habitaciones según su clasificación
contador_ejecutivas = 0
contador_estandar = 0

# while o for
# range(1, 5) -> ejecuta el bloque desde 1 hasta 5
# range(5) -> ejecuta el bloque desde 0 hasta 5
# range(1, 10, 2) -> ejecutar el bloque de 2 en 2
for i in range(cantidad_habitaciones):
    
    while True:
        # Solicitando el número de habitación como texto
        numero_habitacion = input(f"Ingrese el número de habitación {i + 1}: ")

        if (len(numero_habitacion) < 6 or " " in numero_habitacion):
            print("El número de habitación debe tener al menos 6 caracteres")
            print("El número de habitación no debe tener espacios")
        else:
            break
    
    while True:
        try:
            # Solicitando el precio como entero
            precio_habitacion = int(input(f"Ingrese el precio de la habitación {i + 1} : "))

            if precio_habitacion > 0:
                break
            else: 
                print("¡Error tarifario! Ingresa un número entero positivo para la tarifa nocturna.")
        except Exception:
                print("¡Error tarifario! Ingresa un número entero positivo para la tarifa nocturna.")

    if (precio_habitacion <= 90000):
        contador_estandar += 1
        # contador_estandar = contador_estandar +1
    else:
        contador_ejecutivas += 1

print(f"¡El hotel cuenta con {contador_ejecutivas} Suites Ejecutivas y {contador_estandar} Habitaciones Estándar! ¡Check-in disponible!")