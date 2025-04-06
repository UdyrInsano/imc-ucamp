def calcular_imc(peso, estatura):
    return peso / (estatura ** 2)

def obtener_datos():
    while True:
        nombre = input("Ingresa tu nombre: ").strip()
        if nombre:
            break
        print("El nombre no puede estar vacío.")

    while True:
        apellido_paterno = input("Ingresa tu apellido paterno: ").strip()
        if apellido_paterno:
            break
        print("El apellido paterno no puede estar vacío.")

    while True:
        apellido_materno = input("Ingresa tu apellido materno: ").strip()
        if apellido_materno:
            break
        print("El apellido materno no puede estar vacío.")

    while True:
        try:
            edad = int(input("Ingresa tu edad: "))
            break
        except ValueError:
            print("Debes ingresar un número válido para la edad.")

    while True:
        try:
            peso = float(input("Ingresa tu peso en kilogramos: "))
            break
        except ValueError:
            print("Debes ingresar un número válido para el peso.")

    while True:
        try:
            estatura = float(input("Ingresa tu estatura en metros: "))
            break
        except ValueError:
            print("Debes ingresar un número válido para la estatura.")

    return nombre, apellido_paterno, apellido_materno, edad, peso, estatura

nombre, apellido_paterno, apellido_materno, edad, peso, estatura = obtener_datos()

imc = calcular_imc(peso, estatura)

print("\nInformación del usuario:")
print(f"Nombre completo: {nombre} {apellido_paterno} {apellido_materno}")
print(f"Edad: {edad} años")
print(f"Peso: {peso:.2f} kg")
print(f"Estatura: {estatura:.2f} m")
print(f"Índice de Masa Corporal (IMC): {imc:.2f}")