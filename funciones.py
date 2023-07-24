from clases import Paciente

def nuevoPaciente(nombre, edad, raza):
    paciente = Paciente(nombre, edad, raza)
    return paciente


def quitarPaciente(veterinaria, paciente):
    veterinaria.deletePaciente(paciente)


def listarPacientes(veterinaria):
    pacientes = veterinaria.getListado()
    if not pacientes:
        print("No hay pacientes en la base de datos de Mr.Firulays")
    else:
        for idx, paciente in enumerate(pacientes, start=1):
            print(f"{idx}. {paciente}")


def nuevaConsulta(paciente, motivo):
    paciente.setConsulta(motivo)


def obtenerDetallePaciente(paciente):
    return paciente.getDatos()