import clases
import funciones

def mostrar_menu():
    print("╔════════════════════════════════════════╗")
    print("║               MENU PRINCIPAL           ║")
    print("╠════════════════════════════════════════╣")
    print("║ 1. Listar pacientes                    ║")
    print("║ 2. Detallar un paciente                ║")
    print("║ 3. Cargar nuevo paciente               ║")
    print("║ 4. Quitar paciente                     ║")
    print("║ 5. Cargar consulta                     ║")
    print("║ 6. Dar de alta tratamiento médico      ║")
    print("║ 7. Salir                               ║")
    print("╚════════════════════════════════════════╝")

def progPrincipal():
    veterinaria = clases.Veterinaria()
    print("¡Bienvenido a Mr.Firulays!")

    while True:
        print()
        mostrar_menu()
        opcion = input("Ingrese el número de opción que desee: ")

        if opcion == "1":
            print("\n--- Listado de pacientes ---")
            funciones.listarPacientes(veterinaria)
        elif opcion == "2":
            print("\n--- Detalle de paciente ---")
            funciones.listarPacientes(veterinaria)
            paciente_idx = int(input("Ingrese el número de paciente que desea detallar: ")) - 1
            if 0 <= paciente_idx < len(veterinaria.getListado()):
                paciente = veterinaria.getListado()[paciente_idx]
                detalle_paciente = funciones.obtenerDetallePaciente(paciente)
                print("Detalles del paciente:")
                for key, value in detalle_paciente.items():
                    print(f"{key}: {value}")
            else:
                print("Número de paciente inválido.")
        elif opcion == "3":
            print("\n--- Cargar nuevo paciente ---")
            nombre = input("Nombre del paciente: ")
            edad = int(input("Edad del paciente: "))
            raza = input("Raza del paciente: ")
            nuevo_paciente = funciones.nuevoPaciente(nombre, edad, raza)
            veterinaria.setPaciente(nuevo_paciente)
            print("¡Paciente agregado correctamente!")
        elif opcion == "4":
            print("\n--- Quitar paciente ---")
            funciones.listarPacientes(veterinaria)
            paciente_idx = int(input("Ingrese el número de paciente que desea quitar: ")) - 1
            if 0 <= paciente_idx < len(veterinaria.getListado()):
                paciente = veterinaria.getListado()[paciente_idx]
                funciones.quitarPaciente(veterinaria, paciente)
                print("¡Paciente eliminado correctamente!")
            else:
                print("Número de paciente inválido.")
        elif opcion == "5":
            print("\n--- Cargar consulta ---")
            funciones.listarPacientes(veterinaria)
            paciente_idx = int(input("Ingrese el número de paciente al que desea cargar la consulta: ")) - 1
            if 0 <= paciente_idx < len(veterinaria.getListado()):
                paciente = veterinaria.getListado()[paciente_idx]
                motivo_consulta = input("Ingrese el motivo de la consulta: ")
                funciones.nuevaConsulta(paciente, motivo_consulta)
                print("Consulta agregada correctamente.")
            else:
                print("Número de paciente inválido.")
        elif opcion == "6":
            print("\n--- Dar de alta tratamiento médico ---")
            funciones.listarPacientes(veterinaria)
            paciente_idx = int(input("Ingrese el número de paciente al que desea dar de alta el tratamiento médico: ")) - 1
            if 0 <= paciente_idx < len(veterinaria.getListado()):
                paciente = veterinaria.getListado()[paciente_idx]
                paciente.paciente_con_tratamiento_medico = True
                print("¡Tratamiento médico dado de alta!")
            else:
                print("Número de paciente inválido.")
        elif opcion == "7":
            print("\n¡Gracias por utilizar Mr.Firulays!")
            break
        else:
            print("Opción inválida. Por favor, elija una opción válida.")

if __name__ == "__main__":
    progPrincipal()
