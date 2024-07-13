import random
import csv

trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez",
                "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]

def asignar_sueldos_aleatorios():
    sueldos = []
    for _ in range(10):
        sueldo = random.randint(300000, 2500000)
        sueldos.append(sueldo)
    return sueldos

def clasificar_sueldos(sueldos):
    bajo_800k = []
    entre_800k_2m = []
    sobre_2m = []

    for i, sueldo in enumerate(sueldos):
        nombre = trabajadores[i]
        if sueldo < 800000:
            bajo_800k.append((nombre, sueldo))
        elif 800000 <= sueldo <= 2000000:
            entre_800k_2m.append((nombre, sueldo))
        else:
            sobre_2m.append((nombre, sueldo))

    print("Sueldos menores a $800.000\nTOTAL:", len(bajo_800k))
    for nombre, sueldo in bajo_800k:
        print(f"{nombre} ${sueldo}")

    print("\nSueldos entre $800.000 y $2.000.000\nTOTAL:", len(entre_800k_2m))
    for nombre, sueldo in entre_800k_2m:
        print(f"{nombre} ${sueldo}")

    print("\nSueldos superiores a $2.000.000\nTOTAL:", len(sobre_2m))
    for nombre, sueldo in sobre_2m:
        print(f"{nombre} ${sueldo}")

    total_sueldos = sum(sueldos)
    print("\nTOTAL SUELDOS: $", total_sueldos)

def ver_estadisticas(sueldos):
    sueldo_max = max(sueldos)
    sueldo_min = min(sueldos)
    promedio_sueldos = sum(sueldos) / len(sueldos)

    media_geom = 1
    for sueldo in sueldos:
        media_geom *= sueldo
    media_geom = media_geom ** (1 / len(sueldos))

    print(f"Sueldo más alto: ${sueldo_max}")
    print(f"Sueldo más bajo: ${sueldo_min}")
    print(f"Promedio de sueldos: ${promedio_sueldos:.2f}")
    print(f"Media geométrica de sueldos: ${media_geom:.2f}")

def reporte_sueldos(sueldos):
    with open('reporte_sueldos.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre empleado", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Líquido"])

        for i, sueldo in enumerate(sueldos):
            nombre = trabajadores[i]
            desc_salud = sueldo * 0.07
            desc_afp = sueldo * 0.12
            sueldo_liquido = sueldo - desc_salud - desc_afp

            writer.writerow([nombre, sueldo, desc_salud, desc_afp, sueldo_liquido])
    
    print("Se ha creado el archivo 'reporte_sueldos.csv' de manera correcta.")

def main():
    sueldos = []
    
    while True:
        print("\n---------MENU-----")
        print("selleciona una opcion.")
        print("1.-Asignar sueldos aleatorios")
        print("2.-clasificar sueldos")
        print("3.-Ver estadísticas")
        print("4.-Reporte de sueldos")
        print("5.-Salir del programa")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            sueldos = asignar_sueldos_aleatorios()
            print("Sueldos asignados aleatoriamente.")
        elif opcion == '2':
            if sueldos:
                clasificar_sueldos(sueldos)
            else:
                print("Primero debe asignar los sueldos aleatorios antes de seleccionar cualquier opcion (opción 1).")
        elif opcion == '3':
            if sueldos:
                ver_estadisticas(sueldos)
            else:
                print("Primero debes asignar los sueldos aleatorios antes de seleccionar cualquier opcion(opción 1).")
        elif opcion == '4':
            if sueldos:
                reporte_sueldos(sueldos)
            else:
                print("Primero debes asignar los sueldos aleatorios antes de selecionar cualquier opcion (opción 1).")
        elif opcion == '5':
            print("Finalizando programa...")
            print("Programa Desarrollado por Felipe Cartes Brito")
            print("RUT : 20.787.496-5")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opcion del menu.")

if __name__ == "__main__":
    main()