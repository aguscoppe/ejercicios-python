def ingresarPaciente():
    listaTurno = []
    listaUrgencia = []
    numAfiliado = int(input("Ingrese el número de afiliado: "))
    while numAfiliado != -1:
        tipoTurno = int(input("Indique si viene por una urgencia (0) o si tiene turno (1): "))
        if tipoTurno == 0:
            listaUrgencia.append(numAfiliado)
        else:
            listaTurno.append(numAfiliado)
        numAfiliado = int(input("Ingrese el número de afiliado: "))
    return listaTurno, listaUrgencia

def realizarBusqueda(numAfiliado, listaTurno, listaUrgencia):
    turnos = 0
    urgencias = 0
    if numAfiliado in listaTurno:
        turnos = listaTurno.count(numAfiliado)
    if numAfiliado in listaUrgencia:
        urgencias = listaUrgencia.count(numAfiliado)
    return turnos, urgencias

# PROGRAMA PRINCIPAL
listaTurno, listaUrgencia = ingresarPaciente()

print()
print("Pacientes atendidos por urgencia:", *listaUrgencia)

print()
print("Pacientes con turno:", *listaTurno)

print()
afiliadoRandom = 1000
turnos, urgencias = realizarBusqueda(afiliadoRandom, listaTurno, listaUrgencia)
print("El paciente", afiliadoRandom, "se atendió", turnos, "veces por turno y", urgencias, "por urgencia")